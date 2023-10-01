from flask_restful import Api
from .RequestHandler import CropRequestHandler

api = Api()

api.add_resource(CropRequestHandler, '/test-api')
