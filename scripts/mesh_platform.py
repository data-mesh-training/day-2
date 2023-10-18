from catalog_connection import register_dp
from time import sleep

def create_dp(dp_spec_dict, use_alt_service = False):
    print("Checking global policies..."); sleep(1)
    if check_for_basics(dp_spec_dict):
        print("Checks succeeded, initializing infrastructure..."); sleep(0.5)
        print("Creating GitHub repository..."); sleep(1)
        print("Creating Airflow instance..."); sleep(1)
        print("Creating Spark cluster..."); sleep(1)
        print("Creating Kibana dashboard..."); sleep(0.5)
        print("Granting access roles to team members..."); sleep(0.5)
        print("Publishing data product to catalog..."); sleep(0.5)
        register_dp(dp_spec_dict, use_alt_service)
        print("Data product created successfully!")

def has(dict, key):
    return key in dict and dict[key] is not None and dict[key] != ""

def check_for_basics(dp_spec_dict):
    if not has(dp_spec_dict, "data_product_name"):
        print("Please provide a name for your data product.")
        return False
    if not has(dp_spec_dict, "description"):
        print("Please provide a description for your data product.")
        return False
    if not has(dp_spec_dict, "owner"):
        print("Please provide an owner for your data product.")
        return False

    return True

if __name__ == '__main__':
    create_dp({
        "data_product_name": "sales_order",
        "owner": {
            "team": "team-x",
            "domain": "domain-z"
        },
        "stakeholders": [
            { "team": "team-y"}
        ],
        "description": "dataset description abc"
    }, False)
