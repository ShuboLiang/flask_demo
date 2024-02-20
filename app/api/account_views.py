from app.api import account_bp
from app.services import *
from app.utils import json_response
from app.errors import CustomError


@account_bp.route("/", methods=["GET"])
def get_users():
    raise CustomError("CustomError")
    all_users = get_all_users()
    return json_response(all_users)
