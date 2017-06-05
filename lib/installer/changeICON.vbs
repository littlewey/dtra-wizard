Const DESKTOP = &H10&

Set objShell = CreateObject("Shell.Application")

Set objFolder = objShell.NameSpace(DESKTOP)

Set objFolderItem = objFolder.ParseName("DTRA-Wizard.lnk")

Set objShortcut = objFolderItem.GetLink

objShortcut.SetIconLocation "c:\uiPath\lib\guiApp\ico\robot\robot.ico", 0

objShortcut.Save

Set objFolderItem = objFolder.ParseName("DTRA-Pause.lnk")

Set objShortcut = objFolderItem.GetLink

objShortcut.SetIconLocation "c:\uiPath\lib\guiApp\ico\pause.ico", 0

objShortcut.Save

Set objFolderItem = objFolder.ParseName("DTRA-selfCheck.lnk")

Set objShortcut = objFolderItem.GetLink

objShortcut.SetIconLocation "c:\uiPath\lib\guiApp\ico\selfCheck.ico", 0

objShortcut.Save