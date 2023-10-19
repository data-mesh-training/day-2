import yaml
import requests

def print_yaml(dict):
    print(yaml.dump(dict))

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

