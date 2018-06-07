from __future__ import division, print_function

import json
import unittest

from coup_challenge_app.flask_util import create_flask
from coup_challenge_app.endpoints import v0


class TestFleetManagement(unittest.TestCase):
    def setUp(self):
        self.flask = create_flask("Test")
        self.flask.register_blueprint(v0.blueprint)
        self._client = self.flask.test_client()

    def _open_with_json(self, url, method, json_data=None, **kwargs):
        if json_data is not None:
            if 'data' in kwargs or 'content_type' in kwargs:
                raise ValueError()
            kwargs['data'] = json.dumps(json_data)
            kwargs['content_type'] = 'application/json'

        return self._client.open(url, method=method, **kwargs)

    def post(self, url, **kwargs):
        return self._open_with_json(url, method='POST', **kwargs)

    def assertStatusCode(self, status_code, response):
        self.assertEquals(status_code, response.status_code)

    def assertApplicationJson(self, response):
        content_type = response.headers.get('Content-Type')
        self.assertEquals('application/json', content_type, "Content type is different")

    def testFleetManagement(self):
        url = '/v0/fleet-management'
        response = self.post(
            url,
            json_data=dict(
                P=5,
                C=12,
                scooters=[15, 10]
            )
        )

        self.assertStatusCode(200, response)
        self.assertApplicationJson(response)

        payload = json.loads(response.data)
        self.assertEqual(payload['fleet_engineers'], 3)

    def testInvalidInput(self):
        url = '/v0/fleet-management'
        response = self.post(
            url,
            json_data=dict(
                P=2000,
                C=12,
                scooters=[15, 10]
            )
        )

        self.assertStatusCode(400, response)
        self.assertApplicationJson(response)
        payload = json.loads(response.data)
        self.assertEqual(payload['message'], 'Input payload validation failed')
        self.assertEqual(payload['errors']['P'], '2000 is greater than the maximum of 1000')