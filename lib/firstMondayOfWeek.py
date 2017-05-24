# -*- coding: utf-8 -*- 
#!/usr/bin/python
from datetime import date
from datetime import datetime
import string

firstMondayOfWeekPath = r'C:\uiPath\var\startDate.var'
firstMondayOfWeek = str(datetime.today().month)+"/"+str(datetime.today().day-datetime.today().weekday())+"/"+str(datetime.today().year) + " "
with open(firstMondayOfWeekPath,'w') as outputFile:
    outputFile.write(firstMondayOfWeek)