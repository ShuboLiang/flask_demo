from flask import Flask
from app.api import *
from config import config
from app.models import db
from app.errors import *
from app.cache import cache
from flask_migrate import Migrate
from flask_restful import Api
from flask_cors import CORS


def create_app(config_name):
    app = Flask(__name__)
    # 应用配置
    app.config.from_object(config[config_name])

    # 缓存配置
    cache.init_app(app)

    # 注册蓝图
    app.register_blueprint(account_bp, url_prefix="/api/users")
    app.register_blueprint(product_bp, url_prefix="/api/products")
    app.register_blueprint(cache_bp, url_prefix="/api/cache")

    # 数据库配置
    db.init_app(app)
    migrate = Migrate(app, db)
    migrate.init_app(app, db)

    # 错误处理
    app.register_error_handler(CustomError, handle_custom_error)
    app.register_error_handler(415, unsupported_media_type)

    # 注册api
    api = Api(app)
    api.add_resource(BookAPI, "/books/", "/books/<int:id>")

    # 跨域配置
    CORS(app, resources={r"/*": {"origins": "*"}})
    return app
