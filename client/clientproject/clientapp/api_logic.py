import requests
import os
import json

from clientapp.forms import ClientForm


def url():
    host = os.environ.get("TEST_SERVER", "127.0.0.1")
    port = os.environ.get("TEST_SERVER_PORT", "8001")
    return f"http://{host}:{port}"

def calculate(form: ClientForm) -> int:
    endpoint = "/"
    data = form.cleaned_data
    value1 = data["value1"]
    value2 = data["value2"]

    json_data = {"value1": value1, "value2": value2}
    json_object = json.dumps(json_data)

    response = requests.get(url() + endpoint, json=json_object)
    if response.status_code != 200:
        return ""
    return response.json().get("result", None)
