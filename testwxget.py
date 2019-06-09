""" This is a file to test proper input and output to a file."""
import time

for n in range(1, 20):
    with open('testfileB.txt', 'a') as wf:
        time.sleep(0.5)
        wf.writelines("loop# {} \n".format(n))
        print("loop# {} \n".format(n))

