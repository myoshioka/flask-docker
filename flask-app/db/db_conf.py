import os
from dotenv import load_dotenv

# env
dotenv_path = os.path.join('./', '.env')
load_dotenv(dotenv_path)

DATABASES = {
    'default': 'pgsql',
    'pgsql': {
        'driver': 'pgsql',
        'host': os.environ.get('DB_HOST', 'app-db'),
        'database': os.environ.get('DB_DATABASE', 'database'),
        'user': os.environ.get('DB_USERNAME', 'postgres'),
        'password': os.environ.get('DB_PASSWORD', 'postgres'),
        'port': '5432',
        'prefix': ''
    }
}
