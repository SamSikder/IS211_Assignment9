import requests
from bs4 import BeautifulSoup

# URL for CBS NFL Stats - Touchdowns
url = "https://www.cbssports.com/nfl/stats/"

# Send request to fetch the page content
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(response.text, 'html.parser')

# Find the section containing touchdown stats
table = soup.find('table')

if table:
    rows = table.find_all('tr')[1:21]  # Get top 20 players

    print("Top 20 NFL Players by Touchdowns:")
    for row in rows:
        columns = row.find_all('td')
        if len(columns) >= 4:
            player = columns[0].text.strip()
            position = columns[1].text.strip()
            team = columns[2].text.strip()
            touchdowns = columns[3].text.strip()
            print(f"{player} ({position}) - {team}: {touchdowns} TDs")
else:
    print("Table not found. The website structure may have changed.")