from flask import Blueprint, jsonify
from flask_restful import Api

from flask import request
from blog.extensions import db

from blog.apis.resources import PostResource, PostSchema

blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(blueprint)

api.add_resource(PostResource, '/posts/<string:post_id>')

@blueprint.route('/posts', methods=['POST'])
def post():
    schema = PostSchema()
    p, errors = schema.load(request.json)
    if errors:
        return errors, 422

    db.session.add(p)
    db.session.commit()
    return jsonify({"msg": "post created", "post": schema.dump(p).data}), 201

# TODO(inki.hwang) query string : title
# api.add_resource(PostList, '/posts')