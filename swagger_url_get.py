from asyncio.windows_events import NULL
import string
import requests
from sqlalchemy import false
import json
import sys
import urllib3
from urllib.parse import urlparse
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_path(url):
    r = requests.get(url,verify=False)
    json_data = json.loads(r.text)
    path_data = json_data["paths"].keys()
    url = urlparse(url).scheme + '://' + urlparse(url).netloc
    for i in path_data:
        print(url+i)
    #return path_data

# def get_data(url):
#     path_data = get_path(url)
#     url = urlparse(url).scheme + '://' + urlparse(url).netloc
#     for i in path_data:
#         r = requests.get(url+i,verify=False)
#         print(url + str(i) + '\tcode：' + str(r.status_code) + '\tsize: ' + str(len(r.text)))


if __name__ == '__main__':
    if(len(sys.argv) <= 1):
        print('example： python swagger_url_get.py http://xxx/v2/api-docs')
        exit(0)
    else:
        get_path(sys.argv[1])
