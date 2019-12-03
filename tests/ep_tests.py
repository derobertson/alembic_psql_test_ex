from tests.base import BaseClass


class MainTests(BaseClass):
    def test_response(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data.decode('utf8'), 'count: 1')
