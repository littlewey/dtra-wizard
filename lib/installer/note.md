
# schtasks for start a robot example 

schtasks /CREATE /TN TEST_3 /TR "'C:\Program Files (x86)\UiPath Studio\UiRobot.exe' /file C:\uiPath\process\Main.xaml /monitor" /SC ONCE /SD 05/18/2017 /ST 15:54

