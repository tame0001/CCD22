from flask_restful  import Resource, reqparse

class DemoAPI(Resource):

    def get(self):
        print('Demo API works')

        return {
            'message': 'If you see this, you are fine'
        }