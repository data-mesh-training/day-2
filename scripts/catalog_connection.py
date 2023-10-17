import requests
import re
import yaml
import json

data = {
    "description": "test42",
}

def register_dp(dp_spec_dict):
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post('https://data-product-catalog.onrender.com/register', headers=headers, json=dp_spec_dict)

    print(response.json())


def register_dp_from_file(dp_spec_yaml_path):
    with open(dp_spec_yaml_path, 'r') as yaml_in:
        dp_spec_json = json.dumps(yaml.safe_load(yaml_in))

    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post('https://data-product-catalog.onrender.com/register', headers=headers, data=dp_spec_json)

    print(response.json())

if __name__ == '__main__':
    register_dp_from_file("dp_template.yml")
