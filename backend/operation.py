import pandas as pd
from flask_restful  import Resource, reqparse

class OperationAPI(Resource):

    def get(self):
        df = pd.read_csv('operation.csv')
        payload = []
        for index, row in df.iterrows():
            payload.append({
                'id': index,
                'operation_name': row['name']
            })
        
        return payload

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        args = parser.parse_args()

        file_name = 'operation.csv'
        new_operation = args['name']
        df = pd.read_csv(file_name)
        df = df.append({'name': new_operation}, ignore_index=True)
        df.to_csv(file_name, index=False)

        return {
            'message': f'{new_operation} is added into the database.'
        }

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', required=True)
        parser.add_argument('name', required=True)
        args = parser.parse_args()

        file_name = 'operation.csv'
        id = int(args['id'])
        new_name = args['name']
        df = pd.read_csv(file_name)
        df.loc[id]['name'] = new_name
        df.to_csv(file_name, index=False)

        return {
            'message': f'Changing name of operation id {id} to {new_name}.'
        }

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', required=True)
        args = parser.parse_args()

        file_name = 'operation.csv'
        id = int(args['id'])
        df = pd.read_csv(file_name)
        df = df.drop([id])
        df.to_csv(file_name, index=False)

        return {
            'message': f'Delete operation id {id}.'
        }
    