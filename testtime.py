import time

print(time.asctime())

now = time.gmtime()
prn_now = str("{}-{}-{} {:2}:{:2}:{:2}GMT,".format(now[0],now[1],now[2],now[3],now[4],now[5],now[6]))
print(prn_now)