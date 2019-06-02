# This is the main file. 1 Jun 2019 - Mike Freimuth

# 1. Initialization
# 2. Open the output file, echo to terminal
# 3. Begin the call loop A. Call API; B. Process Data; C. Write Data to file
# 4. Once called, reset the timer regardless of success.
# 5. Write output to the CSV file, echo to terminal
# 6. End the loop on exit code 0

from wpconfigs import *
import time
from threading import Thread
import sys

import urllib.request
import json
from wpconfigs import *

def response(url):
    with urllib.request.urlopen(url) as response:
        return response.read()


# wxdata = json.loads(response(URL))



# resp = response(URL)
# wxdata = json.loads(resp)

def openfile():
    pass


def waitloop():
    """This loop delays for a set # of seconds between API calls."""
    for n in range(RECHECK_INTERVAL, 0, -1):
        time.sleep(5)
        print("Next call in {} minutes.".format(n))
    return


def getwxinfo():
    """This function will make the API call and handle parsing the JSON data
    and writing it to the file"""
    print("Sim calling API")
    return


#################  MAIN LOOP  ##################################

if __name__ == '__main__':
    ctr = 0  # Loop counter for number of WX data calls.
    #  TODO Add the open and close csv file code in this main loop structure
    while True:
        try:
            with open(OUTPUT_FILE, 'w+') as wf:
                ctr += 1
                print("Making API call #{}".format(ctr))
                wxdata = json.loads(response(URL))
                wrtline = "API call #{}, ".format(ctr) + str(wxdata) + "\n"
                #print(wf.closed())
                print(wrtline)
                wf.write(wrtline)
                waitloop()
        except KeyboardInterrupt:
            print("This is the exit path")
            sys.exit(0)
