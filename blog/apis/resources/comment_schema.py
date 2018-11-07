from blog.models import Comment
from blog.extensions import ma

class CommentSchema(ma.ModelSchema):
    class Meta:
        model = Comment