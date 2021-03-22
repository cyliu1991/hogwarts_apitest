import requests
import requests.structures

session = requests.sessions.Session()


class BaseApi(object):
    url = ""
    method = ""
    params = ""
    data = ""
    json = {}
    headers = {}

    def set_params(self, **params):
        self.params = params
        return self

    def set_data(self, data):
        self.data = data
        return self

    def set_json(self, json_data):
        self.json = json_data
        return self

    def run(self):
        # proxies = {'http': '127.0.0.1:8888', 'https': '127.0.0.1:8888'}
        self.response = session.request(
            method=self.method,
            url=self.url,
            json=self.json,
            data=self.data,
            params=self.params,
            headers=self.headers,
            # proxies=proxies
        )
        print("response.text=========", self.response.text)
        return self

    def extract(self, field):
        value = self.response
        for _key in field.split('.'):
            print("_key========", _key)
            if isinstance(value, requests.Response):
                if _key in ["json()", "json"]:
                    value = self.response.json()
                else:
                    value = getattr(value, _key)

                print("response_value=========", value)
            elif isinstance(value, (requests.structures.CaseInsensitiveDict, dict)):
                print("structures_value========", value)
                value = value[_key]
        return value

    def validate(self, key, except_value):
        value = self.extract(key)
        assert value == except_value
        return self

    def get_response(self):
        return self.response
