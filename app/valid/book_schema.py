from marshmallow import Schema, fields, ValidationError, INCLUDE


# 定义校验数据的Schema
class BookSchema(Schema):
    id = fields.Int(required=False, error_messages={"required": "id is required."})
