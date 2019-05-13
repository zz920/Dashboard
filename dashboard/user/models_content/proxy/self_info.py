from user.models_content.user import User


class UserSelfInfoProxy(User):

    class Meta:
        proxy = True
