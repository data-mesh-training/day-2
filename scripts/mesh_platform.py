from catalog_connection import register_dp

def create_dp(dp_spec):
    register_dp(dp_spec)

if __name__ == '__main__':
    create_dp("order_positions")