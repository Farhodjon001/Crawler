#!/usr/bin/env/ python
import urllib.parse

import requests
from bs4 import BeautifulSoup

def request(url):
    try:
        return requests.get(url)

    except requests.exceptions.ConnectionError:
        pass
target_url="http://10.0.2.6/mutillidae/index.php?page=dns-lookup.php"
response=request(target_url)
parsed_html=BeautifulSoup(response.content,'html.parser')
forms_list=parsed_html.find_all("form")
print(forms_list)

for form in forms_list:
    action = form.get("action")
    post_url = urllib.parse.urljoin(target_url,action)
    print(post_url)
    method = form.get("method")

    inputs_list = form.find_all("input")
    post_data = {}
    for input in inputs_list:
        input_name=input.get("name")
        input_type=input.get("type")
        input_value=input.get("value")
        if input_type=="text":
            input_value="test"


        post_data[input_name]=input_value
    result=requests.post(post_url,data=post_data)
    print(result.content)