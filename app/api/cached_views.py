from app.api import cache_bp
from app.services import *
from app.utils import json_response
from flask import request
from app.cache import cache


def make_custom_cache_key(*args, **kwargs):
    path = request.path
    return path + str(frozenset(request.args.items()))


# 第一次访问时，会读取数据库，之后会直接从缓存中读取，直到缓存过期（timeout为过期时间）
@cache_bp.route("/", methods=["GET"])
@cache.cached(timeout=60)
def cached_all_users():
    all_users = get_all_users()
    return json_response(all_users)


# 函数自定义前缀
# 通过make_custom_cache_key函数自定义缓存键
# 通过request.path和request.args生成缓存键
# 比如：/api/cache/ 会生成/api/cache/{}，/api/cache/?a=1&b=2 会生成/api/cache/{'a': '1', 'b': '2'}
@cache_bp.route("/", methods=["GET"])
@cache.cached(timeout=60, key_prefix=make_custom_cache_key)
def cached_users():
    all_users = get_all_users()
    return json_response(all_users)
