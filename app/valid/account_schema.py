from marshmallow import Schema, fields, ValidationError, INCLUDE


# 定义校验数据的Schema
class AccountSchema(Schema):
    name = fields.Str(required=True, error_messages={"required": "Name is required."})
    age = fields.Int(
        required=True,
        validate=lambda x: x > 0,
        error_messages={
            "required": "Age is required.",
            "invalid": "Age must be a positive integer.",
        },
    )
