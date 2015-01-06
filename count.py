#!/usr/bin/python
import time;

count_to = 10

print 'Hello, I can count really high.  What do you want me to count to?'
count_to = int(raw_input())

for i in range(1, count_to+1):
    print "Hi, I can count to " + str(i)
    time.sleep(0.5)
