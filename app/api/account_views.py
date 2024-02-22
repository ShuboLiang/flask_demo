from app.api import account_bp
from app.services import *
from app.utils import json_response
from app.valid import validate_with_schema, AccountSchema
from flask.views import MethodView


@account_bp.route("/all", methods=["GET"])
@validate_with_schema(AccountSchema(), data_source="query")
def get_all_users():
    all_users = get_all_users()
    return json_response(all_users)


class UserView(MethodView):
    def get(self, user_id):
        all_users = get_all_users()
        return json_response(all_users)
