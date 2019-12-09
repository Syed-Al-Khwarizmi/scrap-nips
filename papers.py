import urllib
from lxml import html
from urllib.request import urlopen
import requests

class Papers:
    def __init__(self):
        pass
    
    def get(self, url):
        sublinks = []
        connection = urlopen(url)
        dom = html.fromstring(connection.read())
        for link in dom.xpath('//a/@href'):
            if not link.startswith('https'):
                sublinks.append(url+link)
            else:
                sublinks.append(link)
        return sublinks
    
    def download(self, download_url):
        response = urlopen(download_url)
        file = open("NIPS Papers/{}".format(download_url.split('/')[-1]), 'wb')
        file.write(response.read())
        file.close()
        print("{} Downloaded".format(download_url.split('/')[-1]))
        return None
    
    def filter(self):
        NIPS_main = self.get('https://papers.nips.cc')
        NIPS_main = [x for x in NIPS_main if ('https://papers.nips.cc/book/' in x)]
        outer_list = []
        for x in NIPS_main:
            print(x)
            filtered_pings = self.get(x)
            to_remove = filtered_pings[0].split('/')[4]
            filtered_pings = [x.replace('/{}/'.format(to_remove), '') for x in filtered_pings]
            filtered_pings = [x.replace('book', '') for x in filtered_pings]
            outer_list.append(filtered_pings)
            
        return outer_list
