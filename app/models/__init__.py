from flask_sqlalchemy import SQLAlchemy

# 初始化 SQLAlchemy 实例
db = SQLAlchemy()

# 导入所有的模型类，以确保它们被 SQLAlchemy 注册
from .account_model import Accounts
# ... 其他模型的导入 ...

# 其他可能的数据库相关的初始化代码