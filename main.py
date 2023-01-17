#!/usr/bin/env python3
from utils.getter import *
from utils.wrapper import *
from utils.parser import *
from utils.container import *
from utils.writter import *
from utils.currency_converter import *
from utils.classifier import *
import re
from tqdm import tqdm
import pprint


css_class = ("prd_link-product-name", "prd_link-product-price") # product name, product price
div_class = "css-974ipl" # divs pointing to a href => links location

total_objects = []
items_from_excel = loadXlsx("DAFTAR HARGA ATK 2023.xlsx", "NAMA BARANG", 1)
LEN_TOTAL = len(items_from_excel)
# LEN_TOTAL = 7
item_lost = []
counter = 0
for item in tqdm(items_from_excel[:LEN_TOTAL], total=len(items_from_excel[:LEN_TOTAL])):
    obj_list = findPriceWrapper(item, getDataWithRequests, css_class, div_class)
    if (len(obj_list) == 0):
        item_lost.append(item)
        counter += 1
    total_objects.append(obj_list)

print(f"Number of items that are lost: {counter}")
print(f"Item(s) that are lost: {item_lost}")

# list_to_write = [[items_from_excel[i]] + j for i, v in enumerate(formatted_list) for j in v] # list comprehension for expressions below

# for i, v in enumerate(formatted_list):
    # for j in v:
        # list_to_write.append([items_from_excel[i]] + j)
# writeToXlsx(list_to_write)
# print(flattener(container(findPriceWrapper("tinta brother BT6000 BK", getDataWithRequests, css_class, div_class))))


# to do:
# find a way to present values in meaningful way (probably putting data into xlsx) -> done
# find a way to make requests faster -> async -> partially done
# remove ads from tokopedia => ignore: span.css-1gohnec -> done
# removing confusion from seeing the price visualization -> median from top rated stores
#   split items as classes: from classes find the median value: return median value with index corresponding the array element

# make a web/desktop app that can be accessed from the internet