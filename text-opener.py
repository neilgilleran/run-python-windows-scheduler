# text-opener.py
import time
filename = 'text.txt'
file = open(filename,'w')
#file.read()

for i in range(0,10):
    print(i)
    time.sleep(i)

file.close()