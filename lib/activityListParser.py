# -*- coding: utf-8 -*- 
#!/usr/bin/python
import string
from datetime import date
from datetime import datetime 

activityListFilePath = r'C:\uiPath\var\activityListValueOriginal.var'
activityListFileBeautifiedPath = r'C:\uiPath\var\activityListValueBeautified.var'

pausedActivityPath = r'C:\uiPath\var\pausedActivity.list'
inProgressActivityPath = r'C:\uiPath\var\inProgressActivity.var'


myActivityListPath = r'C:\uiPath\myActivityList.txt'

sourceTimeFormatActul = '%m/%d/%Y %I:%M %p'
sourceTimeFormatDueDate = '%m/%d/%Y %I:%M:%S %p'
timeFormat = '%m/%d/%Y-%H:%M'


with open(activityListFilePath) as activityListFile:
    activityListUrgly = activityListFile.read()

parsedActivityTable = str()

# init state variable

pausedActivity = str()
inProgressActivity = str()

myActivityList = str()


#parsedActivityTable = "ProjectName\tWorkPackage\tActivityID\tNumber\tStatus\tAssignment_Start\tAssignment_Finish\tDueDate\tDuration\n"

myActivityList = "ActivityID           \tStatus    \tActivityName\n"

for activityItem in activityListUrgly.split('W6.Web.UI.Controls.W6DataGrid+W6DataGridItemData')[1:]:
    activityList = activityItem.split('\n')
    itemWorkPackage = activityList[2][:19] if len(activityList[2])>19 else activityList[2]
    itemActivityID = activityList[3][:21] if len(activityList[3])>21 else activityList[3]
    itemActualStart = datetime.strptime(activityList[7],sourceTimeFormatActul).strftime(timeFormat)
    itemActualFinish = datetime.strptime(activityList[8],sourceTimeFormatActul).strftime(timeFormat)
    itemActualDueDate = datetime.strptime(activityList[9],sourceTimeFormatDueDate).strftime(timeFormat)
    # assemble parsedActivityTable
    outputListForAppending = [activityList[1], itemWorkPackage, itemActivityID , activityList[5], activityList[6], itemActualStart, itemActualFinish, itemActualDueDate, activityList[10] ]
    if activityList[6] != "Completed":
        parsedActivityTable = parsedActivityTable + '\t'.join(outputListForAppending) + '\n'

    # handling state

    if activityList[6] == "Paused":
        pausedActivity = pausedActivity + itemActivityID + '\n'
    if activityList[6] == "InProgress":
        inProgressActivity = "" + itemActivityID

    # for myActivityList
    myActivityListForAppending = [itemActivityID, activityList[6], activityList[4]]
    if activityList[6] != "Completed":
        myActivityList = myActivityList + '\t'.join(myActivityListForAppending) + '\n'

with open(activityListFileBeautifiedPath,'w') as outputFile:
    outputFile.write(parsedActivityTable)

if pausedActivity == "":
    pausedActivity = "NA"

with open(pausedActivityPath,'w') as pausedActivityFile:
    pausedActivityFile.write(pausedActivity)

if inProgressActivity == "":
    inProgressActivity = "NA"

with open(inProgressActivityPath,'w') as inProgressActivityFile:
    inProgressActivityFile.write(inProgressActivity)

# [debug]
# print myActivityList
with open(myActivityListPath,'w') as myActivityListOutputFile:
    myActivityListOutputFile.write(myActivityList)