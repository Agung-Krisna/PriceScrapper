#!/usr/bin/env python3
from utils.getter import *
from utils.wrapper import *
from utils.parser import *
from utils.container import *
from utils.writter import *
from utils.currency_converter import *
from utils.classifier import *
from utils.connecter_to_db import *
import re
from tqdm import tqdm
import pprint
import aiohttp
import asyncio
from aiohttp_requests import requests
from statistics import mean, median, mode
from utils.thread_request import little_wrapper
import time
css_class = ("prd_link-product-name", "prd_link-product-price") # product name, product price
div_class = "css-974ipl" # divs pointing to a href => links location

def finalFunction():
    total_objects_list = []
    items_from_excel = loadXlsx("DAFTAR HARGA ATK 2023.xlsx", "NAMA BARANG", 1)
    LEN_TOTAL = len(items_from_excel)
    # LEN_TOTAL = 3
    item_lost = []
    counter = 0
    for item in tqdm(items_from_excel[:LEN_TOTAL], total=len(items_from_excel[:LEN_TOTAL])):
        obj_list = findPriceWrapper(item, getDataWithRequests, css_class, div_class)
        if (len(obj_list) == 0):
            item_lost.append(item)
            counter += 1
        total_objects_list.append(obj_list)

    if (counter > 0):
        print(f"Number of items that are lost: {counter}")
        print(f"Item(s) that are lost: {item_lost}")


    est_price = 0
    final_objects = []
    for obj_list in total_objects_list:
        if (len(obj_list) != 0):
            obj = findThirdQuartile(obj_list)# Third quartile is good
            est_price += obj.converted_price
            final_objects.append([obj.keyword, obj.item_desc, obj.item_price, obj.item_link])
    writeToXlsx(final_objects, "third_quartile3.xlsx")


USER_AGENTS = open("useragent.txt", "r").readlines()

async def getDataWithAiohttp(session, url):
    html = None
    while html is None:
        try:
            user_agent = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}
            async with session.get(url, headers=user_agent) as resp:
                html = await resp.json()
        except Exception as e:   
            continue
    return html


async def getDataWithAioWrapper(query):
    query_data = requote_uri(f"https://www.tokopedia.com/search?q={query}")
    html = None
    while html is None:
        try:
            header = {
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "sec-ch-ua": "\".Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"103\", \"Chromium\";v=\"103\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Linux\"",
            "sec-fetch-site": "none",
            "sec-fetch-mod": "",
            "sec-fetch-user": "?1",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "fr-CH,fr;q=0.9,en-US;q=0.8,en;q=0.7"}
            async with requests.get(url, headers=header) as resp:
                html = await resp.text()
        except Exception as e:   
            continue
    return html


async def main(query_list):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for query in tqdm(query_list):
            url = requote_uri(f"https://www.tokopedia.com/search?q={query}")
            tasks.append(asyncio.ensure_future(getDataWithAiohttp(session, url)))

        returned_list = await asyncio.gather(*tasks)
        for item in returned_list:
            print(item)

items_from_excel = loadXlsx("DAFTAR HARGA ATK 2023.xlsx", "NAMA BARANG", 1)
def asyncProcessMain():
    asyncFindPriceWrapper(items_from_excel, css_class, div_class)
def processMain():
    # print(items_from_excel)
    for query in items_from_excel:
        asyncio.run(getDataWithAioWrapper(query))
    #  asyncio.run(getDataWithAioWrapper(items_from_excel[0]))

asyncio.run(processMain())

start = time.time()
print(asyncProcessMain())
print("Time required", round(time.time() - start, 2))

start = time.time()
finalFunction()
print("Time required", round(time.time() - start, 2))

# # keywords = ["bola dunia hvs 70 gsm a4", "epson stylus t6642", "epson stylus t6644", "epson stylus t6641", "epson stylus t6643", "epson stylus 003", "isi cutter besar joyko l-150"]
# keywords = ["bola dunia hvs 70 gsm a4"]
# # est_price = 0
# # for keyword in keywords:
    # # lst = findPriceWrapper(keyword, getDataWithRequests, css_class, div_class)
    # # obj_mode = findWrapper(lst, mode)
    # # obj_max = findWrapper(lst, max)
    # # obj_quartile = findThirdQuartile(lst)
    # # print("Mode =", obj_mode.item_desc, obj_mode.item_price)
    # # print("Max =", obj_max.item_desc, obj_max.item_price)
    # # print("Third Quartile = ", obj_quartile.item_desc, obj_quartile.item_price)
    # # est_price += obj_quartile.converted_price

# # print(est_price) # original price 449K and estimated price is 469K, we did a good job by using mode, however there are instances where it lead to loses in profit
                # third quartile produces 491K
# to do:
# find a way to present values in meaningful way (probably putting data into xlsx) -> done
# find a way to make requests faster -> async -> partially done
# remove ads from tokopedia => ignore: span.css-1gohnec -> done
# removing confusion from seeing the price visualization -> median from top rated stores -> done
#   split items as classes: from classes find the median value: return median value with index corresponding the array element -> done
# make a web/desktop app that can be accessed from the internet