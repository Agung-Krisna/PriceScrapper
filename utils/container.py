#!/usr/bin/env python3
from utils.parser import deleteTokopediaAds
def container(items):
    item1, item2 = items[0]
    item3 = items[1]
    item_pair = list(zip(item1, item2))
    item_link = item3
    max_ = deleteTokopediaAds(item_link)
    item_pair = item_pair[max_ + 1:]
    item_link = item_link[max_ + 1:]
    return list(zip(item_pair, item_link))