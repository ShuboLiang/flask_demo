from flask import Flask
from app.api import account_bp, product_bp
from config import config
from app.models import db
from app.errors import *


def create_app(config_name):
    app = Flask(__name__)
    # 应用配置
    app.config.from_object(config[config_name])

    app.register_blueprint(account_bp, url_prefix="/api/users")
    app.register_blueprint(product_bp, url_prefix="/api/products")

    db.init_app(app)

    app.register_error_handler(CustomError, handle_custom_error)

    return app
