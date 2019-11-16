import urllib2
import json
import requests
request = urllib2.Request("https://api.holtonksweather.com/v1/forecast/daily", headers={"x-api-key" : "<API_KEY>"})
json_string = urllib2.urlopen(request).read()
parsed_json = json.loads(json_string)
high = str(parsed_json[0]['high'])
low =  str(parsed_json[0]['low'])
pop = str(parsed_json[0]['rain'])
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
