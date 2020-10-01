import boto3
import json

table_name = 'movies'
primary_key = 'movie_uuid'

db = boto3.resource('dynamodb')
table = db.Table(table_name)


def handler(event, context):
    movie_uuid = event['queryStringParameters']['movie_uuid']

    response = table.delete_item(
        Key={
            primary_key: movie_uuid
        }
    )

    return {
        "statusCode": response['ResponseMetadata']['HTTPStatusCode'],
        "body": json.dumps(response)
    }
