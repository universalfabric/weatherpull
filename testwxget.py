# this is a test file to get the code right for getting the wx data.
# once pulled, it will simply be displayed to the screen.

import urllib.request
import json

url = 'http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=b169533341072045445577086b3041fd'

def response(url):
    with urllib.request.urlopen(url) as response:
        return response.read()

res = response(url)
wxdata = json.loads(res)
print(type(wxdata))
print(wxdata['main'])
print(type(wxdata['main']))
print(wxdata['main']['temp'])
print(type(wxdata['main']['temp']))
