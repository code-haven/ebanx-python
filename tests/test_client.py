import unittest
from ebanx import EbanxClient
from ebanx.settings import *
from ebanx.exceptions import *


class EbanxClientTest(unittest.TestCase):
    def test_default_endpoint(self):
        client = EbanxClient('integration_key', 'secret_key')
        self.assertEqual(client.integration_key, 'integration_key')
        self.assertEqual(client.secret_key, 'secret_key')
        self.assertEqual(client.endpoint, SANDBOX_ENDPOINT_URL)

    def test_wrong_default_endpont(self):
        client = EbanxClient('integration_key', 'secret_key')
        self.assertNotEqual(client.endpoint, PRODUCTION_ENDPOINT_URL)

    def test_prod_endpoint(self):
        client = EbanxClient('integration_key', 'secret_key', 'production')
        self.assertEqual(client.endpoint, PRODUCTION_ENDPOINT_URL)

if __name__ == '__main__':
    unittest.main()
