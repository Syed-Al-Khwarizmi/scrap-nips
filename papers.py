import urllib
from lxml import html
from urllib.request import urlopen
import requests

class Papers:
    def __init__(self):
        self.URL_PAPERS = "https://papers.nips.cc"
        self.URL_PAPERS_BOOK = "https://papers.nips.cc/book/"
    
    def get(self, url):
        connection = urlopen(url)
        dom = html.fromstring(connection.read())
        return list(map(lambda link: url+link if not link.startswith('https') else link, dom.xpath('//a/@href')))
    
    def download(self, download_url):
        response = urlopen(download_url)
        file = open("NIPS Papers/{}".format(download_url.split('/')[-1]), 'wb')
        file.write(response.read())
        file.close()
        print("{} Downloaded".format(download_url.split('/')[-1]))
        return None
    
    def filter(self):
        NIPS_main = self.get(self.URL_PAPERS)
        NIPS_main = [x for x in NIPS_main if (self.URL_PAPERS_BOOK in x)]
        outer_list = []
        for x in NIPS_main:
            print(x)
            filtered_pings = self.get(x)
            to_remove = filtered_pings[0].split('/')[4]
            filtered_pings = [x.replace('/{}/'.format(to_remove), '') for x in filtered_pings]
            filtered_pings = [x.replace('book', '') for x in filtered_pings]
            outer_list.append(filtered_pings)

        return outer_list
