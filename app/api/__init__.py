# 初始化蓝图和路由
from flask import Blueprint

account_bp = Blueprint("account", __name__)
product_bp = Blueprint("product", __name__)
from . import account_views
from . import product_views
