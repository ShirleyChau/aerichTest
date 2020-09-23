from tortoise import Model, fields
import datetime


class BaseModel(Model):
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        abstract = True


class User(BaseModel):
    username = fields.CharField(max_length=20, unique=True)
    password = fields.CharField(max_length=200)
    last_login = fields.DatetimeField(description="Last Login", default=datetime.datetime.now)
    is_active = fields.BooleanField(default=True, description="Is Active")
    is_superuser = fields.BooleanField(default=False, description="Is SuperUser")
    avatar = fields.CharField(max_length=200, default="")
    intro = fields.TextField(default="")


class Category(BaseModel):
    slug = fields.CharField(max_length=200)
    name = fields.CharField(max_length=200)
    user = fields.ForeignKeyField("models.User", description="User")


class Product(BaseModel):
    categories = fields.ManyToManyField("models.Category")
    name = fields.CharField(max_length=50)
    view_num = fields.IntField(description="View Num")
    sort = fields.IntField()
    is_reviewed = fields.BooleanField(description="Is Reviewed")
    image = fields.CharField(max_length=200)
    body = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)


class Config(BaseModel):
    label = fields.CharField(max_length=200)
    key = fields.CharField(max_length=20)
    value = fields.JSONField()
