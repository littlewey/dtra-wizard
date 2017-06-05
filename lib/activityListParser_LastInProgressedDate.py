# -*- coding: utf-8 -*- 
#!/usr/bin/python
import string
from datetime import date
from datetime import datetime 
from datetime import timedelta 

print "####################################################################################"
print "# Parse the activities listed on lastInProgressedDate for only Paused & inProgress #"
print "####################################################################################"

activityListFilePath = r'C:\uiPath\var\activityListValueOriginal.var'
activityListFileBeautifiedPath = r'C:\uiPath\var\activityListValueBeautified.var'

pausedActivityPath = r'C:\uiPath\var\pausedActivity.list'
inProgressActivityPath = r'C:\uiPath\var\inProgressActivity.var'
dispatchedActivityPath = r'C:\uiPath\var\dispatchedActivity.list'


myActivityListPath = r'C:\uiPath\myActivityList.txt'

ignoredActivityIdPath = r'C:\uiPath\var\ignoredActivityId.list'

focusingLastStartDateViewPath = r'C:\uiPath\var\focusingLastStartDateView.var'

sourceTimeFormatActul = '%m/%d/%Y %I:%M %p'
sourceTimeFormatDueDate = '%m/%d/%Y %I:%M:%S %p'
timeFormat = '%m/%d/%Y-%H:%M'


with open(activityListFilePath) as activityListFile:
    activityListUrgly = activityListFile.read().strip('W6.Web.UI.Controls.W6DataGrid+W6DataGridItemData\n')

parsedActivityTable = str()

with open(ignoredActivityIdPath) as ignoredActivityIdFile:
    ignoredActivityId = ignoredActivityIdFile.read()

if ignoredActivityId != "NA":
    ignoredActivityIdList = ignoredActivityId.split()
else:
    ignoredActivityIdList = []

# init state variable

pausedActivity = str()
inProgressActivity = str()
dispatchedActivity = str()

myActivityList = str()
focusingLastStartDateView = "0"

#parsedActivityTable = "ProjectName\tWorkPackage\tActivityID\tNumber\tStatus\tAssignment_Start\tAssignment_Finish\tDueDate\tDuration\n"

# append only here
# myActivityList = "ActivityID           \tSta\tActivityName\n"

for activityItem in activityListUrgly.split('W6.Web.UI.Controls.W6DataGrid+W6DataGridItemData')[1:]:
    activityList = activityItem.split('\n')
    itemProjectName = activityList[1].strip()
    # here we limit itemWorkPackage itemActivityID itemStatus to fixed length to make datatable generation working fine in UiPath
    itemWorkPackage = activityList[2][:19] if len(activityList[2])>19 else activityList[2]
    itemActivityID = activityList[3][:21] if len(activityList[3])>21 else activityList[3]
    itemActivityName = activityList[4].strip()
    itemPriority = activityList[5].strip()
    itemStatus = activityList[6][:3]
    itemActualStart = datetime.strptime(activityList[7].strip(),sourceTimeFormatActul).strftime(timeFormat)
    itemActualFinish = datetime.strptime(activityList[8].strip(),sourceTimeFormatActul).strftime(timeFormat)
    itemActualDueDate = datetime.strptime(activityList[9].strip(),sourceTimeFormatDueDate).strftime(timeFormat)
    # note to strip() itemDuration will lead datatable generation issues in UiPath, here we leave it as it is.
    itemDuration = activityList[10]
    # assemble parsedActivityTable

    outputListForAppending = [itemProjectName, itemWorkPackage, itemActivityID, itemPriority, itemStatus, itemActualStart, itemActualFinish, itemActualDueDate, itemDuration ]
    if itemStatus != "Com":
        parsedActivityTable = parsedActivityTable + '\t'.join(outputListForAppending) + '\n'

    # handling state

    if itemStatus == "Pau" and itemActivityID not in ignoredActivityIdList :
        pausedActivity = pausedActivity + itemActivityID + '\n'
    if itemStatus == "InP":
        inProgressActivity = "" + itemActivityID
    #if itemStatus == "Dis":
    #    dispatchedActivity = dispatchedActivity + itemActivityID + '\n'

    # for myActivityList
    myActivityListForAppending = [itemActivityID, itemStatus, itemActivityName]
    if itemStatus != "Com":
        myActivityList = myActivityList + '\t'.join(myActivityListForAppending) + '\n'

with open(activityListFileBeautifiedPath,'a') as outputFile:
    outputFile.write(parsedActivityTable)

# log
print str(datetime.now()) + "append parsedActivityTable : \n" + parsedActivityTable + "\n"


print "########################"
print "# inProgressed recheck #"
print "########################"
if inProgressActivity == "":
    inProgressActivity = "NA"
    focusingLastStartDateView = "0"
else:
    focusingLastStartDateView = "1"

with open(inProgressActivityPath,'w') as inProgressActivityFile:
    inProgressActivityFile.write(inProgressActivity)
# log
print str(datetime.now()) + " inProgressActivity : \n" + inProgressActivity + "\n"
print str(datetime.now()) + " focusingLastStartDateView : \n" + focusingLastStartDateView + "\n"


print "##################"
print "# paused recheck #"
print "##################"

with open(pausedActivityPath) as pausedActivityFile:
    pausedActivity_startWeek = pausedActivityFile.read()


pasuedAct_writeMode = 'w' if pausedActivity_startWeek == "NA" else 'a'

# log
print str(datetime.now()) + " pausedActivity_startWeek : \n" + pausedActivity_startWeek + "\n"
print str(datetime.now()) + " pasuedAct_writeMode : \n" + pasuedAct_writeMode + "\n"


if pausedActivity != "":
    focusingLastStartDateView = "1"
    with open(pausedActivityPath, pasuedAct_writeMode) as pausedActivityFile:
        pausedActivityFile.write(pausedActivity)
else:
    pausedActivity = "NA"
# log
print str(datetime.now()) + " pausedActivity : \n" + pausedActivity + "\n"
print str(datetime.now()) + " focusingLastStartDateView : \n" + focusingLastStartDateView + "\n"


print "###################################"
print "# Write focusingLastStartDateView #"
print "###################################"


with open(focusingLastStartDateViewPath,'w') as focusingLastStartDateViewFile:
    focusingLastStartDateViewFile.write(focusingLastStartDateView)

#if dispatchedActivity == "":
#    dispatchedActivity = "NA"

#with open(dispatchedActivityPath,'w') as dispatchedActivityFile:
#    dispatchedActivityFile.write(dispatchedActivity)
# log
# print str(datetime.now()) + " dispatchedActivity : \n" + dispatchedActivity + "\n"

# [debug]
# print myActivityList


# append only
with open(myActivityListPath,'a') as myActivityListOutputFile:
    myActivityListOutputFile.write(myActivityList)

# log
print str(datetime.now()) + " myActivityList : \n" + myActivityList + "\n"