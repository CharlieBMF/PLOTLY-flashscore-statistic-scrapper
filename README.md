# PLOTLY-flashscore-statistic-scrapper
This is a scrapper for popular sport website - flashscore. Scrapping page &amp; creating data visualization for football matches in last days,

# Details
 
Program uses page: 
https://www.flashscore.pl/

1. Opens main page which shows matches from actual day.
<img src="https://user-images.githubusercontent.com/109242797/212497855-04d3765d-e012-4eaa-9fc4-c41313d87a64.png" alt='not found' title='FlashscoreMain'>

2. Moves days backward. Number of days depends on user choices:
<img src="https://user-images.githubusercontent.com/109242797/212498013-ee27dd10-8cb6-41e7-a8ff-1611f47f2297.png" alt='not found' title='DayPicker'>

3. Matches in some leagues on the list are hidden. It opens all hiddens leagues.

BEFORE OPEN: <br>
<img src="https://user-images.githubusercontent.com/109242797/212498079-61b66d02-8fff-46ff-ba1d-29adffb3397a.png" alt='not found' title='HiddenLeagues'>
<br><br>

AFTER OPEN:
<br>
<img src="https://user-images.githubusercontent.com/109242797/212498170-2243e80e-58f5-4452-a4f4-d9038ae6d726.png" alt='not found' title='UnhiddenLeagues'>

4. Scrapping website source. Acquiring data. Moves to next day if needed. 
<img src="https://user-images.githubusercontent.com/109242797/212498396-679710ee-d2f4-4378-979f-b415f36d0660.png" alt='not found' title='Statistic'>

5. Display analysis on plotly server.
<img src="https://user-images.githubusercontent.com/109242797/212498294-3935fbd4-fed3-4044-b582-96e6a3ebcd46.png" alt='not found' title='Statistic'>




