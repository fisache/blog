import uuid
from blog.extensions import db
from sqlalchemy.sql import func
class Post(db.Model):
    """Basic post model
    """

    id = db.Column(db.String, default=lambda: str(uuid.uuid4()), primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.Text, nullable=True)
    time_created = db.Column(db.DateTime(timezone=True), server_default=func.now())
    time_updated = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    comments = db.relationship('Comment', backref='post', lazy=True, cascade='delete')

    def __init__(self, **kwargs):
        super(Post, self).__init__(**kwargs)

    def __repr__(self):
        return "<Post %s>" % self.title
