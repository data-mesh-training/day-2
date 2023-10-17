import catalog_connection as catalog

def create_dp(dp_spec):
    catalog.register_dp(dp_spec)

if __name__ == '__main__':
    create_dp("order_positions")
