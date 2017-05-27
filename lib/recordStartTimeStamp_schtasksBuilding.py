# -*- coding: utf-8 -*- 
#!/usr/bin/python
import string
from datetime import date
from datetime import datetime, timedelta

print "#####################################################"
print "# Record start time and build complete job; STATE:3 #"
print "#####################################################"

activityIdStartedPath = r'C:\uiPath\var\activityIdToStart.var'
startTimeStampPath = r'C:\uiPath\var\startTimeStamp.record'
schtasksPrefixPath = r'C:\uiPath\lib\schtasksPrefix.line'
activityListFileBeautifiedPath = r'C:\uiPath\var\activityListValueBeautified.var'
completeScheduleRatePath = r'C:\uiPath\var\completeScheduleRate.var'
schtasksCommandState3Path = r'C:\uiPath\var\schtasksCommandState3.var'
lastStartActivityDatePath = r'C:\uiPath\var\lastStartActivityDate.var'

with open(activityIdStartedPath) as activityIdStartedFile:
    activityIdStarted = activityIdStartedFile.read()

# log
print str(datetime.now()) + " activityIdStarted : \n" + activityIdStarted + "\n"


with open(schtasksPrefixPath) as schtasksPrefixFile:
    schtasksPrefix = schtasksPrefixFile.read()


timeFormat = '%m/%d/%Y-%H:%M'
timeStamp = datetime.now().strftime(timeFormat)

# log
print str(datetime.now()) + " timeStamp : \n" + timeStamp + "\n"

recordLine = timeStamp + "\t" + activityIdStarted + "\n"
# append record list here
with open(startTimeStampPath,'a') as startTimeStampFile:
    startTimeStampFile.write(recordLine)


# log
print str(datetime.now()) + " recordLine : \n" + recordLine + "\n"

# debug command format
# print schtasksPrefix + r"  /SD 05/19/2017 /ST 21:04"


lastStartActivityDate = datetime.now().strftime('%m/%d/%Y')
with open(lastStartActivityDatePath,'w') as lastStartActivityDateFile:
    lastStartActivityDateFile.write(lastStartActivityDate)

# log
print str(datetime.now()) + " lastStartActivityDate : \n" + lastStartActivityDate + "\n"



# caculate schtasks start datetime

with open(activityListFileBeautifiedPath) as activityListFile:
    activityListString= activityListFile.read()
activityList = activityListString.strip().split("\n")

for line in activityList:
    if activityIdStarted == line.split()[2]:
        durationString = line.split()[8]

duration = timedelta(hours=int(durationString.split(":")[0]),minutes=int(durationString.split(":")[1])) 

# log
print str(datetime.now()) + " duration for " + activityIdStarted + ": \n" + str(duration) + "\n"


with open(completeScheduleRatePath) as completeScheduleRateFile:
    completeScheduleRateString = completeScheduleRateFile.read().strip()
completeScheduleRate = float(completeScheduleRateString)

# log
print str(datetime.now()) + " completeScheduleRate : \n" + completeScheduleRateString + "\n"

optimizedDuration =timedelta(seconds=duration.total_seconds() * completeScheduleRate)

# log
print str(datetime.now()) + " optimizedDuration with  completeScheduleRate:  \n" + str(optimizedDuration) + "\n"


completeTime = datetime.now() + optimizedDuration

completeTimeString = completeTime.strftime(timeFormat)

# log
print str(datetime.now()) + " completeTime:  \n" + completeTimeString + "\n"


schtasksPostfix = "/SD " + completeTimeString.split("-")[0] + " /ST " + completeTimeString.split("-")[1] 

schtasksCommandLine = schtasksPrefix + schtasksPostfix

# log
print str(datetime.now()) + " schtasksCommandLine : \n" + schtasksCommandLine + "\n"

# write schtasksCommandLine
with open(schtasksCommandState3Path,'w') as schtasksCommandState3File:
    schtasksCommandState3File.write(schtasksCommandLine)
