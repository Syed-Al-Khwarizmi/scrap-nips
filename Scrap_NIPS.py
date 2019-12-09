#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import urllib
from urllib.request import urlopen
import lxml.html
import requests


# In[ ]:


def getSubLinks(url):
    sublinks = []
    connection = urlopen(url)
    dom = lxml.html.fromstring(connection.read())
    for link in dom.xpath('//a/@href'):
        if not link.startswith('https'):
            sublinks.append(url+link)
        else:
            sublinks.append(link)
    return sublinks


# In[ ]:


def download_file(download_url):
    response = urlopen(download_url)
    file = open("NIPS Papers/{}".format(download_url.split('/')[-1]), 'wb')
    file.write(response.read())
    file.close()
    print("{} Downloaded".format(download_url.split('/')[-1]))


# In[ ]:


def filterPapers():
    NIPS_main = getSubLinks('https://papers.nips.cc')
    NIPS_main = [x for x in NIPS_main if ('https://papers.nips.cc/book/' in x)]
    outer_list = []
    for x in NIPS_main:
        print(x)
        filtered_pings = getSubLinks(x)
        to_remove = filtered_pings[0].split('/')[4]
        filtered_pings = [x.replace('/{}/'.format(to_remove), '') for x in filtered_pings]
        filtered_pings = [x.replace('book', '') for x in filtered_pings]
        outer_list.append(filtered_pings)
        
    return outer_list


# In[ ]:


papers = filterPapers()


# In[ ]:


papers = [paper for sublist in papers for paper in sublist if '/paper/' in paper]


# In[ ]:


papers = ['{}.pdf'.format(x) for x in papers]


# In[ ]:


for p in papers:
    download_file(p)

