import requests
from datetime import datetime, timedelta

url_template = "https://simurg.space/gen_file?data=obs&date={date}"

current = datetime.now()
while True:
    current = current - timedelta(days=1) 
    date_str = current.strftime("%Y-%m-%d")
    print(f"Current datetime is {current} and {date_str}")

    url = url_template.format(date=date_str)

    response = requests.get(url=url, stream=True)
    print(f"From url {url} got {response}")
if response.status_code == 200:
        print(f"Last avalibe data are for {current}")
        break
