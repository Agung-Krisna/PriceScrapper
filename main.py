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
from statistics import mean, median, mode


css_class = ("prd_link-product-name", "prd_link-product-price") # product name, product price
div_class = "css-974ipl" # divs pointing to a href => links location

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