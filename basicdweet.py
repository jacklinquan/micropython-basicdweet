"""A python module for very basic APIs of the free dweet service.

- Author: Quan Lin
- License: MIT
"""

__version__ = "0.1.0"
__all__ = ["BasicDweetError", "dweet_for", "get_latest_dweet_for", "get_dweets_for"]

import json

try:
    import urequests as requests
except ImportError:
    import requests

BASE_URL = "https://dweet.io"


class BasicDweetError(Exception):
    pass


def _request(method, url, **kwargs):
    url = BASE_URL + url

    request_func = getattr(requests, method)
    response = request_func(url, **kwargs)
    if not (200 <= response.status_code < 300):
        raise BasicDweetError(f"HTTP {response.status_code} response")
    response_json = response.json()
    if response_json["this"] == "failed":
        raise BasicDweetError(response_json["because"])
    return response_json["with"]


def dweet_for(thing_name, payload):
    data = json.dumps(payload)
    headers = {"Content-type": "application/json"}
    return _request(
        "post",
        f"/dweet/for/{thing_name}",
        data=data,
        headers=headers,
    )


def get_latest_dweet_for(thing_name):
    return _request("get", f"/get/latest/dweet/for/{thing_name}")


def get_dweets_for(thing_name):
    return _request("get", f"/get/dweets/for/{thing_name}")
