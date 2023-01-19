from openpyxl import Workbook

def writeToXlsx(data, item_name = "report.xlsx"):
    wb = Workbook()
    ws = wb.active
    INFO = ["Nama Pencarian", "Hasil Pencarian", "Harga Barang", "Link Toko"]
    ws.append(INFO)
    for datum in data: 
        ws.append(datum)
    wb.save(item_name)