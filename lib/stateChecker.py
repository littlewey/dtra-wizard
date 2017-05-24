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
dispatchedActivityPath = r'C:\uiPath\var\dispatchedActivity.list'

with open(pausedActivityPath) as pausedActivityFile:
    pausedActivity = pausedActivityFile.read()

with open(inProgressActivityPath) as inProgressActivityFile:
    inProgressActivity = inProgressActivityFile.read()

with open(ignoredActivityIdPath) as ignoredActivityIdFile:
    ignoredActivityId = ignoredActivityIdFile.read()

if ignoredActivityId != "NA":
    ignoredActivityIdList = ignoredActivityId.split()

with open(dispatchedActivityPath) as dispatchedActivityFile:
    dispatchedActivity = dispatchedActivityFile.read()

if dispatchedActivity != "NA":
    dispatchedActivityList = dispatchedActivity.split()

if inProgressActivity != "NA":
    state = "withInprogressed"
# Inprogressed are NA from here
elif pausedActivity != "NA":
    state = "noInprogressed_WithPaused"
    # considering all paused activity in ignore list case
    if ignoredActivityId != "NA":
        pausedActivityList = pausedActivity.split()
        numberOfPausedActivity = len(pausedActivityList)
        for activity in pausedActivityList:
            if activity in ignoredActivityIdList:
                numberOfPausedActivity = numberOfPausedActivity - 1
        if numberOfPausedActivity <= 0:
            if dispatchedActivity != "NA":
                state = "noInprogressedNoPaused_WithDispatched"
# Paused are NA from here
    # dispatched:Yes
elif dispatchedActivity != "NA":
    state = "noInprogressedNoPaused_WithDispatched"
    # considering all dispatched activity in ignore list case
    if ignoredActivityId != "NA":
        dispatchedActivityList = dispatchedActivity.split()
        numberOfdispatchedActivity = len(dispatchedActivityList)
        for activity in dispatchedActivityList:
            if activity in ignoredActivityIdList:
                numberOfdispatchedActivity = numberOfdispatchedActivity - 1
        if numberOfdispatchedActivity <= 0:
            state = "NA"
else:
    state = "NA"


with open(stateCodePath,'w') as stateFile:
    stateFile.write(stateCode[state])