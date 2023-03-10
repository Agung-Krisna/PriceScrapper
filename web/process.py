#!/usr/bin/env python3
from utils.getter import *
from utils.wrapper import *
from utils.parser import *
from utils.container import *
from utils.writter import *
from utils.currency_converter import *
from utils.classifier import *
from uuid import uuid4
import aiohttp
import asyncio
import os




css_class = ("prd_link-product-name", "prd_link-product-price") # product name, product price
div_class = "css-974ipl" # divs pointing to a href => links location

def processFile(filepath, dict_to_return):
    total_objects_list = []
    items_from_excel = loadXlsx(filepath, "NAMA BARANG")
    LEN_TOTAL = len(items_from_excel)
    item_lost = []
    counter = 0
    for item in items_from_excel[:LEN_TOTAL]:
        if not (isinstance(item, str)):
            continue
        obj_list = findPriceWrapper(item, getDataWithRequests, css_class, div_class)
        if (len(obj_list) == 0):
            item_lost.append(item)
            counter += 1
        total_objects_list.append(obj_list)
    
    est_price = 0
    final_objects = []
    for obj_list in total_objects_list:
        if (len(obj_list) != 0):
            obj = findThirdQuartile(obj_list)# Third quartile is good
            est_price += obj.converted_price
            final_objects.append([obj.keyword, obj.item_desc, obj.item_price, obj.item_link])

    final_objects.append(["", "Harga Total", str(est_price), ""])
    # uuid = uuid4()
    # writeToXlsx(final_objects, f"results/{uuid}.xlsx")
    writeToXlsx(final_objects, "results/result.xlsx")

    if (counter > 0):
        print(f"Number of items that are lost: {counter}")
        print(f"Item(s) that are lost: {item_lost}")
    
    dict_to_return["number-item-lost"] = counter
    dict_to_return["items-lost"] = item_lost
    # dict_to_return["uuid"] = uuid

    # removing the filepath
    os.remove(filepath)

