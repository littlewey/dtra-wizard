# -*- coding: utf-8 -*- 
#!/usr/bin/python
import string
from datetime import date
from datetime import datetime, timedelta

activityListFileBeautifiedPath = r'C:\uiPath\var\activityListValueBeautified.var'

activityDueTimeAdjustmentPath = r'C:\uiPath\var\log\activityDueTimeAdjustment.record'
activityDueTimeAdjustment = str()

with open(activityListFileBeautifiedPath) as activityListFile:
    activityListString= activityListFile.read()
activityList = activityListString.strip().split("\n")

inProgressActivityPath = r'C:\uiPath\var\inProgressActivity.var'

with open(inProgressActivityPath) as inProgressActivityFile:
    inProgressActivity = inProgressActivityFile.read().strip()

durationString = str()

completeScheduleRatePath = r'C:\uiPath\var\completeScheduleRate.var'

with open(completeScheduleRatePath) as completeScheduleRateFile:
    completeScheduleRateString = completeScheduleRateFile.read().strip()
completeScheduleRate = float(completeScheduleRateString)

for line in activityList:
    if inProgressActivity == line.split()[2]:
        durationString = line.split()[8]

# [debug] print durationString

# durationFormat = '%I:%M'

duration = timedelta(hours=int(durationString.split(":")[0]),minutes=int(durationString.split(":")[1])) 

if duration.total_seconds()*completeScheduleRate - inProgressedDuration.total_seconds() - (datetime.now()-startedTime).total_seconds():
	