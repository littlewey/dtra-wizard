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
    itemProjectName = activityList[1].strip()
    itemWorkPackage = activityList[2][:19] if len(activityList[2])>19 else activityList[2]
    itemActivityID = activityList[3][:21] if len(activityList[3])>21 else activityList[3]
    itemActivityName = activityList[4].strip()
    itemPriority = activityList[5].strip()
    itemStatus = activityList[6][:3]
    itemActualStart = datetime.strptime(activityList[7].strip(),sourceTimeFormatActul).strftime(timeFormat)
    itemActualFinish = datetime.strptime(activityList[8].strip(),sourceTimeFormatActul).strftime(timeFormat)
    itemActualDueDate = datetime.strptime(activityList[9].strip(),sourceTimeFormatDueDate).strftime(timeFormat)
    itemDuration = activityList[10]
    # assemble parsedActivityTable

    outputListForAppending = [itemProjectName, itemWorkPackage, itemActivityID, itemPriority, itemStatus, itemActualStart, itemActualFinish, itemActualDueDate, itemDuration ]
    if itemStatus != "Com":
        parsedActivityTable = parsedActivityTable + '\t'.join(outputListForAppending) + '\n'

    # handling state

    if itemStatus == "Pau":
        pausedActivity = pausedActivity + itemActivityID + '\n'
    if itemStatus == "InP":
        inProgressActivity = "" + itemActivityID

    # for myActivityList
    myActivityListForAppending = [itemActivityID, itemStatus, itemActivityName]
    if itemStatus != "Com":
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