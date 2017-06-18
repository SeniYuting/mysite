#-*- coding:utf-8-*-
'''单个商品评论数随时间累加折线图'''
'''@Author: CaoYuting'''
import urllib
import simplejson as json
from datetime import datetime

def get_product_data(target_url):
    '''获取商品信息'''
    return json.loads(urllib.urlopen(target_url).read())
    
def incre_list(origin_list):
    '''数组元素递加'''
    return [sum(origin_list[0: idx]) for idx,ele in enumerate(origin_list)]

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

def function4(ASIN):
    target_url='http://112.124.1.3:8004/api/commodity/'+ASIN+'?field=[\'review.publishTime\']'
    review_count_list = get_review_count_list(target_url)
    
    date_data = map(lambda x:datetime.strptime(str(x[0]), '%Y%m'), review_count_list)
    count_data = incre_list(map(lambda x:x[1], review_count_list))  #评论数累加
    
    change_date_list=[]
    
    for single_date in date_data:
        change_date_list.append(str(single_date).split(' ')[0].split('-')[0]+'/'+str(single_date).split(' ')[0].split('-')[1]+'/'+str(single_date).split(' ')[0].split('-')[2])
    
    #print(date_data)
    #print(change_date_list)
    #print(count_data)
    
    return_list = [] 
    
    return_list.append(change_date_list)
    return_list.append(count_data)

    #print return_list
    return return_list
    
if __name__ == '__main__':
    function4('B00857U1CM')   
