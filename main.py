#!/usr/bin/env python3

import time
from utils.getter import *
from utils.wrapper import *
from utils.parser import *
from utils.container import *
import re
from tqdm import tqdm

css_class = ("prd_link-product-name", "prd_link-product-price") # product name, product price
div_class = "css-974ipl" # divs pointing to a href => links location

mega_list = []

# items_from_excel = loadXlsx("DAFTAR HARGA ATK 2023.xlsx", "NAMA BARANG", 1)
# for item in tqdm(items_from_excel[:5], total=len(items_from_excel[:5])):
    # item_pair = container(findPriceWrapper(item, getDataWithRequests, css_class, div_class))
    # mega_list.append(item_pair)


# new_data = list(mega_list[0])

# new_data.append(mega_list[1])

example_list =[(('Termurah ! Kertas Fotocopy Pint HVS A4 Sinar Dunia SIDU 70 gr Rim', 'Rp43.500'), 'https://www.tokopedia.com/mr12office/termurah-kertas-fotocopy-pint-hvs-a4-sinar-dunia-sidu-70-gr-rim?extParam=ivf%3Dfalse%26src%3Dsearch'), (('Kertas HVS Sidu Sinar Dunia A4 70 / 75 gram ( 5 rim ) GOJEK / GRAB', 'Rp220.000'), 'https://www.tokopedia.com/travis189/kertas-hvs-sidu-sinar-dunia-a4-70-75-gram-5-rim-gojek-grab?extParam=ivf%3Dfalse%26src%3Dsearch'), (('[Grab/Gojek] Kertas Fotocopy Print HVS A4 70g Sinar Dunia SIDU Box Dus', 'Rp217.500'), 'https://www.tokopedia.com/mr12office/grab-gojek-kertas-fotocopy-print-hvs-a4-70g-sinar-dunia-sidu-box-dus?extParam=ivf%3Dfalse%26src%3Dsearch'), (('Kertas HVS Sinar Dunia SIDU A4 70gr', 'Rp41.000'), 'https://www.tokopedia.com/tintatonerink/kertas-hvs-sinar-dunia-sidu-a4-70gr?extParam=ivf%3Dfalse%26src%3Dsearch'), (('Kertas HVS A4 70 Gram Sinar Dunia Sidu / rim - Kertas Fotocopy 70gram', 'Rp48.000'), 'https://www.tokopedia.com/royalatkmlg/kertas-hvs-a4-70-gram-sinar-dunia-sidu-rim-kertas-fotocopy-70gram?extParam=ivf%3Dfalse%26src%3Dsearch'), [(('kertas hvs warna F4 70gr Sidu Sinar Dunia', 'Rp60.000'), 'https://www.tokopedia.com/tintatonerink/kertas-hvs-warna-f4-70gr-sidu-sinar-dunia-merah-muda?extParam=ivf%3Dfalse%26src%3Dsearch&refined=true'), (('Sinar Dunia Kertas HVS Fotocopy Cetak 70gr A4 F4 Folio', 'Rp48.800'), 'https://www.tokopedia.com/jayamediamlg/sinar-dunia-kertas-hvs-fotocopy-cetak-70gr-a4-f4-folio-a4s?extParam=ivf%3Dfalse%26src%3Dsearch&refined=true'), (('kertas hvs F4 (folio) sinar dunia /sidu 70gr', 'Rp55.500'), 'https://www.tokopedia.com/anekajayasby/kertas-hvs-f4-folio-sinar-dunia-sidu-70gr?extParam=ivf%3Dfalse%26src%3Dsearch&refined=true'), (('Kertas HVS Sinar Dunia ( SiDu ) F4 70 gr 1 dus / 5 Rim', 'Rp242.900'), 'https://www.tokopedia.com/inkoriginal/kertas-hvs-sinar-dunia-sidu-f4-70-gr-1-dus-5-rim?extParam=ivf%3Dfalse%26src%3Dsearch&refined=true'), (('Kertas HVS Sinar Dunia SIDU F4 70 Gram', 'Rp57.500'), 'https://www.tokopedia.com/groceranstation/kertas-hvs-sinar-dunia-sidu-f4-70-gram?extParam=ivf%3Dfalse%26src%3Dsearch&refined=true')]]
# print(list(example_list[1][0]).append(example_list[1][1]))
# arrs = example_list[0][0][0], example_list[0][0][1], example_list[0][1]


res = [(a, b) for a, b in example_list]
print(res)  
# print(example_list[0][0][1])



# to do:
# find a way to present values in meaningful way (probably putting data into xlsx)
# find a way to make requests faster
# remove ads from tokopedia => ignore: span.css-1gohnec
# add support to blibli
# make a web/desktop app that 