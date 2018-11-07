from flask import request
from flask_restful import Resource

from blog.models import Post
from blog.extensions import db

from .post_schema import PostSchema

class PostManage(Resource):
    """get_all
    """
    def get(self):
        schema = PostSchema(many=True)
        title = request.args.get('title')
        if title:
            posts = Post.query.filter(Post.title.like('%' + title + '%'))
        else:
            posts = Post.query.all()
        return schema.dump(posts).data, 200

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

class PostResource(Resource):
    """Single object resource
    """
    def get(self, post_id):
        schema = PostSchema()
        post = Post.query.get_or_404(post_id)
        return schema.dump(post).data

    def put(self, post_id):
        schema = PostSchema(partial=True)
        post = Post.query.get_or_404(post_id)
        p, errors = schema.load(request.json, instance=post)
        if errors:
            return errors, 422
        db.session.add(p)
        db.session.commit()

        return schema.dump(p).data, 201

    def delete(self, post_id):
        post = Post.query.get_or_404(post_id)
        db.session.delete(post)
        db.session.commit()

        return {}, 204
