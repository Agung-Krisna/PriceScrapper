from .parser import *
from .container import *
from .classifier import *
from threading import Thread
from .thread_request import little_wrapper

def findPriceWrapper(query: str, get_function: callable, css_class: str, div_class: str) -> str: # type hints so that I won't forget which parameter takes a function
    html = get_function(query)
    data = []
    temp_values = []
    obj_list = []
    for a_class in css_class:
        data.append(parseWithCssClass(html, a_class))
    links = (parseFromInsideDiv(html, div_class))
    for div in data:
        lst = []
        for element in div:
            lst.append(element.string)
        temp_values.append(lst)
    flattened = flattener(container((temp_values, links)))
    for item in flattened:
        obj = TokopediaItems(query, item[0], item[1], item[2])
        obj_list.append(obj)
    return deleteTokopediaAds(obj_list)

def asyncFindPriceWrapper(query_list: str, css_class: str, div_class: str) -> str:
    result_list = little_wrapper(query_list)
    data = []
    for html in result_list:
        for a_class in css_class:
            data.append(parseWithCssClass(html, css_class))
    return data