import pandas as pd
import requests
from requests.utils import requote_uri
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import random
import asyncio

USER_AGENTS = open("useragent.txt", 'r').readlines()

def loadXlsx(filepath, column_name, sheet_num=0):
    xls = pd.ExcelFile(r"{}".format(filepath)) # opening excelfile
    sheet = xls.parse(sheet_num) # getting the first sheet
    item_name = sheet[column_name] # gettting the column name
    return item_name.dropna()


def getDataWithRequests(query): # preferred method, a lot faster than selenium
    query_data = requote_uri(f"https://www.tokopedia.com/search?q={query}") # q=query, ob=order by, rt=rating
    html = None
    while html is None:
        try:
            headers = {"User-Agent": random.choice(USER_AGENTS).replace("\n", "")}
            html = requests.get(query_data, headers=headers, timeout=1).text
        except Exception as e:
            continue
    return html
def getDataWithSelenium(query, order_by="high"): # use selenium when really needed
    headless = Options()
    headless.headless = True # comment to use headful (GUI) browser
    driver = webdriver.Firefox(options=headless)

    if order_by == "high":
        query_data = requote_uri(f"https://www.tokopedia.com/search?q={query}&ob=4")
    else: 
        query_data = requote_uri(f"https://www.tokopedia.com/search?q={query}")
    driver.get(query_data)
    html = driver.find_element(By.TAG_NAME, "html").get_attribute("innerHTML")
    driver.close()
    return html