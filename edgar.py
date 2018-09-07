import os
import requests
import bs4 as bs
import csv
import re

response = requests.get('https://www.sec.gov/Archives/edgar/data/1652044/000165204418000027/goog-20180630.xml')
soup = bs.BeautifulSoup(response.text, 'lxml')
yearTable = soup.find('dei:DocumentFiscalPeriodFocus')
print(
# contextRef
