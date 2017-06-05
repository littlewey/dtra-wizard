# -*- coding: utf-8 -*- 
#!/usr/bin/python
import string
from datetime import date
from datetime import datetime, timedelta
import os

print "#####################################################"
print "# Record start time and build complete job; STATE:2 #"
print "#####################################################"

activityIdStartedPath = r'C:\uiPath\var\activityIdToStart.var'
startTimeStampPath = r'C:\uiPath\var\startTimeStamp.record'
schtasksPrefixPath = r'C:\uiPath\lib\schtasksPrefix.line'
activityListFileBeautifiedPath = r'C:\uiPath\var\activityListValueBeautified.var'
completeScheduleRatePath = r'C:\uiPath\var\completeScheduleRate.var'
#lastStartActivityDatePath = r'C:\uiPath\var\lastStartActivityDate.record'


schtasksCommandState2Path = r'C:\uiPath\var\schtasksCommandState2.var'
activityProgressedDurationPath = r'C:\uiPath\var\activityProgressedDuration.record'


with open(activityIdStartedPath) as activityIdStartedFile:
    activityIdStarted = activityIdStartedFile.read()

# log
print str(datetime.now()) + " activityIdStarted : \n" + activityIdStarted + "\n"


################################################################################
if os.path.isfile(activityProgressedDurationPath):
    print "################################################################"
    print "# Parsing activityProgressedDuration for " + activityIdStarted+" #"
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
        if line.split("\t")[0] == activityIdStarted:
            lineTimedelta = line.split("\t")[1]
            timedeltaList = lineTimedelta.replace("-",":").split(":")
            sumActivityProgressedDuration = sumActivityProgressedDuration + timedelta(days=int(timedeltaList[DAY]),hours=int(timedeltaList[Hour]),minutes=int(timedeltaList[Minute]),seconds=int(timedeltaList[Second]))


    # log
    print str(datetime.now()) + " sumActivityProgressedDuration : \n" + str(sumActivityProgressedDuration) + "\n"
else:
    # log
    print str(datetime.now()) + " C:\uiPath\var\activityProgressedDuration.record not exist: \n"
    sumActivityProgressedDuration = timedelta(minutes=0)
################################################################################

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


#lastStartActivityDate = datetime.now().strftime('%m/%d/%Y')
#with open(lastStartActivityDatePath,'w') as lastStartActivityDateFile:
#    lastStartActivityDateFile.write(lastStartActivityDate)

# log
#print str(datetime.now()) + " lastStartActivityDate : \n" + lastStartActivityDate + "\n"



# caculate schtasks start datetime

with open(activityListFileBeautifiedPath) as activityListFile:
    activityListString= activityListFile.read()
activityList = activityListString.strip().split("\n")

for line in activityList:
    if activityIdStarted == line.split()[2]:
        durationString = line.split()[8]

plannedDuration = timedelta(hours=int(durationString.split(":")[0]),minutes=int(durationString.split(":")[1])) 


# log
print str(datetime.now()) + " plannedDuration for " + activityIdStarted + ": \n" + str(plannedDuration) + "\n"


with open(completeScheduleRatePath) as completeScheduleRateFile:
    completeScheduleRateString = completeScheduleRateFile.read().strip()
completeScheduleRate = float(completeScheduleRateString)

# log
print str(datetime.now()) + " completeScheduleRate : \n" + completeScheduleRateString + "\n"

optimizedDuration =timedelta(seconds=plannedDuration.total_seconds() * completeScheduleRate)

# log
print str(datetime.now()) + " optimizedDuration with  completeScheduleRate:  \n" + str(optimizedDuration) + "\n"


leftDuration = optimizedDuration - sumActivityProgressedDuration

# log
print str(datetime.now()) + " leftDuration:  \n" + str(leftDuration) + "\n"


# in case leftDuration.total_seconds() <= 420

completeTime = datetime.now() + (leftDuration if leftDuration.total_seconds() > 420 else timedelta(minutes=7))

completeTimeString = completeTime.strftime(timeFormat)

# log
print str(datetime.now()) + " completeTime:  \n" + completeTimeString + "\n"


schtasksPostfix = "/SD " + completeTimeString.split("-")[0] + " /ST " + completeTimeString.split("-")[1] 

schtasksCommandLine = schtasksPrefix + schtasksPostfix

# log
print str(datetime.now()) + " schtasksCommandLine : \n" + schtasksCommandLine + "\n"

# write schtasksCommandLine
with open(schtasksCommandState2Path,'w') as schtasksCommandState2File:
    schtasksCommandState2File.write(schtasksCommandLine)
