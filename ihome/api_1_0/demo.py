# coding:utf-8
from . import api
from ihome import db,models
import logging
from flask import current_app

@api.route('/index')
def index():

    # logging.error("fhaas")  #错误级别
    # logging.warn("") #警告级别
    # logging.info("") #消息提示级别
    # logging.debug("") #调试级别
    current_app.logger.error("error msg")
    current_app.logger.warn("warn msg")
    current_app.logger.info("info msg")
    current_app.logger.debug("debug msg")

    return "index_page"
