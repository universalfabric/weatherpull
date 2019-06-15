# This is the main file. 1 Jun 2019 - Mike Freimuth

# 1. Initialization
# 2. Open the output file, echo to terminal
# 3. Begin the call loop A. Call API; B. Process Data; C. Write Data to file
# 4. Once called, reset the timer regardless of success.
# 5. Write output to the CSV file, echo to terminal
# 6. End the loop on exit code 0

import time
import urllib.request
import json
from wpconfigs import *

def response(url):
    with urllib.request.urlopen(url) as response:
        return response.read()

##################################

if __name__ == '__main__':
    for n in range (1, ITERATIONS):
        with open(OUTPUT_FILE, 'a') as wf:
            print("Making API call at {}".format(time.asctime()))
            try:
                wxdata = json.loads(response(URLCONST))
            except:
                wxdata = "Load failed."
            now = time.gmtime()
            prn_now = str("{}-{}-{} {:2}:{:2}:{:2}GMT,".format(now[0],
                                                               now[1],
                                                               now[2],
                                                               now[3],
                                                               now[4],
                                                               now[5],
                                                               now[6]))
            wrtline = prn_now + str(wxdata) + "\n"
            wf.writelines(wrtline)
            time.sleep(60 * RECHECK_INTERVAL) # Sleep time between checks