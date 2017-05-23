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

with open(pausedActivityPath) as pausedActivityFile:
    pausedActivity = pausedActivityFile.read()

with open(inProgressActivityPath) as inProgressActivityFile:
    inProgressActivity = inProgressActivityFile.read()

if inProgressActivity != "NA":
    state = "withInprogressed"
elif pausedActivity != "NA":
    state = "noInprogressed_WithPaused"
elif 


with open(stateCodePath,'w') as stateFile:
    stateFile.write(stateCode[state])