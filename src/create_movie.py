import boto3
import json
from decimal import Decimal
import uuid

table_name = 'movies'
primary_key = 'movie_uuid'

db = boto3.resource('dynamodb')
table = db.Table(table_name)


def handler(event, context):
    params = json.loads(event['body'])

    movie_uuid = uuid.uuid1().hex
    year = params['year']
    title = params['title']
    rank = params['rank']

    response = table.put_item(
        Item={
            primary_key: movie_uuid,
            'year': year,
            'title': title,
            'rank': Decimal(rank)
        }
    )

    return {
        "statusCode": response['ResponseMetadata']['HTTPStatusCode'],
        "body": json.dumps(response)
    }
