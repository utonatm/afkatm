import os

API_KEY = os.getenv('API_KEY', 'your_API_KEY')

START = os.getenv('START', '2011-01-01')
END = os.getenv('END', '2019-09-01')
INTERVAL = os.getenv('INTERVAL', '1d')
ITERATE_EVER_DAYS = int(os.getenv('ITERATE_EVER_DAYS', '150'))
