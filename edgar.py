#! python 3
#from xbrl import XBRLParser, GAAP, GAAPSerializer
import requests
#from xml.etree import ElementTree
import bs4 as bs

response = requests.get('https://www.sec.gov/Archives/edgar/data/1652044/000165204418000027/goog-20180630.xml')
edgar_str = response.text

print(edgar_str)


##soup = bs.BeautifulSoup(response.text, 'lxml')
##yearTable = soup.find('dei:DocumentFiscalPeriodFocus')
##print(yearTable)
### contextRef
#xbrl_parser = XBRLParser()
#xbrl = xbrl_parser.parse(file(response))
