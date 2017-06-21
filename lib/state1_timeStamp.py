# -*- coding: utf-8 -*- 
#!/usr/bin/python
import string
from datetime import date
from datetime import datetime, timedelta
import os

print "#####################################################"
print "# Record Complete time                      STATE:1 #"
print "#####################################################"

startTimeStampPath = r'C:\uiPath\var\startTimeStamp.record'
activityListFileBeautifiedPath = r'C:\uiPath\var\activityListValueBeautified.var'
completeScheduleRatePath = r'C:\uiPath\var\completeScheduleRate.var'
activityCompletePath = r'C:\uiPath\var\activityCompleteDuration.record'
inProgressActivityPath = r'C:\uiPath\var\inProgressActivity.var'

activityIdToComplete = str()

with open(inProgressActivityPath) as inProgressActivityFile:
    inProgressActivity= inProgressActivityFile.read().strip()

activityIdToComplete = inProgressActivity

# log
print str(datetime.now()) + " activityIdToComplete : \n" + activityIdToComplete + "\n"


activityProgressedDurationPath = r'C:\uiPath\var\activityProgressedDuration.record'
################################################################################
if os.path.isfile(activityProgressedDurationPath):
    print "################################################################"
    print "# Parsing activityProgressedDuration for " + activityIdToComplete+" #"
    print "################################################################"
    activityProgressedDurationList = list()
    with open(activityProgressedDurationPath) as activityProgressedDurationListFile:
        activityProgressedDurationListString= activityProgressedDurationListFile.read()
    activityProgressedDurationList = activityProgressedDurationListString.strip().split("\n")
    sumActivityProgressedDuration = timedelta()
    lineTimedelta = ""
    DAY = 0
    Hour = 1
    Minute = 2
    Second = 3
    for line in activityProgressedDurationList:
        if line.split("\t")[0] == activityIdToComplete:
            lineTimedelta = line.split("\t")[1]
            timedeltaList = lineTimedelta.replace("-",":").split(":")
            sumActivityProgressedDuration = sumActivityProgressedDuration + timedelta(days=int(timedeltaList[DAY]),hours=int(timedeltaList[Hour]),minutes=int(timedeltaList[Minute]),seconds=int(timedeltaList[Second]))
    # log
    print str(datetime.now()) + " sumActivityProgressedDuration : \n" + str(sumActivityProgressedDuration) + "\n"
else:
    # log
    print str(datetime.now()) + r" C:\uiPath\var\activityProgressedDuration.record not exist: \n"
    sumActivityProgressedDuration = timedelta(minutes=0)
################################################################################
timeFormat = '%m/%d/%Y-%H:%M'
timeStamp = datetime.now().strftime(timeFormat)
# log
print str(datetime.now()) + " timeStamp : \n" + timeStamp + "\n"

recordLine = timeStamp + "\t" + activityIdToComplete + "\n"
# append record list here
with open(activityCompletePath,'a') as activityCompleteFile:
    activityCompleteFile.write(recordLine)
# log
print str(datetime.now()) + " recordLine : \n" + recordLine + "\n"
