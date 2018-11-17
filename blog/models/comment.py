import uuid
from blog.extensions import db
from sqlalchemy.sql import func
class Comment(db.Model):
    """Basic comment model
    """

    id = db.Column(db.String, default=lambda: str(uuid.uuid4()), primary_key=True)
    content = db.Column(db.Text, nullable=False)
    time_created = db.Column(db.DateTime(timezone=True), server_default=func.now())
    time_updated = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    post_id = db.Column(db.String, db.ForeignKey('post.id'))

    def __init__(self, **kwargs):
        super(Comment, self).__init__(**kwargs)

    def __repr__(self):
        return "<Comment %s>" % self.contents
