echo ####################
echo ## create entries ##
echo ####################

copy uiPath\lib\installer\post-setup\*.lnk %systemdrive%\users\%username%\Desktop

echo ##################
echo ## Change icons ##
echo ##################

start /wait uiPath\lib\installer\changeICON.vbs

echo ####################
echo ## install Python ##
echo ####################

start /wait msiexec /i  uiPath\lib\installer\dependency\python-2.7.13.msi TARGETDIR=c:\python27 ALLUSERS=1 /qb

echo ##################
echo ## install .Net ##
echo ##################

start /wait uiPath\lib\installer\dependency\NDP461-KB3102436-x86-x64-AllOS-ENU.exe    /norestart

echo ########################
echo ## prevent from sleep ##
echo ########################

powercfg.exe -change -standby-timeout-ac 0
powercfg.exe -change -hibernate-timeout-ac 0
powercfg.exe -change -standby-timeout-dc 180
powercfg.exe -change -hibernate-timeout-dc 180

echo ####################
echo ## install UiPath ##
echo ####################

start /wait uiPath\lib\installer\dependency\UiPathStudio.exe /qb

