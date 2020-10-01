import boto3
import json
import decimal

table_name = 'movies'
primary_key = 'movie_uuid'

db = boto3.resource('dynamodb')
table = db.Table(table_name)


def handler(event, context):
    movie_uuid = event['queryStringParameters']['movie_uuid']

    response = table.get_item(
        Key={
            primary_key: movie_uuid
        }
    )

    return {
        "statusCode": response['ResponseMetadata']['HTTPStatusCode'],
        "body": json.dumps(response['Item'], cls=DecimalEncoder)
    }


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)
