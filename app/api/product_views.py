from app.api import product_bp
from app.errors import CustomError


@product_bp.route("/", methods=["GET"])
def get_product():
    raise CustomError("CustomError")
    return "get_product"
