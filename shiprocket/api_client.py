import logging
import timeit

import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

from shiprocket.exceptions import ShipRocketException

logger = logging.getLogger(__name__)

class ApiClient(object):

    def __init__(self, token = None):
        self.base_url = "https://apiv2.shiprocket.in"
        self.token = None

    def requests_retry_session(
            self,
            retries=3,
            backoff_factor=0.3,
            status_forcelist=(500, 502, 503, 504),
            session=None,
    ):
        session = session or SdLoggingSession()
        retry = Retry(
            total=retries,
            read=retries,
            connect=retries,
            backoff_factor=backoff_factor,
            status_forcelist=status_forcelist,
        )
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        return session

    def parse_request(self, path: str, data: dict, options={}):
        headers = {"Content-type": "application/json"}
        if self.token:
            options.update({"Authorization": f"Bearer #{self.token}"})

        data.update(options)
        # logger.info(f"Sending data for request {data}")
        payload = json.dumps(data)
        url = self.base_url + path
        return requests_retry_session().post(url, headers=headers, data=payload)

    def parse_response(self, response):

        self.check_response(response)

        response = response.text
        return json.loads(response)

    def check_response(self, response_data) -> Union[bool, Exception]:
        if response_data.status_code != 200:
            logger.error(f" Getting error while requesting  {response_data.content}")
            raise ShipRocketException(
                message=response_data.content, code=response_data.status_code
            )
        return True
