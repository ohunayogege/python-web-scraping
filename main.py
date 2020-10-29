from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import lxml
import validators
from connection import connect


if not connect():
  print('You are not connected to the internet.')
else:
  url = 'https://facebook.com'
  req = Request(url)
  html_page = urlopen(req)

  soup = BeautifulSoup(html_page, "lxml")
  links = []
  new_link = []
  for link in soup.findAll('a'):
    a = link.get('href')
    valid=validators.url(a)
    if valid==True:
      url2 = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', a)
      b = url2[0]
      req2 = Request(b)
      html_page2 = urlopen(req2)
      soup2 = BeautifulSoup(html_page2, "lxml")
      if soup2.title:
        title = soup2.title.string
      else:
        title = "No Title for this page"
      data = {
        'title': title,
        'url': b
      }
      new_link.append(data)
  print(new_link)
