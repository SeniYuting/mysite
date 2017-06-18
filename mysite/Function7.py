# -*- coding:utf-8-*-

import urllib
import simplejson as json

def get_product_data(ASIN):
    target_url = 'http://112.124.1.3:8004/api/commodity/'+ASIN+'/'
    return json.loads(urllib.urlopen(target_url).read())

def function7(ASIN):
    product_data = get_product_data(ASIN)
    
    star_list = [float(single_review['star'].split()[0]) \
                 for single_review in product_data['review']]
    one=0.0   
    two=0.0 
    three=0.0
    four=0.0  
    five=0.0
    
    for i in star_list:
        if i==1.0:
            one=one+1.0
        elif i==2.0:
            two=two+1.0
        elif i==3.0:
            three=three+1.0
        elif i==4.0:
            four=four+1.0
        else:
            five=five+1.0
    
    #print(one)
    #print(two)
    #print(three)
    #print(four)
    #print(five)
    
    return_list = [] 
    
    list1 = ['1', one]
    list2 = ['2', two]
    list3 = ['3', three]
    list4 = ['4', four]
    list5 = ['5', five]
    
    return_list.append(list1)
    return_list.append(list2)
    return_list.append(list3)
    return_list.append(list4)
    return_list.append(list5)

    #print return_list
    return return_list 

if __name__ == '__main__':
    function7('B00857U1CM')    
