import yaml
import requests
from collections.abc import MutableMapping
from contextlib import suppress

def delete_key_from_dict(dictionary, key):
    with suppress(KeyError):
        del dictionary[key]
    for value in dictionary.values():
        if isinstance(value, MutableMapping):
            delete_key_from_dict(value, key)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, MutableMapping):
                    delete_key_from_dict(item, key)

def print_yaml(dict):
    delete_key_from_dict(dict, "id")
    print(yaml.dump(dict, Dumper=MyDumper, default_flow_style=False))

def has(dict, key):
    return key in dict and dict[key] is not None and dict[key] != "" and dict[key] != [] and dict[key] != {}

def post_request(url, payload, is_dict = True):
    headers = {
        "Content-Type": "application/json"
    }
    if is_dict:
        response = requests.post(url, headers=headers, json=payload)
    else:
        response = requests.post(url, headers=headers, data=payload)

    print(response.json())

class MyDumper(yaml.Dumper):

    def increase_indent(self, flow=False, indentless=False):
        return super(MyDumper, self).increase_indent(flow, False)
