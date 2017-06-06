echo ####################
echo ## create entries ##
echo ####################

copy uiPath\lib\installer\post-setup\*.lnk %systemdrive%\users\%username%\Desktop

echo ##################
echo ## Change icons ##
echo ##################

start /wait uiPath\lib\installer\changeICON.vbs


echo ########################
echo ## prevent from sleep ##
echo ########################

powercfg.exe -change -standby-timeout-ac 0
powercfg.exe -change -hibernate-timeout-ac 0
powercfg.exe -change -standby-timeout-dc 180
powercfg.exe -change -hibernate-timeout-dc 180


