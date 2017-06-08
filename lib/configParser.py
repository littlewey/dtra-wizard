# -*- coding: utf-8 -*- 
#!/usr/bin/python
import string
from datetime import date
from datetime import datetime

print "#################################"
print "# parse configuration variables #"
print "#################################"

configInputPath = r'C:\uiPath\Preference_Configuration.csv'
outputStartDatePath = r'C:\uiPath\var\startDate.var'
outputPreferredActivityIdPath = r'C:\uiPath\var\preferredActivityId.list'
outputIgnoredActivityIdPath = r'C:\uiPath\var\ignoredActivityId.list'
outputCompleteScheduleRatePath = r'C:\uiPath\var\completeScheduleRate.var'

with open(configInputPath) as configCSVFile:
    configCSV = configCSVFile.read().split('\n')


###################### preferredStartDate #####################
preferredStartDate = configCSV[0].split(',')[1]
if preferredStartDate == "":
    preferredStartDate = "NA"
# write only when field was filled 
if '/' in preferredStartDate:
    with open(outputStartDatePath,'w') as outputStartDateFile:
        outputStartDateFile.write(preferredStartDate)
# log
print str(datetime.now()) + " preferredStartDate : \n" + preferredStartDate + "\n"

###################### preferredStartDate #####################



###################### preferredActivityId #####################

preferredActivityId = configCSV[1].split(',')[1:]

# remove "," in the end if existed 
if preferredActivityId[-1] == '':
    preferredActivityId.pop()
if preferredActivityId == []:
    preferredActivityId = ['NA']

# write "NA" when field was not filled

with open(outputPreferredActivityIdPath,'w') as preferredActivityIdFile:
    if '-' not in preferredActivityId[0]:
        preferredActivityIdFile.write('NA')
    else:
        preferredActivityIdFile.write('\n'.join(preferredActivityId))


# log
print str(datetime.now()) + " preferredActivityId : \n" + '\n'.join(preferredActivityId) + "\n"
###################### preferredActivityId #####################


###################### outputIgnoredActivityId #####################

ignoredActivityId = configCSV[2].split(',')[1:]

# remove "," in the end if existed 
if ignoredActivityId[-1] == '':
    ignoredActivityId.pop()
if ignoredActivityId == []:
    ignoredActivityId = ['NA']
# write "NA" when field was not filled

with open(outputIgnoredActivityIdPath,'w') as IgnoredActivityIdFile:
    if '-' not in ignoredActivityId[0]:
        IgnoredActivityIdFile.write('NA')
    else:
        IgnoredActivityIdFile.write('\n'.join(ignoredActivityId))
# log
print str(datetime.now()) + " ignoredActivityId : \n" + '\n'.join(ignoredActivityId) + "\n"

###################### outputIgnoredActivityId #####################


###################### outputCompleteScheduleRate #####################
completeScheduleRate = configCSV[3].split(',')[1]
if  completeScheduleRate == "":
    completeScheduleRate = "1"

# write only when field was filled 
if '%' not in completeScheduleRate:
    completeScheduleRate = "1"
else:
    completeScheduleRate = str(float(configCSV[3].split(',')[1][:-1])/100)

with open(outputCompleteScheduleRatePath,'w') as outputCompleteScheduleRateFile:
    outputCompleteScheduleRateFile.write(completeScheduleRate)

# log
print str(datetime.now()) + " completeScheduleRate : \n" + completeScheduleRate + "\n"

###################### outputCompleteScheduleRate #####################