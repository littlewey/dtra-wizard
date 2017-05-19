# -*- coding: utf-8 -*- 
#!/usr/bin/python
import string

configInputPath = r'C:\uiPath\Preference_Configuration.csv'
outputStartDatePath = r'C:\uiPath\var\startDate.var'
outputPreferredActivityIdPath = r'C:\uiPath\var\preferredActivityId.list'


with open(configInputPath) as configCSVFile:
    configCSV = configCSVFile.read().split('\n')


###################### preferredStartDate #####################
preferredStartDate = configCSV[0].split(',')[1]
# write only when field was filled 
if '/' in preferredStartDate:
    with open(outputStartDatePath,'w') as outputStartDateFile:
        outputStartDateFile.write(preferredStartDate)

###################### preferredStartDate #####################



###################### preferredActivityId #####################

preferredActivityId = configCSV[1].split(',')[1:]

# remove "," in the end if existed 
if preferredActivityId[-1] == '':
    preferredActivityId.pop()

# write "NA" when field was not filled

with open(outputPreferredActivityIdPath,'w') as preferredActivityIdFile:
    if '-' not in preferredActivityId[0]:
        preferredActivityIdFile.write('NA')
    else:
        preferredActivityIdFile.write('\n'.join(preferredActivityId))

###################### preferredActivityId #####################


parsedActivityTable = str()
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
    parsedActivityTable = parsedActivityTable + '\t'.join(outputListForAppending) + '\n'
    # for myActivityList

    myActivityListForAppending = [itemActivityID, activityList[6], activityList[4]]
    if activityList[6] != "Completed":
        myActivityList = myActivityList + '\t'.join(myActivityListForAppending) + '\n'

with open(activityListFileBeautifiedPath,'w') as outputFile:
    outputFile.write(parsedActivityTable)
# [debug]
# print myActivityList
with open(myActivityListPath,'w') as myActivityListOutputFile:
    myActivityListOutputFile.write(myActivityList)