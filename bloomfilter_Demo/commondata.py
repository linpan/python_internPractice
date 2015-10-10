#usr/bin/env python
#authour:linpan
#email:yidiyu0507s@163.com
#
'''
compare the common between A file and B file ,of course they are commonly super file whiout loaded memeory once.
pybloom is best functions
'''

__author__ = 'galaxy'
import time
from pybloomfilter import BloomFilter  # you need install this package
t1=time.time()
bf=BloomFilter(5000000000,0.01)

with open('/home/galaxy/Templates/Aip.txt') as f1:
    for ip in f1 :
        bf.add(ip)

count=0
with open('/home/galaxy/Templates/Bip.txt')as f2:
    for ip in f2:
        if ip in bf:
            print  ip
            count+=1
t2=time.time()-t1
print 'the amount is:', count
print 'the total time:',t2