import requests
from datetime import datetime, timedelta

url_template = "https://simurg.space/gen_file?data=obs&date={date}"

current = datetime.now()
