import uuid
from blog.extensions import db
from sqlalchemy_utils.types import UUIDType

class Comment(db.Model):
    """Basic comment model
    """

    # TODO(inki.hwang) created date
    id = db.Column(UUIDType, primary_key=True, default=uuid.uuid4)
    contents = db.Column(db.Text, nullable=False)
    post_id = db.Column(UUIDType, db.ForeignKey('post.id'))

    def __init__(self, **kwargs):
        super(Comment, self).__init__(**kwargs)

    def __repr__(self):
        return "<Comment %s>" % self.contents
