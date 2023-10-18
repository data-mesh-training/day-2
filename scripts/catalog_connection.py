import requests
import yaml
import json
from utils import make_request

service_url = "https://data-product-catalog.onrender.com"
alt_service_url = "https://data-mesh-platform.onrender.com"

def register_dp(dp_spec_dict, use_alt_service = False):
    if use_alt_service:
        make_request(alt_service_url + "/register", dp_spec_dict)
    else:
        make_request(service_url + "/register", dp_spec_dict)

def register_dp_from_file(dp_spec_yaml_path, use_alt_service = False):
    with open(dp_spec_yaml_path, 'r') as dp_spec_yaml:
        dp_spec_dict = yaml.safe_load(dp_spec_yaml)
        register_dp(dp_spec_dict, use_alt_service)

if __name__ == '__main__':
    register_dp_from_file("dp_template.yml")
