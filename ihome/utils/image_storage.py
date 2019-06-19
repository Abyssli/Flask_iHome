# -*- coding: utf-8 -*-

from qiniu import Auth, put_data, etag, urlsafe_base64_encode
# import qiniu.config

# 需要填写你的 Access Key 和 Secret Key
access_key = 'sZC2Rs6kCLVQjuj2CaHqMV2gPjeEIBSZpUw07DXY'
secret_key = 'uMOeb6YIUJFVhDmgXyWTkPUB7oyF4c_hl6mr1IPl'


def storage(file_data):
    """
    上传文件到七牛
    :param file_data: 要上传的文件数据
    :return:
    """
    # 构建鉴权对象
    q = Auth(access_key, secret_key)

    # 要上传的空间
    bucket_name = 'ihome'

    # 生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name, None, 3600)

    ret, info = put_data(token, None, file_data)

    # print(info)
    # print("*"*10)
    # print(ret)
    if info.status_code == 200:
        # 表示上传成功, 返回文件名
        return ret.get("key")
    else:
        # 上传失败
        raise Exception("上传七牛失败")


if __name__ == '__main__':
    with open("./banner03.jpg", "rb") as f:
        file_data = f.read()
        storage(file_data)
