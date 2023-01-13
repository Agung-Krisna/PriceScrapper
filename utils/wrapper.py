from .parser import *

def findPriceWrapper(query: str, get_function: callable, css_class: str, div_class: str) -> str: # type hints so that I won't forget which parameter takes a function
    html = get_function(query)
    data = []
    for a_class in css_class:
        data.append(parseWithCssClass(html, a_class))
    links = (parseFromInsideDiv(html, div_class))
    temp_values = []
    for div in data:
        lst = []
        for element in div:
            lst.append(element.string)
        temp_values.append(lst)
    return temp_values, links
