$today = Get-Date
$listForString =$today.month,($today.day - $today.DayOfWeek.value__ + 1),$today.year
$mondayOfThisWeek = [system.String]::Join("/",$listForString)
$mondayOfThisWeek > mondayOfThisWeek.txt