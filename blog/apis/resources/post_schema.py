from blog.models import Post
from blog.extensions import ma

class PostSchema(ma.ModelSchema):
    class Meta:
        model = Post