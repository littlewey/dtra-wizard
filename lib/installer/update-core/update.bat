cd /d C:\
rmdir upgradeBuffer /S /Q
mkdir uiPath-updater
xcopy uiPath\lib\installer\git-bash uiPath-updater /Y /e
uiPath-updater\git-cmd.exe git clone http://gitlab.swdp.me/Wey/dtra-wizard upgradeBuffer
xcopy upgradeBuffer\* uiPath /Y
rmdir upgradeBuffer /S /Q
