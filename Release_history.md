2017/06/07
- update process optimized:avoid override Preference_Configuration.csv during OTA updating
- [Bug:coverred lines of activities cannot be selected by UiPath]
    + Workaround: add filter with condition: contains one of [status= "Dispatched","Paused","InProgress"]
- [Bug:status changed but not shown changed][pending]
    + Root cause:suspect bugs of DTRA web client triggerred by close window very fast
    + Workaround: add delay 2 seconds
    + Status: await further test
2017/06/06
- add build release for no-dependency package
- modify update source from github to gitlab to enhance speed
- DTRA-update: fixing xcopy switch by adding /e
- introduce DTRA-update to auto update dtra core via git clone
- add release_history.md & build date,time
2017/06/05
- Ignore list empty exceptions
- multi {W6.Web.UI.Controls.W6DataGrid+W6DataGridItemData\n} existed in orginal scarped data
- missing check existence of activityProgressedDuration.record
- completeScheduleRate one digit wrong caculation
- state:1 close window action missing
- make time window between two activities as 70 seconds
- add window size adjustment workflow