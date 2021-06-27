from app.models import User
from app.permissions import is_authenticated
from app.schemas import UserUpdateSchema


@is_authenticated(str)
def create_user(user_schema: UserUpdateSchema):
    user = User(
        name=user_schema.name,
        title=user_schema.title,
        address=user_schema.address,
        social_networks=user_schema.social_networks
    )
    user.save()
    return user


@is_authenticated(str)
def update_user(user_id, user_schema: UserUpdateSchema):
    user = User.objects(id=user_id).first()
    user.name = user_schema.name
    user.title = user_schema.title
    user.address = user_schema.address
    user.social_networks = user_schema.social_networks
    user.save()
    return user
