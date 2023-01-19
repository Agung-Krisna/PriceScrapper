from bs4 import BeautifulSoup as bs
import re

def parseWithCssClass(rendered_html, css_class):
    soup = bs(rendered_html, 'html.parser')
    return soup.find_all(class_=css_class)

def parseFromInsideDiv(rendered_html, div_class):
    soup = bs(rendered_html, 'html.parser')
    divs = soup.find_all(class_=div_class)
    links = []
    for div in divs:
        links.append(div.a["href"])
    return links

def deleteTokopediaAds(obj_list):
    obj_to_delete = [obj for obj in obj_list if re.search(r"^https://ta.tokopedia.com", obj.item_link)]
    obj_to_return = [obj for obj in obj_list if obj not in obj_to_delete]
    return obj_to_return