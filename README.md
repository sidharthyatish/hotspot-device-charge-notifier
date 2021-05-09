# hotspot-device-charge-notifier

## What is this
A tiny script to notify upon battery low and battery charged state of Airtel hotspot device. Works with Jio as well

## Supported OS
Currently Mac os. Can be extended easily for others as well

## Setup
- Install `virtualenv` using `pip install virtualenv`
- `virtualenv venv && source ./venv/bin/activate`
- `pip install -r requirements.txt`
- Run `python main.py` or setup crontab (in mac) `*/30 * * * * cd ~/study/wifi-charge-notifier && source ./venv/bin/activate && python main.py >> notifier.log
`
