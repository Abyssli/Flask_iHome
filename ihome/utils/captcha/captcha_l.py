from captcha.image import ImageCaptcha
# 验证码的包
from PIL import Image
import random
import time
# 系统模块
import os


# 定义随机方法
def random_captcha():
    # 做一个容器
    captcha_text = []
    for i in range(4):
        # 定义验证码字符 指定随机
        c = random.choice(['0', '1', '2', '3', '4','5','6','7','8','9'])
        captcha_text.append(c)
    # 返回一个随机生成的字符串
    return ' '.join(captcha_text)  # 字符串中间没有空格


# 生成验证码方法
def gen_capthca():

    #定义图片对象
    image = ImageCaptcha()
    # 获取字符串
    captcha_text = random_captcha()
    # 生成图像
    captcha_image = Image.open(image.generate(captcha_text))
    return captcha_text, captcha_image

# if __name__ == "__main__":
# 定义图片个数
# count = 1
# # 定义图片文件夹
# path = './captcha_image'
# # 如果没有就创建
# if not os.path.exists(path):
#     os.makedirs(path)

# 循环创建图片
# for i in range(count):
#     # 定义创建时间
#     now = str(int(time.time()))
#     # 接收字符串和图片
#     text, image = gen_capthca()
#     # 定义图片名称
#     filename = text + '_' + now + '.png'
#     # 存储图片
#     image.save(path + os.path.sep + filename)
#     print('saved %s' % filename)
