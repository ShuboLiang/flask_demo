# 初始化蓝图和路由
from flask import Blueprint

account_bp = Blueprint("account", __name__)
product_bp = Blueprint("product", __name__)
cache_bp = Blueprint("cache", __name__)
from . import cached_views
from . import account_views
from . import product_views
