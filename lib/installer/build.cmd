
date /t > c:\uiPath\lib\installer\release\build"
time /t >> c:\uiPath\lib\installer\release\build"

"C:\Program Files (x86)\WinRAR\winrar" a -r -ep1 -inul -ibck -y -sfx -z"c:\uiPath\lib\installer\config.txt" -x@"c:\uiPath\lib\installer\rar-ignore-list.txt" -iiconc:\uiPath\lib\guiApp\ico\robot\robot.ico c:\uiPath\lib\installer\release\DTRA-Wizard-Setup-full.exe c:\uiPath 

"C:\Program Files (x86)\WinRAR\winrar" a -r -ep1 -inul -ibck -y -sfx -z"c:\uiPath\lib\installer\config-no-dependency.txt" -x@"c:\uiPath\lib\installer\rar-ignore-list-no-dependency.txt" -iiconc:\uiPath\lib\guiApp\ico\robot\robot.ico c:\uiPath\lib\installer\release\DTRA-Wizard-Setup-lite.exe c:\uiPath 
