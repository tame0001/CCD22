import pandas as pd
from flask_restful  import Resource, reqparse

class FieldAPI(Resource):

    def get(self):
        df = pd.read_csv('field.csv')
        payload = []
        for index, row in df.iterrows():
            payload.append({
                'id': index,
                'field_name': row['name'],
                'address': row['address'],
                'area': str(row['area'])
            })
        
        return payload

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        args = parser.parse_args()

        file_name = 'field.csv'
        new_field = args['name']
        df = pd.read_csv(file_name)
        df = df.append({'name': new_field}, ignore_index=True)
        df.to_csv(file_name, index=False)

        return {
            'message': f'{new_field} is added into the database.'
        }

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', required=True)
        parser.add_argument('name', required=True)
        args = parser.parse_args()

        file_name = 'field.csv'
        id = int(args['id'])
        new_name = args['name']
        df = pd.read_csv(file_name)
        print()
        df.loc[id]['name'] = new_name
        print(df)
        df.to_csv(file_name, index=False)

        return {
            'message': f'Changing name of field id {id} to {new_name}.'
        }

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', required=True)
        args = parser.parse_args()

        file_name = 'field.csv'
        id = int(args['id'])
        df = pd.read_csv(file_name)
        df = df.drop([id])
        df.to_csv(file_name, index=False)

        return {
            'message': f'Delete field id {id}.'
        }
    