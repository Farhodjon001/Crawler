#!/usr/bin/env/ python
import requests

def request(url):
    try:
        return requests.get("http://"+url)

    except requests.exceptions.ConnectionError:
        pass
target_url=("asilmedia.org")

with open("subdomen.lst","r")  as wordlist:
    for line in wordlist:
        word=line.strip()
        test_url=word +"."+target_url
        response=request(test_url)
        if response:
            print("Topildi--> "+test_url)
