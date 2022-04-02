from flask import Flask
from flask_restful  import Api
from demo import DemoAPI
from field import FieldAPI
from operation import OperationAPI
from field_operation import FieldOperationAPI
from operation_date import OperationDateAPI

# using csv files to keep information for now. No time to create te database

app = Flask(__name__)
api = Api(app)

api.add_resource(DemoAPI, '/')
api.add_resource(FieldAPI, '/field')
api.add_resource(OperationAPI, '/operation')
api.add_resource(FieldOperationAPI, '/field_operation')
api.add_resource(OperationDateAPI, '/operation_date')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)