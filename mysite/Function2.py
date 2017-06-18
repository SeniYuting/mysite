# -*- coding:utf-8-*-
import simplejson as json
import urllib
from datetime import datetime
import string

def get_single_data(ASIN):
    url = 'http://112.124.1.3:8004/api/commodity/' + ASIN
    return json.loads(urllib.urlopen(url).read())

def get_product_data(target_url):    
    return json.loads(urllib.urlopen(target_url).read())

def function2(ASIN):
    product_data=get_single_data(ASIN)
    
    price_list=[]
    date_list=[]
    
    for offer in product_data['offer']:
        if(len(offer['info']) is not 0):#如果info对应的序列不是空的;有price信息
            num=0
            price_num=0
            for info in offer['info']:
                num =num+1
                price_num=price_num+info['price']
            date_list.append(datetime.strptime(offer['timestamp'],'%Y-%m-%d %H:%M:%S'))#最后一个
            
            price_list.append((price_num/num)*10000//100/100)    

    #以上为getprice
    
    len_cmt=len(product_data['review'])
    
    max_year=string.atoi(product_data['review'][0]['publishTime'].split('-')[0])#评论的最近年份
    min_year=string.atoi(product_data['review'][len_cmt-1]['publishTime'].split('-')[0])

    max_month=string.atoi(product_data['review'][0]['publishTime'].split('-')[1])#月份
    min_month=string.atoi(product_data['review'][len_cmt-1]['publishTime'].split('-')[1])
 
    month_num=(max_year-min_year)*12+max_month-min_month

    cmtnum_list=[0]*month_num
    
    for review in product_data['review']:
        itv=(string.atoi(review['publishTime'].split('-')[0])-min_year)*12+(string.atoi(review['publishTime'].split('-')[1])-min_month)
        #print itv
        #cmtnum_list[itv-1]+=1
        cmtnum_list[itv-1]+=1

    cmt_date_list=[]
    i=0
    while i<month_num:
        
        if min_month+i<=12:
            cmt_date_list.append(datetime.strptime(('%d' %min_year)+'-'+('%d' %(min_month+i))+'-1 00:00:00',
                                          '%Y-%m-%d %H:%M:%S'))
        elif min_month+i<=24:
            cmt_date_list.append(datetime.strptime(('%d' %(min_year+1)) +'-'+('%d' %(min_month+i-12))+'-1 00:00:00',
                                          '%Y-%m-%d %H:%M:%S'))
        elif min_month+i<=36:
            cmt_date_list.append(datetime.strptime(('%d' %(min_year+2)) +'-'+('%d' %(min_month+i-24))+'-1 00:00:00',
                                          '%Y-%m-%d %H:%M:%S'))
        elif min_month+i<=48:
            cmt_date_list.append(datetime.strptime(('%d' %(min_year+3)) +'-'+('%d' %(min_month+i-36))+'-1 00:00:00',
                                          '%Y-%m-%d %H:%M:%S'))
        elif min_month+i<=60:
            cmt_date_list.append(datetime.strptime(('%d' %(min_year+4)) +'-'+('%d' %(min_month+i-48))+'-1 00:00:00',
                                          '%Y-%m-%d %H:%M:%S'))
        elif min_month+i<=72:
            cmt_date_list.append(datetime.strptime(('%d' %(min_year+5)) +'-'+('%d' %(min_month+i-60))+'-1 00:00:00',
                                          '%Y-%m-%d %H:%M:%S'))
        elif min_month+i<=84:
            cmt_date_list.append(datetime.strptime(('%d' %(min_year+6)) +'-'+('%d' %(min_month+i-72))+'-1 00:00:00',
                                          '%Y-%m-%d %H:%M:%S'))
        elif min_month+i<=96:
            cmt_date_list.append(datetime.strptime(('%d' %(min_year+7)) +'-'+('%d' %(min_month+i-84))+'-1 00:00:00',
                                          '%Y-%m-%d %H:%M:%S'))
            
        i+=1

    cmtnum_list2=cmtnum_list[-len(date_list):]
    cmt_date_list2=cmt_date_list[-len(date_list):]

    return_list = []
    date_list = []
    for ele in cmt_date_list2:
        date = str(ele.year) +'-' + str(ele.month)
        date_list.append(date)
    
    return_list.append(date_list)
    return_list.append(price_list)
    return_list.append(cmtnum_list2)
    
   # for ele in return_list:
    #    print ele
    #first:date,second:price,third:comment
    return return_list

if __name__ == '__main__':
    function2('B00857U1CM')