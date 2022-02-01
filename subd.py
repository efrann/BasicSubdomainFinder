from ast import parse
from email.utils import parsedate
from urllib import request
import requests
import sys
import argparse

parser = argparse.ArgumentParser(description="Subdomain Finder")
parser.add_argument("-url", dest="url", help="Enter the url", required=True)
parser.add_argument("-i", dest="keywordfile", help="Enter the keyword file", required=True)
parsed_args = parser.parse_args()

basarisiz = 0
basarili = 0

with open(parsed_args.keywordfile) as file:
    for subs in file:
        subs = subs.strip()
        url_to_check = f"http://{subs}.{parsed_args.url}"

        try:
            requests.get(url_to_check)
    
        except requests.ConnectionError:
            basarisiz = basarisiz + 1
            pass

        else:
            print("Valid domain: ",url_to_check)
            basarili = basarili + 1


'''
sublist = open("keywords.txt").read()
%subs = sublist.splitlines()

%for sub in subs:
    url_to_check = f"http://{sub}.{sys.argv[1]}"

    try:
        requests.get(url_to_check)
    
    except requests.ConnectionError:
        basarisiz = basarisiz + 1
        pass

    else:
        print("Valid domain: ",url_to_check)
        basarili = basarili + 1
'''


print("Sonuc: \n"+ str(basarili) + "adet basarili" +
            "\n" + str(basarisiz) + "adet basarisiz")
