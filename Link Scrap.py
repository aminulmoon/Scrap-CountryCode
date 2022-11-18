from csv import writer
from requests import get
from bs4 import BeautifulSoup as bs

url = 'https://countrycode.org'

res = get(url)
soup = bs(res.text, 'html.parser')
table_body = soup.find('tbody')


link_list = []
for links in table_body.find_all('a', href=True):
    link_list.append(url + links['href'])

file = open('Country Links.csv', 'a+')
for link in link_list:
        file.write(f"{link}\n")
file.close()
