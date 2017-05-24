# -*- coding: utf-8 -*- 
#!/usr/bin/python
import string

configInputPath = r'C:\uiPath\Preference_Configuration.csv'
outputStartDatePath = r'C:\uiPath\var\startDate.var'
outputPreferredActivityIdPath = r'C:\uiPath\var\preferredActivityId.list'
outputIgnoredActivityIdPath = r'C:\uiPath\var\ignoredActivityId.list'


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


###################### outputIgnoredActivityId #####################

ignoredActivityId = configCSV[2].split(',')[1:]

# remove "," in the end if existed 
if ignoredActivityId[-1] == '':
    IgnoredActivityId.pop()

# write "NA" when field was not filled

with open(outputIgnoredActivityIdPath,'w') as IgnoredActivityIdFile:
    if '-' not in ignoredActivityId[0]:
        IgnoredActivityIdFile.write('NA')
    else:
        IgnoredActivityIdFile.write('\n'.join(ignoredActivityId))

###################### outputIgnoredActivityId #####################