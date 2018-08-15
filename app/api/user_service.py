from app.api import api, ns
from flask_restplus import Resource


@ns.route('/user')
class UserAPI(Resource):
    def get(self):
        return {
            'user': 'user service api'
        }