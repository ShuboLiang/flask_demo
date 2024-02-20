from app.utils import json_error_response


class CustomError(Exception):
    pass


def handle_custom_error(error):
    return json_error_response(message=str(error))
