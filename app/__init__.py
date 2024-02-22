from flask import Flask
from app.api import *
from config import config
from app.models import db
from app.errors import *
from app.cache import cache
from flask_migrate import Migrate
from flask_restful import Api


def create_app(config_name):
    app = Flask(__name__)
    # 应用配置
    app.config.from_object(config[config_name])
    cache.init_app(app)

    app.register_blueprint(account_bp, url_prefix="/api/users")
    app.register_blueprint(product_bp, url_prefix="/api/products")
    app.register_blueprint(cache_bp, url_prefix="/api/cache")

    db.init_app(app)
    migrate = Migrate(app, db)
    migrate.init_app(app, db)
    app.register_error_handler(CustomError, handle_custom_error)
    app.register_error_handler(415, unsupported_media_type)
    api = Api(app)
    api.add_resource(BookAPI, "/books/", "/books/<int:id>")

    return app
