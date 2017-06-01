# -*- coding: utf-8 -*- 
#!/usr/bin/python
from datetime import date
from datetime import datetime
from datetime import timedelta 
import string

print "###########################"
print "# caculate current Monday #"
print "###########################"


firstMondayOfWeekPath = r'C:\uiPath\var\startDate.var'

timeFormat = '%m/%d/%Y'


firstMondayOfWeek = (datetime.today()-timedelta(days=(1 + datetime.today().weekday()-datetime.today().day))).strftime(timeFormat)
with open(firstMondayOfWeekPath,'w') as outputFile:
    outputFile.write(firstMondayOfWeek)


# log
print str(datetime.now()) + " firstMondayOfWeek.py firstMondayOfWeek : \n" + firstMondayOfWeek + "\n"