# -*- coding: utf-8 -*- 
#!/usr/bin/python
import string
from datetime import date
from datetime import datetime, timedelta
import random
import os

print "####################################################"
print "# check complete time and build start/complete job #"
print "####################################################"

activityIdToComplete = str()
inProgressActivityPath = r'C:\uiPath\var\inProgressActivity.var'

with open(inProgressActivityPath) as inProgressActivityFile:
    inProgressActivity= inProgressActivityFile.read().strip()

activityIdToComplete = inProgressActivity

activityListFileBeautifiedPath = r'C:\uiPath\var\activityListValueBeautified.var'
activityProgressedDurationPath = r'C:\uiPath\var\log\activityProgressedDuration.record'
activityProgressedDuration = str()

with open(activityListFileBeautifiedPath) as activityListFile:
    activityListString= activityListFile.read()
activityList = activityListString.strip().split("\n")



durationString = str()

# plannedDuration
for line in activityList:
    if inProgressActivity == line.split()[2]:
        durationString = line.split()[8]
plannedDuration = timedelta(hours=int(durationString.split(":")[0]),minutes=int(durationString.split(":")[1])) 
# log
print str(datetime.now()) + " plannedDuration for " + activityIdToComplete + ": \n" + str(plannedDuration) + "\n"


# completeScheduleRate
completeScheduleRatePath = r'C:\uiPath\var\completeScheduleRate.var'
with open(completeScheduleRatePath) as completeScheduleRateFile:
    completeScheduleRateString = completeScheduleRateFile.read().strip()
completeScheduleRate = float(completeScheduleRateString)
# log
print str(datetime.now()) + " completeScheduleRate : \n" + completeScheduleRateString + "\n"

# with random
randomRateDelta = random.uniform(-0.01, 0.01)
# log
print str(datetime.now()) + " randomRateDelta : \n" + str(randomRateDelta) + "\n"

# randomed completeScheduleRate
completeScheduleRate = completeScheduleRate + randomRateDelta
# log
print str(datetime.now()) + " completeScheduleRate : \n" + str(completeScheduleRate) + "\n"

optimizedDuration =timedelta(seconds=plannedDuration.total_seconds() * completeScheduleRate)
# log
print str(datetime.now()) + " optimizedDuration with  completeScheduleRate:  \n" + str(optimizedDuration) + "\n"


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
    if line.split()[1].strip() == activityIdToComplete:
        startTimeRecordLatest = line.split()[0].strip()

# log
print str(datetime.now()) + " startTimeRecordLatest : \n" + startTimeRecordLatest + "\n"

timeFormat = '%m/%d/%Y-%H:%M'

activityLastStartedDatetime = datetime.strptime(startTimeRecordLatest,timeFormat)

#####################################################################

activityProgressedDuration = datetime.now() - activityLastStartedDatetime

# log
print str(datetime.now()) + " activityProgressedDuration :" 
print activityProgressedDuration

################################################################################
activityProgressedDurationPath = r'C:\uiPath\var\activityProgressedDuration.record'
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
    print str(datetime.now()) + " C:\uiPath\var\activityProgressedDuration.record not exist: \n"
    sumActivityProgressedDuration = timedelta(minutes=0)
################################################################################

leftDuration = optimizedDuration - sumActivityProgressedDuration - activityProgressedDuration
# log
print str(datetime.now()) + " leftDuration:  \n" + str(leftDuration) + "\n"

intervalTimerNextStart = 180
# log
print str(datetime.now()) + " intervalTimerNextStart:  \n" + str(intervalTimerNextStart) + "\n"

state1_ifCompeleteNowPath = r'C:\uiPath\var\state1_ifCompeleteNow.var'
state1_ifCompeleteNow = "0" if leftDuration.total_seconds() > intervalTimerNextStart else inProgressActivity
with open(state1_ifCompeleteNowPath,'w') as state1_ifCompeleteNowFile:
    state1_ifCompeleteNowFile.write(state1_ifCompeleteNow)

completeTime = datetime.now() + (leftDuration if leftDuration.total_seconds() > intervalTimerNextStart else timedelta(minutes=7))

if state1_ifCompeleteNow != "0":
    completeTime = datetime.now() + timedelta(seconds=70)

timeFormat = '%m/%d/%Y-%H:%M'
completeTimeString = completeTime.strftime(timeFormat)
# log
print str(datetime.now()) + " completeTime:  \n" + completeTimeString + "\n"

schtasksPrefixPath = r'C:\uiPath\lib\schtasksPrefix.line'
with open(schtasksPrefixPath) as schtasksPrefixFile:
    schtasksPrefix = schtasksPrefixFile.read()

schtasksPostfix = "/SD " + completeTimeString.split("-")[0] + " /ST " + completeTimeString.split("-")[1] 
schtasksCommandLine = schtasksPrefix + schtasksPostfix

# log
print str(datetime.now()) + " schtasksCommandLine : \n" + schtasksCommandLine + "\n"

schtasksCommandState1Path = r'C:\uiPath\var\schtasksCommandState1.var'
# write schtasksCommandLine
with open(schtasksCommandState1Path,'w') as schtasksCommandState1File:
    schtasksCommandState1File.write(schtasksCommandLine)
