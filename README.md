# ColesVsWooles Web Scraping
## Automated Web Scraping Coles Vs Woolies using Selenium

This was a project I did in June of 2021 to compare prices of two biggest retail shopping brands in Australia - Coles and Woolworths
Code uses Selenium to web scrape data from coles and woolworths and populates gathered data into Google Sheets using 'Google sheet API'. Gathered data in sheet can be used to compare price of products for like to like items. 
Object-Oriented Programming is used for user to use the project as per needed.

## Setting up the project
1. Install the Selenium Python library and place a ChromeDriver executable on your path. `chrome_driver_path = "\\\chromedriver.exe"`
2. Install dependencies - 'Selenium' and '__future__' via pip install or other prefered method(s)
3. Register an account with google colud and get API KEY. You may need to setup google platform account ID for credentials
```
get account - https://cloud.google.com/
setup project - https://console.cloud.google.com/home/dashboard?authuser=1&project="YOUR PROJECT NAME"
get keys -https://console.cloud.google.com/iam-admin/serviceaccounts/details
```
## Logic 
`coles.py` has code for scraping coles site by `suburb` and `item` where both are set as strings for inputs, output is a JSON
`woolies.py` has the code for scraping woolworths site by `item` where input is a string as well, output is a JSON
Both files add their brand name in fornt of the serach field for relevent result to be shown. This result then can be compered to get price deffierence and further data analysis. Output spreadsheet and be even taken as a form or outputed as a form (Google forms) for better visual representation.
Google sheet is used as a simple form of database here. `googlesheet1.py` is where the google sheet API lives. Output from above two methods are passed in as .JSON
`main.py` is where all three files are called and excecuted to get final results popultaed in the sheet



Please feel free to fork it / contribute to it
