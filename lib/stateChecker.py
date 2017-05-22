# -*- coding: utf-8 -*- 
#!/usr/bin/python
import string
from datetime import date
from datetime import datetime 

statePath = r'C:\uiPath\var\state.var'
state = str()

#with open(xxxPath) as xxxFile:
#    xxx = xxxFile.read()


with open(statePath,'w') as stateFile:
    stateFile.write(state)