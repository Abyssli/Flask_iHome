import redis

class Config(object):
    """
        配置信息
    """
    SECRET_KEY = "XHSOI*Y9dfs9cshd9"

    DEBUG = True

    # 数据库
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@127.0.0.1:3306/ihome_python04"
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # redis
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    # flask-session配置
    SESSION_TYPE = "redis"
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST,port=REDIS_PORT)
    SESSION_USE_SIGNER = True #对cookie中的session_id进行隐藏
    PERMANENT_SESSION_LIFETIME = 60*60*24 #session数据的有效期


class DevelopmentConfig(Config):
    """
        开发模式的配置信息
    """
    DEBUG = True

class ProductionConfig(Config):
    """
        生成环境配置信息
    """
    pass

config_map = {
    "develop":DevelopmentConfig,
    "peoduct":ProductionConfig

}