import simplejson as json
import urllib
from datetime import datetime

def get_single_data(ASIN):
    url = 'http://112.124.1.3:8004/api/commodity/' + ASIN
    return json.loads(urllib.urlopen(url).read())

def get_single_price(dict):
    sum = 0.0
    num = 0
    avgPrice = []
    time = []
    maxPrice = []
    minPrice = []
    
    if dict['offer']:
        for each_time_offer in dict['offer']:
            if each_time_offer['info']:
                time.append(datetime.strptime(each_time_offer['timestamp'],'%Y-%m-%d %H:%M:%S'))
                max = each_time_offer['info'][0]['price']
                min = each_time_offer['info'][0]['price']
                for each_seller_offer in each_time_offer['info']:
                    single_price = each_seller_offer['price']
                    
                    if (isinstance(single_price,float)) or (isinstance(single_price,int)):
                        sum  = sum + single_price
                        if single_price > max:
                            max = single_price
                        if single_price < min:
                            min = single_price                
                    else:
                        length = single_price.split('$')
                        trans_price = (float)(length[1])
                        if trans_price > max:
                            max = trans_price
                        if trans_price < min:
                            min = trans_price 
                        sum = sum + trans_price
                    num = num + 1
                maxPrice.append(max)
                minPrice.append(min)
                avg_price = sum / num
                avgPrice.append(round(avg_price,3))
                sum = 0.0
                num = 0
        
        avg_time_list = group_by_time(time,avgPrice)
        max_time_list = group_by_time(time,maxPrice)
        min_time_list = group_by_time(time,minPrice)
        
        list_of_three = []
        list_of_three.append(max_time_list)
        list_of_three.append(avg_time_list)
        list_of_three.append(min_time_list)
        
        return list_of_three     
    else:
        return []
    
def group_by_time(time,list):
    k = 0
    dict = {}
    for single_date in time:
        if dict.has_key(int(single_date.strftime('%Y%m%d'))):
            dict[int(single_date.strftime('%Y%m%d'))][0] = dict[int(single_date.strftime('%Y%m%d'))][0] + list[k]
            dict[int(single_date.strftime('%Y%m%d'))][1] = dict[int(single_date.strftime('%Y%m%d'))][1] + 1
        else:
            dict[int(single_date.strftime('%Y%m%d'))] = [list[k],1]
        k = k + 1
        
    for ele in dict:
        dict[ele] = (dict[ele][0])/(dict[ele][1])
        
    price_time_list = sorted(dict.iteritems(), key=lambda x:x[0])
    return price_time_list

def function1(ASIN):
    dict = get_single_data(ASIN)
    list_of_three = get_single_price(dict)   
    return_list = []  #first:date,second:max,third:avg,forth:min
    date_list = [] 
    
    max_time_list = list_of_three[0]
    avg_time_list = list_of_three[1]
    min_time_list = list_of_three[2]
    
    
    max_price_data = map(lambda x:x[1], max_time_list)
    min_price_data = map(lambda x:x[1], min_time_list)
    avg_price_data = map(lambda x:x[1], avg_time_list)
    date_data = map(lambda x:datetime.strptime(str(x[0]), '%Y%m%d'), min_time_list)
    for ele in date_data:
        date = str(ele.year) +'-' + str(ele.month)
        date_list.append(date)
    
    return_list.append(date_list)
    return_list.append(max_price_data)
    return_list.append(avg_price_data)
    return_list.append(min_price_data)
    
    #for ele in return_list:
        #print ele
    return return_list

if __name__ == '__main__':
    function1('B00857U1CM')
