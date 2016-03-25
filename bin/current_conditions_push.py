import xml.etree.ElementTree as ET
import requests
import urllib2
import time
from datetime import datetime
tree = ET.ElementTree(file=urllib2.urlopen('http://holtonksweather.com/data/wxrss.xml' ))
root = tree.getroot()


for node in root.iter():
	temperature = root.findtext('.//outsideTemp')
	dewpoint = root.findtext('.//dewpoint')
	rain = root.findtext('.//rain')
	humidity = root.findtext('.//humidity')
	windSpeed = root.findtext('.//windSpeed')
	windDir = root.findtext('.//windDir')
	obtime = root.findtext('.//obTime')
tempf = temperature + " F" 
dewf = dewpoint + " F"
rainin = rain + " Inches"
percent = "%"
humidityp = humidity
timeAdd = str(time.time())
windStr = windDir + " at " + windSpeed + " MPH" 
timeString = datetime.strptime(obtime, '%H:%M:%S')
updateTime = "Observed at " + timeString.strftime('%I:%M %p')



radarImage = "http://mesonet.agron.iastate.edu/GIS/radmap.php?layers%5b%5d=nexrad&layers%5b%5d=uscounties&bbox=-96.8,38.9,-94.46,39.8&title=Current%20NE%20Kansas%20Radar&width=740&height=680&d=" + timeAdd

rainurl = "http://localhost:3030/widgets/rain"

raintext = '{ "auth_token": "YOUR_AUTH_TOKEN", "value": "' +  rainin + '", "finished": "' + updateTime + '" }'

humurl = "http://localhost:3030/widgets/humidity"

humtext = '{ "auth_token": "YOUR_AUTH_TOKEN", "value": "' +  humidityp + '", "finished": "' + updateTime + '" }'

radarurl = "http://localhost:3030/widgets/picture"

radartext = '{ "auth_token": "YOUR_AUTH_TOKEN", "image": "' +  radarImage + '", "finished": "' + updateTime + '" }'

tempurl = "http://localhost:3030/widgets/temperature"

temptext='{ "auth_token": "YOUR_AUTH_TOKEN", "value": "' +  tempf + '", "finished": "' + updateTime + '" }'

dewurl = "http://localhost:3030/widgets/dewpoint"

dewtext='{ "auth_token": "YOUR_AUTH_TOKEN", "value": "' + dewf + '", "finished": "' + updateTime + '" }'



windurl = "http://localhost:3030/widgets/windspeed"

windtext='{ "auth_token": "YOUR_AUTH_TOKEN", "value": "' + windStr + '", "finished": "' + updateTime + '" }'

result=requests.post(tempurl, data = temptext )
result=requests.post(dewurl, data = dewtext)
result=requests.post(radarurl, data = radartext)
result=requests.post(rainurl, data = raintext)
result=requests.post(humurl, data = humtext)
result=requests.post(windurl, data = windtext)
