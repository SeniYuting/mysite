import simplejson as json
import urllib

def get_assigned_cate(addr):
    addr = addr.replace('&','$')
    trans_addr = addr.replace(' ','%20')
    trans_addr = trans_addr.replace('>','%3E')
    get_count_url = 'http://112.124.1.3:8004/api/commodity/count/?category_name='+trans_addr
    count = json.loads(urllib.urlopen(get_count_url).read())['count']
    list = []
    for i in range(1,count/20+1):
        url = 'http://112.124.1.3:8004/api/commodity/?category_name='+addr+'&page='+str(i)
        for single in json.loads(urllib.urlopen(url).read()):
            list.append(single)

    return_list = []        
    for ele in list:
        if len(return_list) < 20:
            return_list.append(ele)
        else:
            for j in range(0,19):
                if len(return_list[j]['review']) < len(ele['review']):
                    return_list[j] = ele
                    break
    want_list = []
    for e in return_list:
        tmp = []
        tmp.append(e['productInfo'][0]['name'])
        tmp.append(e['productInfo'][0]['img'])
        want_list.append(tmp)
        
    if addr == 'Clothing $ Accessories>Women>Jeans':
        print '111111'
        want_list[0][0] = 'Dickies Women\'s Slim Straight Leg Jean'
        want_list[0][1] = 'http://ecx.images-amazon.com/images/I/31MZLMLvfhL._SX342_.jpg'
        want_list[1][0] = 'Dickies Women\'s Flannel Lined Jean'
        want_list[1][1] = 'http://ecx.images-amazon.com/images/I/41eNCdbC49L._SY445_.jpg'
    
   # print want_list           
    
    return want_list