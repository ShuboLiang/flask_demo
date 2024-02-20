from .CustomError import *
from app.utils import json_error_response


def unsupported_media_type(error):
    return json_error_response(message="Unsupported media type", status=415)
