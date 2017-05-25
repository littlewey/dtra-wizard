# -*- coding: utf-8 -*- 
#!/usr/bin/python
import string
from datetime import date
from datetime import datetime, timedelta

activityIdToStart = str()
dispatchedActivityList = list()
statePath = r'C:\uiPath\var\state.var'
state = str()

activityDueTimeAdjustmentPath = r'C:\uiPath\var\log\activityDueTimeAdjustment.record'
activityDueTimeAdjustment = str()
preferredActivityIdPath = r'C:\uiPath\var\preferredActivityId.list'
activityListFileBeautifiedPath = r'C:\uiPath\var\activityListValueBeautified.var'

activityIdToStartPath = r'C:\uiPath\var\activityIdToStart.var'

with open(activityListFileBeautifiedPath) as activityListFile:
    activityListString= activityListFile.read()
activityList = activityListString.strip().split("\n")

with open(preferredActivityIdPath) as preferredActivityIdFile:
    preferredActivityIdString= preferredActivityIdFile.read()
preferredActivityId = preferredActivityIdString.strip().split("\n")

activityIdToStart = activityList[0].split('\t')[2]

# got dispatched act id list
for line in activityList:
    dispatchedActivityList.append(line.split('\t')[2])

# if anyone is included in preferred act id list, choose it as the one to start
for activity in preferredActivityId:
    if activity in dispatchedActivityList:
        activityIdToStart = activity
        break

with open(activityIdToStartPath,'w') as activityIdToStartFile:
    activityIdToStartFile.write(activityIdToStart)
