from flask import Flask
from flask_restful import Resource, Api
from app.valid import validate_with_schema, BookSchema


class BookAPI(Resource):
    @validate_with_schema(BookSchema(), data_source="query")
    def get(self, id=None):
        if id is None:
            return "book1, book2, book3"
        else:
            # 返回特定书籍
            return "book with id"

    def post(self):
        # 创建新书籍
        pass
