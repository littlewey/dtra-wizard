# -*- coding: utf-8 -*- 
#!/usr/bin/python
import string
import os.path
from datetime import datetime

lastStartActDateRecord_ifExistsPath = r'C:\uiPath\var\lastStartActDateRecord_ifExists.var'


lastStartActDateRecord_ifExists = os.path.exists(r"C:\uiPath\var\lastStartActivityDate.record")

with open(lastStartActDateRecord_ifExistsPath,'w') as lastStartActDateRecord_ifExistsFile:
    lastStartActDateRecord_ifExistsFile.write(str(lastStartActDateRecord_ifExists))

# log
print str(datetime.now()) + " lastStartActDateRecord_ifExistsFile : \n" + str(lastStartActDateRecord_ifExists) + "\n"
