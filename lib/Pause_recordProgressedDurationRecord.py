# -*- coding: utf-8 -*- 
#!/usr/bin/python
import string
from datetime import date
from datetime import datetime, timedelta

print "#######################################################"
print "# Record Progressed Record; After Pausing an activity #"
print "#######################################################"



activityProgressedDurationPath = r'C:\uiPath\var\activityProgressedDuration.record'
activityListFileBeautifiedPath = r'C:\uiPath\var\activityListValueBeautified.var'
inProgressActivityPath = r'C:\uiPath\var\inProgressActivity.var'


with open(inProgressActivityPath) as inProgressActivityFile:
    inProgressActivity = inProgressActivityFile.read()

pausedActivity = inProgressActivity

# log
print str(datetime.now()) + " pausedActivity : \n" + pausedActivity + "\n"

####################################################################
############### parse startTimeStamp.record ########################
####################################################################

print "###############################"
print "# parse startTimeStamp.record #"
print "###############################"

startTimeStampPath = r'C:\uiPath\var\startTimeStamp.record'
with open(startTimeStampPath) as startTimeStampFile:
    startTimeStamp = startTimeStampFile.read()
startTimeRecordLatest = str()

startTimeStampList = startTimeStamp.split('\n')

# remove blank in the end if existed 
if startTimeStampList[-1] == '':
    startTimeStampList.pop()

for line in startTimeStampList:
    if line.split()[1].strip() == pausedActivity:
        startTimeRecordLatest = line.split()[0].strip()

# log
print str(datetime.now()) + " startTimeRecordLatest : \n" + startTimeRecordLatest + "\n"

timeFormat = '%m/%d/%Y-%H:%M'
print startTimeRecordLatest
activityLastStartedDatetime = datetime.strptime(startTimeRecordLatest,timeFormat)

#####################################################################


activityProgressedDuration = datetime.now() - activityLastStartedDatetime

# log
print str(datetime.now()) + " activityProgressedDuration :" 
print activityProgressedDuration


# remove after .
activityProgressedDurationString = str(activityProgressedDuration).split(".")[0] if "." in str(activityProgressedDuration) else str(activityProgressedDuration)


# format as D-h:m:s
activityProgressedDurationStringList = activityProgressedDurationString.replace("days","day").split("day, ")
activityProgressedDurationString = "0-" + activityProgressedDurationString if "day" not in activityProgressedDurationString else activityProgressedDurationStringList[0].strip() + "-" + activityProgressedDurationStringList[1]

recordLine = pausedActivity + "\t" + activityProgressedDurationString + "\n"
# append record list here
with open(activityProgressedDurationPath,'a') as activityProgressedDurationFile:
    activityProgressedDurationFile.write(recordLine)

# log
print str(datetime.now()) + " activityProgressedDuration recordLine : \n" + recordLine + "\n"


