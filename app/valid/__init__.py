from flask import Flask, request, jsonify
from marshmallow import Schema, fields, ValidationError, INCLUDE
from functools import wraps
from app.utils import json_error_response


def validate_with_schema(schema, data_source="json"):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if data_source == "json":
                data = request.get_json()
            elif data_source == "form":
                data = request.form
            elif data_source == "query":
                data = request.args
            else:
                return json_error_response(message="Invalid data source", status=400)

            if not data:
                return json_error_response(message="No input data provided", status=400)

            try:
                # 校验数据
                validated_data = schema.load(data)
            except ValidationError as err:
                # 如果校验失败，返回错误信息，包括具体的字段和错误详情
                return json_error_response(
                    message="Validation Error", status=400, errors=err.messages
                )

            # 如果校验成功，将校验后的数据存储在`request`对象中
            request.validated_data = validated_data
            return f(*args, **kwargs)

        return wrapper

    return decorator


from .account_schema import *
