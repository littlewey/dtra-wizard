# -*- coding: utf-8 -*- 
#!/usr/bin/python
import string
from datetime import date
from datetime import datetime, timedelta

print "################################"
print "# Select InProgressed to Pause #"
print "################################"

activityIdToPause = str()
activityProgressedDuration = str()

activityListFileBeautifiedPath = r'C:\uiPath\var\activityListValueBeautified.var'
inProgressActivityPath = r'C:\uiPath\var\inProgressActivity.var'



with open(activityListFileBeautifiedPath) as activityListFile:
    activityListString= activityListFile.read()
activityList = activityListString.strip().split("\n")


with open(inProgressActivityPath) as inProgressActivityFile:
    inProgressActivity= inProgressActivityFile.read()

activityIdToPause = inProgressActivity
# log
print str(datetime.now()) + " activityIdToPause = inProgressActivity : \n" + inProgressActivity + "\n"
