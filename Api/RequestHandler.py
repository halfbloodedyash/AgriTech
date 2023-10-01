from flask_restful import Resource
from flask import request
from .predict import classify_using_bytes
from .solution import solution

class CropRequestHandler(Resource):
    def get(self):
        return {'Hello': 'World'}
    
    def post(self):

        file = request.files.get('file')

        if file:
            raw_result = classify_using_bytes(file.read(), 'Api/models/model.h5', 224)
            print(f'raw result {raw_result}')
            result = solution.get(raw_result['idx'] + 1)
            result['score'] = raw_result['score']
            return result

        else:
            print("\n404 no file found\n")
