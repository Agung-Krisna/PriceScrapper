from threading import Thread
import requests
from requests.utils import requote_uri

threads = []
result_list = []

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}
def getDataWithRequests(result_list, url):
    result_list.append(requests.get(url, headers=header).text)
def thread_request(url_list):
    for url in url_list:
        thread = Thread(target=getDataWithRequests, args=(result_list, url))
        thread.start()
        threads.append(thread)

def little_wrapper(query_list):
    target = [requote_uri(f'https://www.tokopedia.com/search?q={query}') for query in query_list]
    thread_request(target)
    for thread in threads:
        thread.join()
    return result_list