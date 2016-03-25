import datetime
from astral import Astral
import requests
city_name = 'Topeka'
a = Astral()
a.solar_depression = 'civil'
city = a[city_name]

sun = city.sun()

sunrise = sun['sunrise']
sunset = sun['sunset']
moon_phase = city.moon_phase()

if moon_phase == 0:
	moon_phasestr = "New Moon"
elif moon_phase >= 1 and moon_phase < 7:
	moon_phasestr = "Waxing Crescent"
elif moon_phase == 7:
	moon_phasestr = "First Quarter"
elif moon_phase >=8 and moon_phase < 14:
	moon_phasestr = "Waxing Gibbous"
elif moon_phase == 14:
	moon_phasestr = "Full"
elif moon_phase > 14 and moon_phase <21:
	moon_phasestr = "Waning Gibbous"
elif moon_phase == 21:
	moon_phasestr = "Third Quarter"
elif moon_phase > 21:
	moon_phasestr = "Waning Crescent"


sunrise = sunrise.strftime("%I:%M %p")
sunset = sunset.strftime("%I:%M %p")



sunriseurl = "http://localhost:3030/widgets/sunrise"

sunrisetext='{ "auth_token": "YOUR_AUTH_TOKEN", "value": "' + sunrise + '" }'


sunseturl = "http://localhost:3030/widgets/sunset"

sunsettext='{ "auth_token": "YOUR_AUTH_TOKEN", "value": "' + sunset + '" }'

moonurl = "http://localhost:3030/widgets/moonphase"

moontext='{ "auth_token": "YOUR_AUTH_TOKEN", "value": "' + moon_phasestr + '" }'


result=requests.post(sunseturl, data = sunsettext)


result=requests.post(sunriseurl, data = sunrisetext)
result=requests.post(moonurl, data = moontext)
