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
        print("response.text=========", self.response.text)
        return self

    def validate(self, key, except_value):
        value = self.response

        for _key in key.split('.'):
            print("_key========", _key)
            if isinstance(value, requests.Response):
                if _key == "json()":
                    value = self.response.json()
                else:
                    value = getattr(value, _key)

                print("response_value=========", value)
            elif isinstance(value, (requests.structures.CaseInsensitiveDict, dict)):
                print("structures_value========", value)
                value = value[_key]
        print("========", value)
        assert value == except_value
        return self
