import json, os, secrets
from urllib.parse import urlparse

table = None
def get_table():
    global table
    if table is None:
        import boto3
        table = boto3.resource('dynamodb').Table(os.environ['TABLE'])
    return table

def reply(code, body=None, headers=None):
    return {'statusCode': code, 'headers': headers or {}, 'body': json.dumps(body or {})}

def handler(event, context):
    if event['requestContext']['http']['method'] == 'POST':
        try:
            url = json.loads(event.get('body') or '{}')['url']
            parts = urlparse(url)
            assert parts.scheme in ('http', 'https') and parts.netloc
        except Exception:
            return reply(400, {'error': 'Send a valid http or https url'})
        code = secrets.token_urlsafe(6)
        get_table().put_item(Item={'code': code, 'url': url}, ConditionExpression='attribute_not_exists(code)')
        return reply(201, {'code': code})
    code = (event.get('pathParameters') or {}).get('code', '')
    item = get_table().get_item(Key={'code': code}).get('Item') if code else None
    return reply(302, headers={'Location': item['url']}) if item else reply(404, {'error': 'Not found'})
