from shiprocket.api_client import ApiClient

class Authentication(object):

    def __init__(self, api_client = None, username: str, password: str):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.username = username
        self.password = password


    def get_token(self):
        data = {
            "email": self.username,
            "password": self.password
        }
        response = self.api_client.parse_request("/v1/external/auth/login", data)
        parsed_response = self.api_client.parse_response(response)
        return parsed_response["token"]
