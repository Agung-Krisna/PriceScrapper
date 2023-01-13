from openpyxl import Workbook
from itertools import chain

def writeToXlsx(query, data):
    # workbook = Workbook()
    # worksheet = workbook.active
    res = list(chain.from_iterable(i if insinstance(i, tuple) else [i] for i in data))
    print(res)