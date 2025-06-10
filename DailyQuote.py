import requests 
from datetime import date
import calendar
#payload = {'keyword':'change'} not free LOL #filters the request to just focus on quotes about success and focus, note: keyword is necessary to let it know success is a keyword
response = requests.get("https://zenquotes.io/api/quotes/random") # adding the random at end makes the content randomly generated

if response.status_code == 200:
    #getting the current date and time

    today_date = date.today();
    tday = date.today().day;
    quotes = response.json()[0];
    quote = quotes['q']
    author = quotes['a']

    print(f'"{quote}" \n- {author}') # prints the quote based on the number representing the day
    print("success");

elif response.status_code == 404:
    print("Not found")
#print(response.text)

#Next Step 
    #figure out getting my key to allow filtering the quotes
    #figure out a way to only show one quote every day
        #-> how to get one quote at a time
        #-> how to get them to display every day 



