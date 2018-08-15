from flask_restplus import Api


api = Api(version='1.0', title='user service', description='simple user service code')
ns = api.namespace('v0.1', 'user service')