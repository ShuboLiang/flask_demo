import os


# 基础配置
class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "a_default_secret_key"
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get("DATABASE_URL") or "sqlite:///my_database.db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
    TESTING = False
    # ... 其他的通用配置 ...


# 测试环境配置
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    # ... 测试环境专属配置 ...


# 生产环境配置
class ProductionConfig(Config):
    # ... 生产环境专属配置 ...
    pass


# 开发环境配置
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = (
        "mysql+pymysql://weather:weather%40123@106.13.179.38:6024/weather_bishe"
    )
    # ... 开发环境专属配置 ...


# 导出配置字典，便于应用工厂使用
config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig,
}
