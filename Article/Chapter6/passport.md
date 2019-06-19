# 注册后端接口逻辑代码
代码地址： /ihome/api_1_0/passport.py
```python
# coding: utf-8

from . import api
from flask import request, jsonify, current_app, session
from ihome import redis_store, db
from ihome.utils.response_code import RET
from ihome.models import User
from sqlalchemy.exc import IntegrityError
import re

@api.route("/users", methods=["POST"])
def register():
    """注册
    请求的参数： 手机号,短信验证码,密码, 确认密码
    参数格式: json
    """
    # 获取请求的json数据,返回字典
    req_dict = request.get_json()

    mobile = req_dict.get("mobile")
    sms_code = req_dict.get("sms_code")
    password = req_dict.get("password")
    password2 = req_dict.get("password2")

    # 校验参数
    if not all([mobile, sms_code, password, password2]):
        return jsonify(errno=RET.PARAMERR, errmag="参数不完整")

    # 判断手机号格式
    if not re.match(r"1[34578]\d{9}", mobile):
        # 表示格式不对
        return jsonify(errno=RET.PARAMERR, errmag="手机号格式错误")

    if password != password2:
        return jsonify(errno=RET.PARAMERR, errmag="两次密码不一致")

    # 从redis中取出短信验证码
    try:
        real_sms_code = redis_store.get("sms_code_%s" % mobile)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmag="读取真实短信验证码异常")

    # 判断短信验证码是否过期
    if real_sms_code is None:
        return jsonify(errno=RET.NODATA, errmag="短信验证码失效")

    #删除redis中的短信验证码,防止重复使用校验
    try:
        redis_store.delete("sms_code_%s" % mobile)
    except Exception as e:
        current_app.logger.error(e)

    # 判断用户填写的短信验证码正确性
    if real_sms_code != sms_code:
        return jsonify(errno=RET.NODATA, errmag="短信验证码错误")

    # 判断手机号是否存在,是否已注册
    # try:
    #     user = User.query.filter_by(mobile=mobile).first()
    # except Exception as e:
    #     current_app.logger.error(e)
    #     return jsonify(errno=RET.DBERR, errmag="数据库异常")
    # else:
    #     if user is not None:
    #         # 表示手机号已存在
    #         return jsonify(errno=RET.DATAEXIST, errmag="手机号已存在")

    # 注册
    # 用户1 password="123456" + "abc"  sha1 abc$ifmgivmopape
    # 用户2 password="123456" + "dfc"  sha1 dfc$dfefivmopape

    # 用户登录 password = ”123456“ + sha256

    # 保存用户的注册数据到数据库中
    user = User(name=mobile, mobile=mobile)

    user.password = password # 设置属性

    try:
        db.session.add(user)
        db.session.commit()
    except IntegrityError as e:
        # 数据库操作错误后的回滚
        db.session.rollback()
        # 表示手机号出现了重复值,即手机号已注册
        current_app.logger.error(e)
        return jsonify(errno=RET.DATAEXIST, errmag="手机号已存在")
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmag="查询数据库异常")

    # 保存登录状态到session中
    session["name"] = mobile
    session["mobile"] = mobile
    session["user_id"] = user.id

    # 返回结果
    return jsonify(errno=RET.OK, errmsg="注册成功")
```