import requests


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
        actual_value = getattr(self.response, key)
        assert actual_value == except_value
        return self