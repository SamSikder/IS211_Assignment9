import requests
from bs4 import BeautifulSoup

# URL for Apple Stock Data
url = "https://finance.yahoo.com/quote/AAPL/history?p=AAPL"

# Send request to fetch the page content
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table containing the data
table = soup.find('table')

if table:
    rows = table.find_all('tr')[1:]  # Skip header row

    print("Apple Stock Prices:")
    for row in rows:
        columns = row.find_all('td')
        if len(columns) >= 6:
            date = columns[0].text.strip()
            close_price = columns[4].text.strip()
            print(f"Date: {date}, Close Price: {close_price}")
else:
    print("Table not found. The website structure may have changed.")