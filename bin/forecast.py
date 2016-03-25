import urllib2
import json
import requests
f = urllib2.urlopen('http://api.wunderground.com/api/3e393e8246e7ad6c/forecast/q/KS/Holton.json')
json_string = f.read()
parsed_json = json.loads(json_string)
high = parsed_json['forecast']['simpleforecast']['forecastday'][0]['high']['fahrenheit']
low =  parsed_json['forecast']['simpleforecast']['forecastday'][0]['low']['fahrenheit']
pop = parsed_json['forecast']['simpleforecast']['forecastday'][0]['pop']
f.close()

high = high + " F"
low = low + " F"
pop = str(pop)

highurl = "http://localhost:3030/widgets/hightemp"

hightext='{ "auth_token": "YOUR_AUTH_TOKEN", "value": "' + high + '" }'

lowurl = "http://localhost:3030/widgets/lowtemp"

lowtext='{ "auth_token": "YOUR_AUTH_TOKEN", "value": "' + low + '" }'

popurl = "http://localhost:3030/widgets/pop"

poptext='{ "auth_token": "YOUR_AUTH_TOKEN", "value": "' + pop + '"}'

result=requests.post(popurl, data = poptext )



result=requests.post(lowurl, data = lowtext )



result=requests.post(highurl, data = hightext )


