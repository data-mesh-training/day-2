from catalog_connection import register_dp
from utils import has
from time import sleep

def register_dp_in_catalog(dp_spec_dict, use_alt_service = False):
    print("Checking global policies..."); sleep(1)
    if check_for_basics(dp_spec_dict):
        print("Checks succeeded, publishing data product to catalog..."); sleep(0.5)
        register_dp(dp_spec_dict, use_alt_service)
        print("Data product registered successfully!")

def create_dp(dp_spec_dict, use_alt_service = False):
    print("Checking global policies..."); sleep(1)
    if check_full(dp_spec_dict):
        print("Checks succeeded, initializing infrastructure..."); sleep(0.5)
        print("Creating GitHub repository..."); sleep(1)
        print("Creating Airflow instance..."); sleep(1)
        print("Creating Spark cluster..."); sleep(1)
        print("Creating Kibana dashboard..."); sleep(0.5)
        print("Granting access roles to team members..."); sleep(0.5)
        print("Publishing data product to catalog..."); sleep(0.5)
        register_dp(dp_spec_dict, use_alt_service)
        print("Data product created successfully!")

def check_for_basics(dp_spec_dict):
    if not has(dp_spec_dict, "data_product_name"):
        print("Please provide a name for your data product.")
        return False
    if not has(dp_spec_dict, "description"):
        print("Please provide a description for your data product.")
        return False
    if not has(dp_spec_dict, "owner"):
        print("Please specify who owns your data product.")
        return False
    if not has(dp_spec_dict["owner"], "team"):
        print("Please name an owning team for your data product.")
        return False
    if not has(dp_spec_dict, "schema"):
        print("Please specify a schema for your data product.")
        return False
    if not has(dp_spec_dict["schema"][0], "name"):
        print("Please specify a name for each column.")
        return False
    if not has(dp_spec_dict["schema"][0], "type"):
        print("Please specify a type for each column.")
        return False

    return True

def check_full(dp_spec_dict):
    if not check_for_basics(dp_spec_dict):
        return False
    if not has(dp_spec_dict, "stakeholders"):
        print("Please specify the stakeholders of your data product.")
        return False
    if not has(dp_spec_dict["stakeholders"][0], "team"):
        print("Please name at least one stakeholder team.")
        return False
    if not has(dp_spec_dict, "sensitivity_tags"):
        print("Please specify the sensitivity of the data you are serving.")
        return False
    if not has(dp_spec_dict["sensitivity_tags"][0], "column_name"):
        print("Please specify each column containing sensitive data.")
        return False
    if not has(dp_spec_dict["sensitivity_tags"][0], "tag"):
        print("Please specify the kind of sensitivity for each sensitive column.")
        return False
    if not has(dp_spec_dict, "service_level_objectives"):
        print("Please specify at least one SLO for the data you are serving.")
        return False
    if not has(dp_spec_dict["service_level_objectives"][0], "type"):
        print("Please specify the kind of SLO.")
        return False
    if not has(dp_spec_dict["service_level_objectives"][0], "expression"):
        print("Please specify how the SLO can be expressed in an automatable form.")
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
        "description": "dataset description abc",
        "schema": [
        {
            "name": "order_id",
            "type": "string"
        }
        ]}, False)
