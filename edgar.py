from bs4 import BeautifulSoup
import requests
import sys

# Obtain XBRL text from document
xbrl_resp = requests.get('https://www.sec.gov/Archives/edgar/data/1652044/000165204418000027/goog-20180630.xml')
xbrl_str = xbrl_resp.text

# Find and print stockholder's equity
soup = BeautifulSoup(xbrl_str, 'lxml')
tag_list = soup.find_all()
for tag in tag_list:
    if tag.name == 'us-gaap:stockholdersequity':
        print("Stockholder's equity: " + tag.text)
