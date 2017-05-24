# -*- coding: utf-8 -*- 
#!/usr/bin/python
import string
from datetime import date
from datetime import datetime 

stateCode = {
    "NA" : "0",
    "withInprogressed" : "1",
    "noInprogressed_WithPaused" : "2",
    "noInprogressedNoPaused_WithDispatched" : "3"
}

# state code mapping

stateCodePath = r'C:\uiPath\var\state.var'
state = "NA"


pausedActivityPath = r'C:\uiPath\var\pausedActivity.list'
inProgressActivityPath = r'C:\uiPath\var\inProgressActivity.var'
ignoredActivityIdPath = r'C:\uiPath\var\ignoredActivityId.list'


with open(pausedActivityPath) as pausedActivityFile:
    pausedActivity = pausedActivityFile.read()

with open(inProgressActivityPath) as inProgressActivityFile:
    inProgressActivity = inProgressActivityFile.read()

with open(ignoredActivityIdPath) as ignoredActivityIdFile:
    ignoredActivityId = ignoredActivityIdFile.read()

if ignoredActivityId != "NA":
    ignoredActivityIdList = ignoredActivityId.split()


if inProgressActivity != "NA":
    state = "withInprogressed"
elif pausedActivity != "NA":
    state = "noInprogressed_WithPaused"
    if ignoredActivityId != "NA":
        pausedActivitiesList = pausedActivity.split()
        numberOfPausedActivity = len(pausedActivitiesList)
        for activity in pausedActivitiesList:
            if activity in ignoredActivityIdList:
                numberOfPausedActivity = numberOfPausedActivity - 1
        if numberOfPausedActivity <= 0:
            if 
            state = "noInprogressedNoPaused_WithDispatched"
elif 


with open(stateCodePath,'w') as stateFile:
    stateFile.write(stateCode[state])