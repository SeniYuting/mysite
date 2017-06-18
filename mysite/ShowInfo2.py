import urllib
import simplejson as json

def get_single_data2():
    url = 'http://112.124.1.3:8004/api/commodity/B00857U1CM'  #113 B002FU62Q4
    return json.loads(urllib.urlopen(url).read())

def get_name2():
    dict = get_single_data2()
    name = dict['productInfo'][0]['name']
    return name

def get_image2():
    dict = get_single_data2()
    image = dict['productInfo'][0]['img']
    return image

def get_feature2():
    dict = get_single_data2()
    feature = dict['productInfo'][0]['feature']
    return feature

def get_descrip2():
    dict = get_single_data2()
    description = dict['productInfo'][0]['productDescription']
    return description


def get_star2():
    dict = get_single_data2()
    star = dict['stats_info']['star_info']
    avg_star = float(star['1']+star['2']*2+star['3']*3+star['4']*4+star['5']*5)/(star['1']+star['2']+star['3']+star['4']+star['5'])
    return round(avg_star,2)
	
def get_price2():
    seller = []
    all_price = 0.0
    dict = get_single_data2()
    offer = dict['offer'][0]['info']
    for each_seller in offer:
        all_price = all_price + each_seller['price']
    
    avg_price = all_price/len(offer)
    
    return avg_price
