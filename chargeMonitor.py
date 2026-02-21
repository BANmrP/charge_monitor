import psutil
from win11toast import toast
import time

last_percent = 100

while True:
	time.sleep(60)

	battery = psutil.sensors_battery()
	percent = battery.percent

	if percent <= 10 and percent != last_percent:
		toast('Заряд 10%			')
		last_percent = percent

	elif percent <= 20 and percent != last_percent:
		toast('Заряд 20%			')
		last_percent = percent

	elif percent <= 30 and percent != last_percent:
		toast('Заряд 30%			')
		last_percent = percent

	elif percent > last_percent:	#charging test
		last_percent = 100