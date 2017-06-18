#-*- coding:utf-8-*-
'''单个商品的评论数统计'''
'''单个商品评论数随时间不累加单月柱状图'''
'''@Author: CaoYuting'''
import urllib
import simplejson as json
from datetime import datetime

def get_product_data(target_url):
    '''获取商品信息'''
    return json.loads(urllib.urlopen(target_url).read())

def get_date_list(target_url):
    '''获取商品的所有评论日期'''
    product_data = get_product_data(target_url)
    date_list=[]
    
    review=product_data['review']
    for review_time in review:
        date_list.append(datetime.strptime(review_time['publishTime'], '%Y-%m-%d %H:%M:%S'))
        
    return date_list

def get_review_count_list(target_url):
    '''获取商品的所有评论日期（年/月）对应的评论数'''
    date_list=get_date_list(target_url)
    review_count_dict = {}
    
    for single_date in date_list[::-1]:
        review_count_dict[int(single_date.strftime('%Y%m'))] = review_count_dict[int(single_date.strftime('%Y%m'))] + 1 \
            if review_count_dict.has_key(int(single_date.strftime('%Y%m'))) else 1
    review_count_list = sorted(review_count_dict.iteritems(), key=lambda x:x[0])
     
    return review_count_list 
    
def function5(ASIN):
    target_url='http://112.124.1.3:8004/api/commodity/'+ASIN+'?field=[\'review.publishTime\']'
    review_count_list = get_review_count_list(target_url)
    
    date_data = map(lambda x:datetime.strptime(str(x[0]), '%Y%m'), review_count_list)
    review_count=[]
    for review_count_item in review_count_list:
        review_count.append(review_count_item[1])
        
    change_date_list=[]
    
    for single_date in date_data:
        change_date_list.append(str(single_date).split(' ')[0].split('-')[0]+'/'+str(single_date).split(' ')[0].split('-')[1]+'/'+str(single_date).split(' ')[0].split('-')[2])
        
    #print(date_data)
    #print(change_date_list)
    #print(review_count)
    
    return_list = [] 
    
    return_list.append(change_date_list)
    return_list.append(review_count)

    #print return_list
    return return_list
    
if __name__ == '__main__':  
    function5('B00857U1CM') 
