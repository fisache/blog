from flask import request
from flask_restful import Resource

from blog.models import Comment, Post
from blog.extensions import db

from .comment_schema import CommentSchema

class CommentManage(Resource):
    """get_all
    """
    def get(self, post_id):
        schema = CommentSchema(many=True)
        content = request.args.get('content')
        post = Post.query.get_or_404(post_id)
        if content:
            comments = Comment.query.filter(Comment.post_id==post.id).filter(Comment.content.like('%' + content + '%'))
        else:
            comments = Comment.query.filter(Comment.post_id==post.id).all()
        return schema.dump(comments).data, 200

    """create
    """
    def post(self, post_id):
        schema = CommentSchema()
        request.json['post'] = post_id
        c, errors = schema.load(request.json, session=db.session)
        if errors:
            return errors, 422

        db.session.add(c)
        db.session.commit()

        return schema.dump(c).data, 201


class CommentResource(Resource):
    """Single object resource
    """
    def get(self, comment_id):
        schema = CommentSchema()
        comment = Comment.query.get_or_404(comment_id)
        return schema.dump(comment).data

    def put(self, comment_id):
        schema = CommentSchema(partial=True)
        comment = Comment.query.get_or_404(comment_id)
        c, errors = schema.load(request.json, instance=comment)
        if errors:
            return errors, 422
        db.session.add(c)
        db.session.commit()

        return schema.dump(c).data, 201

    def delete(self, comment_id):
        comment = Comment.query.get_or_404(comment_id)
        db.session.delete(comment)
        db.session.commit()

        return {}, 204
