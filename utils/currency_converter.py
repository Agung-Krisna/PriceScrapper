from statistics import median

# preprocessing

def findWrapper(obj_list: list, filter_method: callable):
    obj_price_list = [obj.converted_price for obj in obj_list]
    filter_result = filter_method(obj_price_list)
    result = []
    for obj in obj_list:
        if (obj.converted_price == filter_result):
            result.append(obj)
    try:
        return result[0]
    except: 
        return []


def findMedian(obj_list):
    obj_price_list = [obj.converted_price for obj in obj_list]
    med = median(obj_price_list)
    result = []
    for obj in obj_list:
        if (obj.converted_price == med):
            result.append(obj)
    if (len(result) == 1):
        return result[0]
    else:
        return result

def findThirdQuartile(obj_list):
    obj_price_list = [obj.converted_price for obj in obj_list]
    obj_price_list.sort()
    half_len = len(obj_price_list) // 2
    try:
        upper_quartile = obj_price_list[half_len:][len(obj_price_list[half_len:]) // 2] # half of lower half
    except IndexError:
        upper_quartile = obj_price_list[-1]
    try:
        lower_quartile = obj_price_list[:half_len][len(obj_price_list[:half_len]) // 2] # half of upper half
    except IndexError:
        lower_quartile = obj_price_list[0]
    
    for obj in obj_list:
        if(obj.converted_price == upper_quartile and type(obj) is not None):            
            return obj