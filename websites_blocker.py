import time
from datetime import datetime as dt 

hosts_tmp = "hosts"
unix_hosts_path = "/etc/hosts"
win_hosts_path = r"C:\Window\System32\drivers\etc\hosts"
redirect = "127.0.0.1"

websites_list = [
    "www.facebook.com",
    "facebook.com"
    ]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day,8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,18):
        with open(unix_hosts_path, 'r+') as file:
            content = file.read()
            for website in websites_list:
                if website in content:
                    continue
                else:
                    file.write(redirect + "\t" + website + "\n")
    else:
        with open(unix_hosts_path, "r+") as file:
            content = file.readlines()
            file.seek(0)

            for line in content:
                if not any(website in line for website in websites_list):
                    file.write(line)
            file.truncate()
    time.sleep(5)