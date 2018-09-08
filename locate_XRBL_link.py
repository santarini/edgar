from bs4 import BeautifulSoup as bs
import requests
import sys

# Company Data and Document Type
ticker = 'msft'
typeQuerry = '10-K'

# Obtain HTML for search page
baseURL = "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={}&type={}"
response = requests.get(baseURL.format(ticker, typeQuerry))
responseText = response.text

# Find filing detail link
soup = bs(responseText, 'html.parser')
table = soup.find('table', class_='tableFile2')
firstRow = table.findAll('tr')[1]
firstAnchor = firstRow.find('a')
filingDetailLink = 'https://www.sec.gov' + firstAnchor.get("href")

# Obtain HTML for document page
response = requests.get(filingDetailLink)
responseText = response.text

# Find the XBRL link
soup = bs(responseText, 'html.parser')
table = soup.find('table', class_='tableFile', summary='Data Files')
firstRow = table.find_all('tr')[1]
firstAnchor = firstRow.find('a')
XBRL_link = 'https://www.sec.gov' + firstAnchor.get("href")

print(XBRL_link)
