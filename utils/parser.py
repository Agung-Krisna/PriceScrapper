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

def deleteTokopediaAds(links):
    max_ = 0
    for index, val in enumerate(links):
        if (re.search(r"^https://ta.tokopedia.com*", val)): # ads, skewing results 
            if index > max_:
                max_ = index    
    return max_