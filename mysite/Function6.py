import simplejson as json
import urllib
from textblob import TextBlob
from datetime import datetime
import math

def get_single_data(ASIN):
    url = 'http://112.124.1.3:8004/api/commodity/'+ASIN  #121 B00857U1CM  113 B002FU62Q4
    return json.loads(urllib.urlopen(url).read())

def imotion_percentage(ASIN):
    dict = get_single_data(ASIN)
    time = []          #2013.1-2014.5
    polarity = []
    neg_count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    pos_count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    rate = []
        
    if dict['review']:
        for each_review in dict['review']:
            content = each_review['content']
            cl = TextBlob(content)
            polarity.append(cl.polarity)
            time.append(datetime.strptime(each_review['publishTime'],'%Y-%m-%d %H:%M:%S'))
   
    for i in range(0,time.__len__()):
        year = time[i].year
        month = time[i].month

        if year == 2013:
            if polarity[i] > 0.0:
                pos_count[month-1] = pos_count[month-1] + 1
            elif polarity[i] < 0.0:
                neg_count[month-1] = neg_count[month-1] + 1
        if year == 2014:
            if polarity[i] > 0.0:
                pos_count[month+11] = pos_count[month+11] + 1
            elif polarity[i] < 0.0:
                neg_count[month+11] = neg_count[month+11] + 1

            
    for i in range(0,17):
        if (pos_count[i] + neg_count[i]) == 0:
            this_rate = -1
        else:
            this_rate = ((float)(pos_count[i]))/(pos_count[i] + neg_count[i])
        rate.append(round(this_rate,4))
        
    date = ['2013-1','2013-2','2013-3','2013-4','2013-5','2013-6','2013-7','2013-8','2013-9','2013-10','2013-11','2013-12','2014-1','2014-2','2014-3','2014-4','2014-5']
    return_list = []
    new_date = []
    pos_rate = []
    neg_rate = []
    for i in range(0,17):
        if not rate[i] == -1:
            new_date.append(date[i])
            pos_rate.append(rate[i])
            neg_rate.append(round(1-rate[i],4))
    
    return_list.append(new_date)
    return_list.append(pos_rate)
    return_list.append(neg_rate)
    
    #print return_list        
    return return_list

if __name__ == '__main__':
    imotion_percentage('B00857U1CM')