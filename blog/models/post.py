import uuid
from blog.extensions import db
from sqlalchemy_utils.types import UUIDType

class Post(db.Model):
    """Basic post model
    """

    # TODO(inki.hwang) created date
    id = db.Column(UUIDType, primary_key=True, default=uuid.uuid4)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.Text, nullable=True)
    comments = db.relationship('Comment', backref='post', lazy=True, cascade='delete')

    def __init__(self, **kwargs):
        super(Post, self).__init__(**kwargs)

    def __repr__(self):
        return "<Post %s>" % self.title
