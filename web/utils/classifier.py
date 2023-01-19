class TokopediaItems():
    def __init__(self, keyword = None, item_desc = None, item_price = None, item_link = None):
        self.keyword = keyword
        self.item_desc = item_desc
        self.item_price = item_price
        self.item_link = item_link
        self.converted_price = self.convertPriceToInt()
    def convertPriceToInt(self):
        price = self.item_price
        price = price.replace("Rp", "")
        price = price.replace(".", "")
        return int(price)
    def __str__(self):
        return (f"Keyword: {self.keyword}, Item Description: {self.item_desc}, Item Price: {self.item_price}, Item Link: {self.item_link}")