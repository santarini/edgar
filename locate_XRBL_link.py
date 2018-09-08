from bs4 import BeautifulSoup
import requests
import sys

# Access page
cik = '0001652044'
typeQuerry = '10-K'

# Obtain HTML for search page
base_url = "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={}&type={}"
edgar_resp = requests.get(base_url.format(cik, typeQuerry))
edgar_str = edgar_resp.text

# Find the document link
doc_link = ''
soup = BeautifulSoup(edgar_str, 'html.parser')
table_tag = soup.find('table', class_='tableFile2')
firstRow = table_tag.findAll('tr')[2]
firstAnchor = firstRow.find('a')
filingDetailLink = 'https://www.sec.gov' + firstAnchor.get("href")

# Obtain HTML for document page
doc_resp = requests.get(filingDetailLink)
doc_str = doc_resp.text


# Find the XBRL link
soup = BeautifulSoup(doc_str, 'html.parser')
table_tag = soup.find('table', class_='tableFile', summary='Data Files')
firstRow = table_tag.find_all('tr')[1]
firstAnchor = firstRow.find('a')
xbrl_link = 'https://www.sec.gov' + firstAnchor.get("href")

print(xbrl_link)
