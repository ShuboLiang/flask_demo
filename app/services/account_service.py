from app.models import Accounts


def get_all_users():
    data = Accounts.query.all()
    res = [
        {
            "id": user.id,
            "username": user.username,
        }
        for user in data
    ]

    return res
