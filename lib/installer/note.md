# how to build a release

exec build-7zSfx.bat

# schtasks for start a robot example 

schtasks /CREATE /TN TEST_3 /TR "'C:\Program Files (x86)\UiPath Studio\UiRobot.exe' /file C:\uiPath\process\Main.xaml /monitor" /SC ONCE /SD 05/18/2017 /ST 15:54

# %LOCALAPPDATA%\UiPath\app-2017.1.6309.33850

schtasks /CREATE /TN toCompleteDTRA /TR "'%LOCALAPPDATA%\UiPath\app-2017.1.6309.33850\UiRobot.exe' /file C:\uiPath\process\Main.xaml /monitor" /SC ONCE /SD 05/19/2017 /ST 21:04 /F

* note /F means override existed ones

# query 
schtasks /QUERY /TN toCompleteDTRA /XML | findstr  /i /c:"Command" /c:"Arguments"

or

schtasks /QUERY /TN toCompleteDTRA /XML | findstr  ":"




@ start pause @

%LOCALAPPDATA%\UiPath\app-2017.1.6309.33850\UiRobot.exe /file C:\uiPath\process\pauseInProgressedActivity.xaml /monitor

# delete task
schtasks.exe /Delete /TN toCompleteDTRA /F

"/C echo [%DATE%_%TIME%  schtasks-cancel] >> C:\uiPath\var\log\schtasks.log & " + "schtasks.exe /Delete /TN toCompleteDTRA /F" + " >> C:\uiPath\var\log\schtasks.log & schtasks /QUERY /TN toCompleteDTRA /XML | findstr  : >> C:\uiPath\var\log\schtasks.log"


# update cli
cd /d C:\
rmdir upgradeBuffer /S /Q
mkdir uiPath-updater
xcopy uiPath\lib\installer\git-bash uiPath-updater /Y /e
uiPath-updater\cmd\git clone http://gitlab.swdp.me/Wey/dtra-wizard upgradeBuffer
xcopy upgradeBuffer\* uiPath /Y
rmdir upgradeBuffer /S /Q
