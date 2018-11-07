from flask import Blueprint
from flask_restful import Api


from blog.apis.resources import PostResource, PostManage

blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(blueprint)

api.add_resource(PostManage, '/posts')
api.add_resource(PostResource, '/posts/<string:post_id>')