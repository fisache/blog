from blog.models import Post
from blog.extensions import ma
from .comment import CommentSchema

class PostSchema(ma.ModelSchema):
    class Meta:
        model = Post
    comment = ma.Nested(CommentSchema)