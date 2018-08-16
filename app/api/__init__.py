from flask_restplus import Api


api = Api(version='1.0', title='User Service', description='Simple user service code')
ns = api.namespace('v0.1', 'User service')