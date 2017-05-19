
# schtasks for start a robot example 

schtasks /CREATE /TN TEST_3 /TR "'C:\Program Files (x86)\UiPath Studio\UiRobot.exe' /file C:\uiPath\process\Main.xaml /monitor" /SC ONCE /SD 05/18/2017 /ST 15:54

# %LOCALAPPDATA%\UiPath\app-2017.1.6309.33850

schtasks /CREATE /TN TEST_3 /TR "'%LOCALAPPDATA%\UiPath\app-2017.1.6309.33850\UiRobot.exe' /file C:\uiPath\process\Main.xaml /monitor" /SC ONCE /SD 05/19/2017 /ST 21:04
