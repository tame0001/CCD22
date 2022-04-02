import pandas as pd
from flask_restful  import Resource, reqparse

class FieldOperationAPI(Resource):

    def get(self):
        field = pd.read_csv('field.csv')
        operation = pd.read_csv('operation.csv')
        field_operation = pd.read_csv('field_operation.csv')
        payload = []
        print(field)
        for index, row in field_operation.iterrows():
            payload.append({
                'field': field.loc[row['field']]['name'],
                'address': field.loc[row['field']]['address'],
                'area': str(field.loc[row['field']]['area']),
                'operation': operation.loc[row['operation']]['name'],
                'time': row['time'],
                'detail': row['detail']
            })
        
        return payload

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('field_id', required=True)
        parser.add_argument('operation_id', required=True)
        parser.add_argument('time', required=True)
        parser.add_argument('detail')
        args = parser.parse_args()

        file_name = 'field_operation.csv'
        operation = args['operation_id']
        field = args['field_id']
        time = args['time']
        df = pd.read_csv(file_name)
        df = df.append({
            'field': field, 
            'operation': operation,
            'time': time,
            'detail': args['detail'] if args['detail'] else ''
            }, ignore_index=True)
        df.to_csv(file_name, index=False)

        return {
            'message': f'Done!'
        }
