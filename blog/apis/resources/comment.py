from flask import request
from flask_restful import Resource

from blog.models import Comment
from blog.extensions import db

from .comment_schema import CommentSchema

class CommentManage(Resource):
    """get_all
    """
    def get(self):
        schema = CommentSchema(many=True)
        contents = request.args.get('contents')
        if contents:
            comments = Comment.quuery.with_
            comments = Comment.query.filter(Comment.contents.like('%' + contents + '%'))
        else:
            comments = Comment.query.all()
        return schema.dump(comments).data, 200

    """create
    """
    def post(self):
        schema = PostSchema()
        p, errors = schema.load(request.json)
        if errors:
            return errors, 422

        db.session.add(p)
        db.session.commit()
        return schema.dump(p).data, 201