#!/usr/bin/env/ python
import requests
import re
# from urllib.parse import urljoin

import urlparse

target_url="http://10.0.2.6/mutillidae/"
target_links=[]

def extract_links_from(url):
    response=requests.get(url)
    # print(response.content)
    return re.findall(b'(?:href=")(.*?)"',response.content)

def crawl(url):
    href_links=extract_links_from(url)
    for link in href_links:
        link=urlparse.urljoin(url,link)
        if "#" in link:
            link=link.split("#")[0]

        if target_url in link and link not in target_links:
            target_links.append(link)
            print(link)
            crawl(link)


crawl(target_url)


