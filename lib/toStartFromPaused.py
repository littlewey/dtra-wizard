# -*- coding: utf-8 -*- 
#!/usr/bin/python
import string
from datetime import date
from datetime import datetime 

print "#############################################"
print "# select activity to be started from paused #"
print "#############################################"

activityIdToStart = str()
pausedActivityList = list()

preferredActivityIdPath = r'C:\uiPath\var\preferredActivityId.list'

activityIdToStartPath = r'C:\uiPath\var\activityIdToStart.var'

pausedActivityPath = r'C:\uiPath\var\pausedActivity.list'


with open(pausedActivityPath) as pausedActivityListFile:
    pausedActivityListString= pausedActivityListFile.read()
pausedActivityList = pausedActivityListString.strip().split("\n")

with open(preferredActivityIdPath) as preferredActivityIdFile:
    preferredActivityIdString= preferredActivityIdFile.read()

# log
print str(datetime.now()) + " pausedActivityListString : \n" + pausedActivityListString + "\n"


# log
print str(datetime.now()) + " preferredActivityIdString : \n" + preferredActivityIdString + "\n"

preferredActivityId = preferredActivityIdString.strip().split("\n")

activityIdToStart = pausedActivityList[0]


# if anyone is included in preferred act id list, choose it as the one to start
for activity in preferredActivityId:
    if activity in pausedActivityList:
        activityIdToStart = activity
        # log
        print str(datetime.now()) + " preferredActivityId selected : \n" + activity + "\n"
        break

with open(activityIdToStartPath,'w') as activityIdToStartFile:
    activityIdToStartFile.write(activityIdToStart)
# log
print str(datetime.now()) + " activityIdToStart : \n" + activityIdToStart + "\n"