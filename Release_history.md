2017/06/16
- lib/activityListParser.py [adjustment for SPM] consider other statuses apart from Pau,InP,Dis
- lib/state2_timeStamp_schtasksBuilding.py [Improvement for schtasks] consider start time earlier than now
- state3_timeStamp_schtasksBuilding.py [Improvement for schtasks] consider start time earlier than now
2017/06/09
- workflow modified to be Compatible with SPM client view
2017/06/08
- update updater to fix new bug involved causing file not updated
    + It's found by Summer complete workflow didnt work as expected
    + Root cause: toComplete.py was not updated in latest update
    + Solution: corrected updater program, wipe wizard folder and reinstall
    + Status: [passed]
- [unexpected siutation on "SiteName not empty"] [ongoing]
    + During test from Core Design team(Stephen Yang), it's found not all IWP activities are with Sitename empty, this requires changing of activity list.
    + Solution: update selfcheck process and modify adjustment of activitylist column order
    + Status: initial test[Passed], further test[will be done by Summer]
- [Bug:status changed but not shown changed][consider passed]
    + Root cause:suspect bugs of DTRA web client triggerred by close window very fast
    + Workaround: add delay 2 seconds
    + Status: issue not occured anymore
    + updated action:changed delay time from 2 seconds to 3 seconds on safe side
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