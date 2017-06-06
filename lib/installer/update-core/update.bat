cd /d C:\
rmdir upgradeBuffer /S /Q
mkdir uiPath-updater
xcopy uiPath\lib\installer\git-bash uiPath-updater /Y
uiPath-updater\git-cmd.exe git clone https://github.com/littlewey/dtra-wizard upgradeBuffer
xcopy upgradeBuffer\* uiPath /Y
rmdir upgradeBuffer /S /Q
