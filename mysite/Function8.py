#-*- coding:utf-8-*-
'''单个商品亚马逊和其他商家不同时间的价格比较'''
'''单个商品亚马逊和其他商家不同时间的价格比较雷达图'''
'''@Author: CaoYuting'''
import urllib
import simplejson as json
from datetime import datetime

def get_product_data(target_url):
    '''获取商品信息'''
    return json.loads(urllib.urlopen(target_url).read())

def get_date_list(target_url):
    '''获取该商品(ASIN)的价格爬取时间点'''
    product_data = get_product_data(target_url)
    date_list=[]
    
    for x in range(len(product_data['offer'])):
        date_list.append(datetime.strptime(product_data['offer'][x]['timestamp'], '%Y-%m-%d %H:%M:%S'))

    return date_list

def get_data_count(target_url):
    product_data = get_product_data(target_url)
    return len(product_data['offer'])

def get_change_date_list(target_url):
    '''爬取时间点格式转变为年/月/日'''
    date_list=get_date_list(target_url)
    #print(date_list)
    change_date_list=[]
    
    for single_date in date_list:
        change_date_list.append(str(single_date).split(' ')[0].split('-')[0]+'/'+str(single_date).split(' ')[0].split('-')[1]+'/'+str(single_date).split(' ')[0].split('-')[2])

    return change_date_list

def get_amazon_price_list(target_url):
    '''获取该商品(ASIN)的亚马逊价格---0价格保留'''
    product_data = get_product_data(target_url)
    amazon_price_list=[]
    
    for x in range(len(product_data['offer'])):
        amazon_price_list.append(0)
        for y in range(len(product_data['offer'][x]['info'])):
            if(product_data['offer'][x]['info'][y]['seller']['name']=='Amazon'):
                amazon_price_list.remove(amazon_price_list[-1])
                amazon_price_list.append(product_data['offer'][x]['info'][y]['price'])
              
    return amazon_price_list 

def get_other_avg_price_list(target_url):
    '''获取该商品(ASIN)的其他商家的价格平均---0价格保留'''
    product_data = get_product_data(target_url)
    other_avg_price_list=[]
    
    for x in range(len(product_data['offer'])):
        other_avg_price_list.append(0)
        other_price=0
        count=0
        for y in range(len(product_data['offer'][x]['info'])):
            if(product_data['offer'][x]['info'][y]['seller']['name']!='Amazon'):
                other_price+=product_data['offer'][x]['info'][y]['price']
                count+=1
               
        if(count!=0):
            other_avg_price_list.remove(other_avg_price_list[-1])
            other_avg_price_list.append(other_price/count)
    
    return other_avg_price_list;

def function8(ASIN):
    '''雷达图获取动态数据'''
    target_url='http://112.124.1.3:8004/api/commodity/'+ASIN+'?field=[\'offer\']'
    date_list=get_change_date_list(target_url)
    amazon_price_list=get_amazon_price_list(target_url)
    other_avg_price_list=get_other_avg_price_list(target_url)
    
    #print(date_list)   
    #print(amazon_price_list)
    #print(other_avg_price_list)
    
    return_list = [] 
    
    return_list.append(date_list)
    return_list.append(amazon_price_list)
    return_list.append(other_avg_price_list)
    #print return_list
    return return_list
   
if __name__ == '__main__':  
    function8('B00857U1CM') 
