from time import strftime
from datetime import datetime

with open('C:\\Users\\Nandita\\Desktop\\finefoods\\files\\unixTime.txt') as f:
    lines = f.read().splitlines()
f = open('C:\\Users\\Nandita\\Desktop\\finefoods\\files\\dateTime.txt','w')    
for i in lines:
    f.write(datetime.fromtimestamp(int(i)).strftime('%Y-%m-%d'))
    f.write('\n')
f.close()
    
    
