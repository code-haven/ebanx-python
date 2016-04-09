from ebanx.settings import SANDBOX_ENDPOINT_URL, PRODUCTION_ENDPOINT_URL


class EbanxClient:
    """
    A wrapper that implements the GET/POST methods used throughout the lifecycle of a payment.
    """
    def __init__(self, integration_key, secret_key, environment='sandbox'):
        self.integration_key = integration_key
        self.secret_key = secret_key
        self.endpoint = self._get_endpoint(environment)

    def get(self, *args, **kwargs):
        pass

    def post(self, *args, **kwargs):
        pass

    def _get_endpoint(environment):
        if environment == 'sandbox':
            return SANDBOX_ENDPOINT_URL

        elif environment == 'production':
            return PRODUCTION_ENDPOINT_URL
