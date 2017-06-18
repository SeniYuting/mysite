import simplejson as json
import urllib
from datetime import datetime
import numpy as np
import pandas as pd

def get_single_data(ASIN):
    url = 'http://112.124.1.3:8004/api/commodity/' + ASIN
    return json.loads(urllib.urlopen(url).read())

def function3(ASIN):
    data = get_single_data(ASIN)
    price_time_dict = {}
    
    for single_pro in data['offer']:
        price = []
        for single_seller in single_pro['info']:
            price.append(single_seller['price'])
        if not price_time_dict.has_key(single_pro['timestamp']):
            price_time_dict[(int)(datetime.strftime(datetime.strptime(single_pro['timestamp'],'%Y-%m-%d %H:%M:%S'),'%Y%m%d'))] = price
        else:
            for ele in price:
                price_time_dict[(int)(datetime.strftime(datetime.strptime(single_pro['timestamp'],'%Y-%m-%d %H:%M:%S'),'%Y%m%d'))].append(ele)
    
    new_dict = {}
    for i in price_time_dict:
        if price_time_dict[i]:
            new_dict[i] = price_time_dict[i]
    price_time_list = sorted(new_dict.iteritems(), key=lambda x:x[0])

    price_data = map(lambda x:x[1], price_time_list)
    
    max = []
    q3 = []
    mid = []
    q1 = []
    min = []
    #upper,Q3,middle,Q1,lower
    for ele in price_data:
        for i in range(0,len(ele)-1):
            for j in range(i+1,len(ele)):
                if ele[i] > ele[j]:
                    tmp = ele[i]
                    ele[i] = ele[j]
                    ele[j] = tmp
        
    for e in price_data:
        max.append(e[len(e)-1])
        min.append(e[0])
        
        t = round((float)(len(e)+1)/4 - (len(e)+1)/4,1)
        if t < 0.5:
            q1.append(e[(len(e)+1)/4-1])
        elif t > 0.5:
            q1.append(e[(len(e)+1)/4])
        elif t == 0.5:
            q1.append(round((e[(len(e)+1)/4]+e[(len(e)+1)/4-1])/2,2))
            
        m = round((float)((len(e)+1)*3)/4 - (len(e)+1)*3/4,1)
        if m < 0.5:
            q3.append(e[(len(e)+1)*3/4-1])
        elif m > 0.5:
            q3.append(e[(len(e)+1)*3/4])
        elif m == 0.5:
            q3.append(round((e[(len(e)+1)*3/4]+e[(len(e)+1)*3/4-1])/2,2))
        
        if len(e) % 2 == 0:
            mid.append(round((e[len(e)/2]+e[len(e)/2-1])/2,2))
        else:
            mid.append(e[len(e)/2])
        

    date_data = map(lambda x:datetime.strptime(str(x[0]), '%Y%m%d'), price_time_list)        
    
    str_date = []
    for one in date_data:
        str_date.append(one.strftime('%Y-%m-%d'))
    
    return_list = []
    return_list.append(str_date)
    list_1 = []
    list_1.append(max)
    list_1.append(q3)
    list_1.append(mid)
    list_1.append(q1)
    list_1.append(min)
    return_list.append(list_1)
 
    
    #for ele in return_list:
    #    print ele
        
    return ele

if __name__ == '__main__':
    function3('B002FU62Q4')
