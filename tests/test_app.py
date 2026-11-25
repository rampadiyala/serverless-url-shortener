import json, os, sys, unittest
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import app

class Fake:
    data = {}
    def put_item(self, Item, **kw): self.data[Item['code']] = Item
    def get_item(self, Key): return {'Item': self.data[Key['code']]} if Key['code'] in self.data else {}

def event(method, body=None, code=None):
    return {'requestContext': {'http': {'method': method}}, 'body': body, 'pathParameters': {'code': code} if code else None}

class T(unittest.TestCase):
    def setUp(self): app.table = Fake()
    def test_create_and_redirect(self):
        r = app.handler(event('POST', json.dumps({'url': 'https://example.com'})), None)
        r2 = app.handler(event('GET', code=json.loads(r['body'])['code']), None)
        self.assertEqual((r['statusCode'], r2['statusCode'], r2['headers']['Location']), (201, 302, 'https://example.com'))
    def test_bad_input(self): self.assertEqual(app.handler(event('POST', 'x'), None)['statusCode'], 400)
    def test_missing(self): self.assertEqual(app.handler(event('GET', code='no'), None)['statusCode'], 404)
if __name__ == '__main__': unittest.main()
