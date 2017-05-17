# -*- coding: utf-8 -*- 
#!/usr/bin/python
import string
from datetime import date
from datetime import datetime 

activityListFilePath = r'C:\uiPath\var\activityListValueOriginal.var'
activityListFileBeautifiedPath = r'C:\uiPath\var\activityListValueBeautified.var'

sourceTimeFormatActul = '%m/%d/%Y %I:%M %p'
sourceTimeFormatDueDate = '%m/%d/%Y %I:%M:%S %p'
timeFormat = '%m/%d/%Y-%H:%M'


with open(activityListFilePath) as activityListFile:
    activityListUrgly = activityListFile.read()
parsedActivityTable = str()
#parsedActivityTable = "ProjectName\tWorkPackage\tActivityID\tNumber\tStatus\tAssignment_Start\tAssignment_Finish\tDueDate\tDuration\n"
for activityItem in activityListUrgly.split('W6.Web.UI.Controls.W6DataGrid+W6DataGridItemData')[1:]:
    activityList = activityItem.split('\n')
    itemWorkPackage = activityList[2][:19] if len(activityList[2])>19 else activityList[2]
    itemActivityID = activityList[3][:21] if len(activityList[3])>21 else activityList[3]

    itemActualStart = datetime.strptime(activityList[7],sourceTimeFormatActul).strftime(timeFormat)
    itemActualFinish = datetime.strptime(activityList[8],sourceTimeFormatActul).strftime(timeFormat)
    itemActualDueDate = datetime.strptime(activityList[9],sourceTimeFormatDueDate).strftime(timeFormat)

    outputListForAppending = [activityList[1], itemWorkPackage, itemActivityID , activityList[5], activityList[6], itemActualStart, itemActualFinish, itemActualDueDate, activityList[10] ]

    # append by +
    parsedActivityTable = parsedActivityTable + '\t'.join(outputListForAppending) + '\n'
with open(activityListFileBeautifiedPath,'w') as outputFile:
    outputFile.write(parsedActivityTable)