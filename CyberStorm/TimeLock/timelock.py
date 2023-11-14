from sys import stdin
from datetime import datetime
from hashlib import md5
import pytz

#time1 = datetime.now(pytz.utc).replace(tzinfo=None)

#time to change for inplace system time
time1 = (datetime(2010,6,13,12,55,34).astimezone(pytz.utc)).replace(tzinfo=None)

#times for testing correct output should be ee93
#if you use this you need to comment out all the stdin and the varabiles below it
#time1 = (datetime(2013,5,6,7,43,25).astimezone(pytz.utc)).replace(tzinfo=None)
#time2 = datetime(1999, 12, 31,23,59,59).astimezone(pytz.utc).replace(tzinfo=None)

#takes a date from the standard input epoch.txt
for line in stdin:
	date = line.split()

YYYY = int(date[0])
MM = int(date[1])
DD = int(date[2])
HH = int(date[3])
mm = int(date[4])
SS = int(date [5])

time2 = (datetime(YYYY,MM,DD,HH,mm,SS).astimezone(pytz.utc)).replace(tzinfo=None)

#debug print
print(time1)
print(time2)

#take the difference between the 2 times and computese the extra time in a 60 second interval
diff = (time1 - time2).total_seconds()
extra = diff%60

#Debug outputs
print(f"epoch:      {diff}")
print(f"Extra time: {extra}")

#takes away the extra time
diff = str(int(diff - extra))
print(f"time diff:  {diff}")

#takes the md5 of the difference time then the md5 again
code = md5(diff.encode()).hexdigest()
code = md5(code.encode()).hexdigest()
print(f"md5:        {code}")

#this takes the md5 hash and extracts the first 2 letters and numbers
letter = ""
number = ""
for i in code:
	if i.isalpha():
		letter+=i
	if len(letter) > 1:
		break
		

for i in code[::-1]:
	if i.isdigit():
		number+=i
	if len(number) > 1:
		break

letter+=number
print(f"Code:       {letter}")

if len(code)%2 == 0:
	middleindex = (len(code)-1)//2
else:
	middleindex = (len(code)-1)/2

print(f"Middle Character: {code[middleindex]}")
