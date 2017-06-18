import urllib
import simplejson as json

def get_single_data3():
    url = 'http://112.124.1.3:8004/api/commodity/B00CAAJA2W'  
    return json.loads(urllib.urlopen(url).read())

def get_name3():
    dict = get_single_data3()
    name = dict['productInfo'][0]['name']
    return name

def get_image3():
    dict = get_single_data3()
    image = dict['productInfo'][0]['img']
    return image

def get_feature3():
    dict = get_single_data3()
    feature = dict['productInfo'][0]['feature']
    return feature

def get_descrip3():
    dict = get_single_data3()
    description = dict['productInfo'][0]['productDescription']
    return description


def get_star3():
    dict = get_single_data3()
    star = dict['stats_info']['star_info']
    avg_star = float(star['1']+star['2']*2+star['3']*3+star['4']*4+star['5']*5)/(star['1']+star['2']+star['3']+star['4']+star['5'])
    return round(avg_star,2)
	
def get_price3():
    seller = []
    all_price = 0.0
    dict = get_single_data3()
    offer = dict['offer'][0]['info']
    for each_seller in offer:
        all_price = all_price + each_seller['price']
    
    avg_price = all_price/len(offer)
    
    return avg_price

def price_range():
    dict = get_single_data3()
    price = 0.0
    price_list = []
    count = 0
    if dict['offer']:
        for each_offer in dict['offer']:
            if each_offer['info']:
                for each_seller in each_offer['info']:
                    if each_seller:
                        price_list.append(each_seller['price'])
                        price = price + each_seller['price']
                        count = count + 1
    
    avg_price = price / count
    
    s = 0.0
    for ele in price_list:
        s = s + (ele - avg_price)*(ele - avg_price)
    
    s = math.sqrt(s / (len(price_list) - 1))
    min = round(avg_price - 1.96 * s / math.sqrt(len(price_list)),2)
    max = round(avg_price + 1.96 * s / math.sqrt(len(price_list)),2)
    
    info = str(min)+'--'+str(max)
    print info
    return info