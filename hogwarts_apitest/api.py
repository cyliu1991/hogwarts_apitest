import requests
import requests.structures


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
        self.json_data = json_data
        return self

    def run(self):
        self.response = requests.request(
            method=self.method,
            url=self.url,
            json=self.json,
            data=self.data,
            headers=self.headers
        )
        print(self.response.text)
        return self

    def validate(self, key, except_value):
        value = self.response
        for _key in key.split('.'):
            if isinstance(value, requests.Response):
                value = getattr(self.response, key)
            elif isinstance(value, (requests.structures.CaseInsensitiveDict, dict)):
                value = value[_key]
        actual_value = getattr(self.response, key)
        assert actual_value == except_value
        return self