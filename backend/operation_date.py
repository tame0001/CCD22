from time import time
import pandas as pd
from flask_restful  import Resource, reqparse

class OperationDateAPI(Resource):

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('start_date')
        parser.add_argument('end_date')
        args = parser.parse_args()
        start_date = args['start_date']
        end_date = args['end_date']
        field = pd.read_csv('field.csv')
        operation = pd.read_csv('operation.csv')
        field_operation = pd.read_csv('field_operation.csv')
        pd.to_datetime(field_operation['time'])
        field_operation['time'] = pd.to_datetime(field_operation['time'])
        field_operation = field_operation.set_index('time')
        sub_df = field_operation[start_date:end_date]
        payload = []
        for index, row in sub_df.iterrows():
            payload.append({
                'field': field.loc[row['field']]['name'],
                'operation': operation.loc[row['operation']]['name'],
                'time': index.date().isoformat(),
                'detail': row['detail']
            })
        
        return payload
