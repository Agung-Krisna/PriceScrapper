from statistics import median

# preprocessing

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
    # return obj_price_dict[median(obj_price_dict.keys())]

    

def findMaximum(tag, prices):
    return tag, max(prices)