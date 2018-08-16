from flask import jsonify, request
from app.api import api, ns
from flask_restplus import Resource, fields
from app.models.users import User, UserSchema, db


user_fields = api.model('User', {
    'name': fields.String,
    'email': fields.String
})

user_schema = UserSchema(many=True)


@ns.route('/user')
class UserListAPI(Resource):
    def get(self):
        queryset = User.query.all()
        queryset = user_schema.dump(queryset).data

        return jsonify({
            'data': queryset,
            'message': 'data have been successfully fetched',
            'error': False
        })

    @api.doc(body=user_fields)
    def post(self):
        data = request.get_json(force=True)
        if data:
            user = User()
            user.name = data['name']
            user.email = data['email']
            db.session.add(user)
            db.session.commit()

        return jsonify ({
            'data': [
                user.__serialize__()
            ],
            'message': 'data have been successfully saved',
            'error': False 
        })


@ns.route('/user/<int:id>')
class UserAPI(Resource):
    def get(self, id):
        user = User.query.get(id)
        if user:
            return jsonify({
                'data': [
                    user.__serialize__()
                ],
                'message': 'successfully!',
                'error': False
            })

        return jsonify({
            'data': [],
            'message': 'data not found',
            'error': False
        })

    @api.doc(body=user_fields)
    def put(self, id):
        data = request.get_json(force=True)
        user = User.query.get(id)
        user.name = data['name']
        user.email = data['email']
        db.session.add(user)
        db.session.commit()

        return jsonify({
            'data': [
                user.__serialize__()
            ],
            'message': 'successfully updated',
            'error': False
        })

    def delete(self, id):
        user = User.query.get(id)
        db.session.delete(user)
        db.session.commit()

        return jsonify({
            'data': [
                user.__serialize__()
            ],
            'message': 'successfully deleted',
            'error': False
        })