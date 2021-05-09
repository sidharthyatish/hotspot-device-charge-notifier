import requests
import calendar
import time
from bs4 import BeautifulSoup
import os
from datetime import datetime
def notify_dialog(title, text):
    os.system("""
              osascript -e 'tell app "System Events" to display dialog "{} : {}%" with icon caution'
              """.format(title,text))

def notify_notification(title, text):
    os.system("""
              osascript -e 'display notification "{}%" with title "{}" sound name "Submarine"'
              """.format(text,title))


gmt = time.gmtime()
ts=calendar.timegm(gmt)
headers = {
    'Connection': 'keep-alive',
    'Accept': '*/*',
    'DNT': '1',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36 OPR/75.0.3969.218',
    'Referer': 'http://192.168.1.1/index.m.htm',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
}

params = (
    ('_', str(ts)),
)

dateTimeObj = datetime.now()
try:

    response = requests.get('http://192.168.1.1/mark_title.w.xml', headers=headers, params=params, verify=False, timeout=5)
    soup = BeautifulSoup(response.text, 'html.parser')

    battery_level = int(soup.batt_p.text)


    if battery_level <=10:
        notify_notification("Modem battery is very low",str(battery_level))
        notify_dialog("Modem battery LOW",str(battery_level))
    elif battery_level <=15 or battery_level >=96:
        notify_notification("Modem battery",str(battery_level))

except (requests.ConnectionError, requests.Timeout) as e:
    battery_level=-1
    print("Unable to connect to modem..")

print(dateTimeObj,battery_level)
# notify_dialog("Modem battery",str(battery_level))