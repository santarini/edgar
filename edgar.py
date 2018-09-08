from bs4 import BeautifulSoup
import requests
import sys

# Obtain XBRL text from document
response = requests.get('https://www.sec.gov/Archives/edgar/data/1652044/000165204418000027/goog-20180630.xml')
responseText = response.text

# Find and print stockholder's equity
soup = BeautifulSoup(responseText, 'lxml')
tagList = soup.findAll()
for tag in tagList:
    if tag.name == 'us-gaap:stockholdersequity':
        print("Stockholder's equity: " + tag.text)
        #print("Stockholder's equity: " + tag["contextRef"])
