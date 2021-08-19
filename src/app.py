import config
import os
from app_initializer import initialize_data

connex_app = config.connex_app
connex_app.add_api("swagger.yml", strict_validation=True)


if __name__ == '__main__':
    initialize_data()
    port = int(os.environ.get('PORT', 5000))
    connex_app.run(host='0.0.0.0', port=port,debug=True)
