# These are the configuration constants for my Weather Pull code.
CITY = "CHICAGO"
OUTPUT_FILE = "wxoutput.csv"
RECHECK_INTERVAL = 9  # / 60 SECONDS = 10 MINUTES

WXKEY = "b169533341072045445577086b3041fd" # This is my API key for openweathermap.org

# This is an example of JSON data returned from a command line API call
TESTSTRING = '{"coord":{"lon":-87.62,"lat":41.88},"weather":[{"id":500,"main":"Rain",' \
             '"description":"light rain","icon":"10d"},{"id":211,"main":"Thunderstorm",' \
             '"description":"thunderstorm","icon":"11d"}],"base":"stations",' \
             '"main":{"temp":298.67,"pressure":1005,"humidity":61,"temp_min":291.48,' \
             '"temp_max":301.48},"visibility":16093,"wind":{"speed":1.5,"deg":120},' \
             '"rain":{"1h":0.25},"clouds":{"all":90},"dt":1559428062,"sys":{"type":1,' \
             '"id":4861,"message":0.0085,"country":"US","sunrise":1559384286,' \
             '"sunset":1559438330},"timezone":-18000,"id":4887398,"name":"Chicago"' \
             ',"cod":200}'
