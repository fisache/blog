from flask import request
from flask_restful import Resource

from blog.models import Post
from blog.extensions import db

from .post_schema import PostSchema

class PostResource(Resource):
    """Single object resource
    """
    def get(self, post_id):
        schema = PostSchema()
        post = Post.query.get_or_404(post_id)
        return {"post": schema.dump(post).data}

    def put(self, post_id):
        schema = PostSchema(partial=True)
        post = Post.query.get_or_404(post_id)
        post, errors = schema.load(request.json, instance=post)
        if errors:
            return errors, 422

        return {"msg": "post updated", "post": schema.dump(post).data}, 201

    def delete(self, post_id):
        post = Post.query.get_or_404(post_id)
        db.session.delete(post)
        db.session.commit()

        return {"msg": "post deleted"}, 204