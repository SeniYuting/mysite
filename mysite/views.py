#-*- coding:utf-8-*-
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context,loader
from django.template import RequestContext
import datetime
from django.shortcuts import render_to_response
from ShowInfo1 import get_image,get_name,get_feature,get_star,get_price
from ShowInfo2 import get_image2,get_name2,get_feature2,get_star2,get_price2
from ShowInfo3 import get_image3,get_name3,get_feature3,get_star3,get_price3

from getNameImage import get_assigned_cate
from Function1 import function1
from Function2 import function2
from Function3 import function3
from Function4 import function4
from Function5 import function5
from Function6 import imotion_percentage
from Function7 import function7
from Function8 import function8

#First 第一件商品是静态数据
list1_1=['2013/10/26', '2013/11/10', '2013/11/17', '2013/12/23', '2014/01/31', '2014/02/18', '2014/03/04', '2014/04/23', '2014/05/08']
list1_2=[27.99, 27.97, 27.02, 27.77, 0, 0, 0, 27.99, 0, 27.99]
list1_3=[36.23571428571429, 33.8675, 33.96625, 33.583749999999995, 0, 0, 0,31.980000000000004, 0, 32.80200000000001]

list2_1=['2013-10-26', '2013-11-10', '2013-11-17', '2013-12-23', '2014-02-18', '2014-03-04', '2014-04-23', '2014-05-08']
list2_2=[	    [26.140,29.99,30.640,32.99,35.140],
	            [29.210,29.99,29.990,30.51,30.770],
	            [29.930,29.95,29.990,29.99,30.050],
	            [25.540,29.99,30.040,32.99,34.540],
	            [28.610,29.99,29.990,30.91,31.370],
                [27.590,28.39,29.990,29.99,32.390],
                [28.145,30.90,31.730,33.29,35.315],
                [25.950,29.99,30.900,33.29,35.850],
	    ]
		
list3_1=['2010-1-1','2010-8-1','2010-12-1','2011-1-1','2011-4-1','2012-12-1','2012-1-1','2012-2-1','2012-3-1','2012-9-1','2012-10-1','2012-11-1','2012-12-1','2013-1-1','2013-2-1','2013-3-1','2013-4-1','2013-5-1','2013-7-1','2013-8-1','2013-9-1','2013-10-1','2013-11-1','2014-0-1','2014-1-1','2014-2-1','2014-3-1','2014-4-1']
list3_2=[0, 1, 2, 3, 4, 6, 8, 11, 13, 14, 15, 22, 27, 42, 64, 71, 75, 76, 77, 78, 79, 83, 93, 107, 125, 153, 167, 172]


list4_1=['2013-10-26', '2013-11-10', '2013-11-17', '2013-12-23', '2014-2-18', '2014-3-4', '2014-4-23', '2014-5-8']
list4_2=[48, 38.59, 38.59, 37.59, 37.59, 37.59, 40.59, 40.59]
list4_3=[34.28, 32.288, 32.228, 31.98, 31.91, 31.175, 32.747, 32.95]
list4_4=[29.78, 29.66, 29.86, 29.29, 29.99, 27.5, 29.98, 29.98]

list5_1=['2010-1-1','2010-8-1','2010-12-1','2011-1-1','2011-4-1','2012-12-1','2012-1-1','2012-2-1','2012-3-1','2012-9-1','2012-10-1','2012-11-1','2012-12-1','2013-1-1','2013-2-1','2013-3-1','2013-4-1','2013-5-1','2013-7-1','2013-8-1','2013-9-1','2013-10-1','2013-11-1','2014-0-1','2014-1-1','2014-2-1','2014-3-1','2014-4-1']
list5_2=[1, 1, 1, 1, 2, 2, 3, 2, 1, 1, 7, 5, 15, 22, 7, 4, 1, 1, 1, 1, 4, 10, 14, 18, 28,14, 5, 7]

list6_1=['2013-1','2013-2','2013-3','2013-5','2013-7','2013-8','2013-9','2013-10','2013-11','2013-12','2014-1','2014-2','2014-3','2014-4']
list6_2=[0.8, 1.0, 1.0, 1.0,  1.0, 0.5, 1.0, 1.0, 1.0, 0.75, 1.0, 0.5, 0.5, 0.6667]
list6_3=[-0.2, 0, 0, 0,  0, -0.5, 0, 0, 0, -0.25, 0, -0.5, -0.5, -0.3333]
	
list7_1=['2013-10-1', '2013-11-1', '2013-12-1', '2014-1-1','2014-2-1', '2014-3-1']
list7_2=[14, 18, 28, 14, 5, 8]
list7_3=[35.2, 33.21, 33.19, 32.93, 31.58, 32.36]

list8_1=[       ['1', 6.0 ],
                ['2', 23.0],
                ['3', 33.0],
                ['4', 50.0],
                ['5', 67.0]
        ]

#Second 第二件商品是静态数据
datalist1_1=['2013/10/26', '2013/11/10', '2013/11/17', '2013/12/23', '2014/01/31', '2014/02/18', '2014/03/04', '2014/04/23', '2014/05/08']
datalist1_2=[30.64, 30.51, 29.86, 30.04, 30.91, 28.39, 30.9, 0, 30.9]
datalist1_3=[35.19, 32.644000000000005, 32.702, 32.465, 32.11, 31.732, 33.116, 0, 33.4625]

datalist2_1=['2013-10-26', '2013-11-10', '2013-11-17', '2013-12-23', '2014-05-08']
datalist2_2=[
	            [15.12000,27.990,33.43500,40.2000,51.75000],
	            [18.65875,27.985, 29.99500,35.5425,41.33125],
	            [18.65125,27.980, 29.99500,35.5425,41.33875],
	            [18.58375,27.935, 29.99500,35.5425,41.40625],
	            [21.54000,27.990,30.63000,34.0500,39.72000],
            ]
		
datalist3_1=['2012-3-1','2012-4-1','2012-5-1','2012-6-1','2012-7-1','2012-8-1','2012-9-1','2012-10-1','2012-11-1','2013-12-1','2013-1-1','2013-2-1','2013-3-1','2013-4-1','2013-5-1','2013-6-1','2013-7-1','2013-8-1','2013-9-1','2013-10-1','2013-11-1','2013-12-1','2014-1-1','2014-2-1','2014-3-1','2014-4-1']
datalist3_2=[0, 3, 5, 14, 26, 33, 42, 50, 69, 80, 111, 143, 167, 179, 195, 220, 231, 246, 253,258, 265, 277, 290, 310, 333, 351]


datalist4_1=['2013-10-26', '2013-11-10', '2013-11-17', '2013-12-23', '2014-2-18', ]
datalist4_2=[51.02, 41.41, 41.41, 40.2, 42.41]
datalist4_3=[35.205, 33.212, 33.194, 32.938, 31.973]
datalist4_4=[27.37, 27.16, 27.02, 26.89, 27.98]

datalist5_1=['2012-3-1','2012-4-1','2012-5-1','2012-6-1','2012-7-1','2012-8-1','2012-9-1','2012-10-1','2012-11-1','2013-12-1','2013-1-1','2013-2-1','2013-3-1','2013-4-1','2013-5-1','2013-6-1','2013-7-1','2013-8-1','2013-9-1','2013-10-1','2013-11-1','2013-12-1','2014-1-1','2014-2-1','2014-3-1','2014-4-1']
datalist5_2=[3, 2, 9, 12, 7, 9, 8, 19, 11, 31, 32, 24, 12, 16, 25, 11, 15, 7, 5, 7, 12, 13, 20, 23, 18, 6]

datalist6_1=['2013-1', '2013-2', '2013-3', '2013-4', '2013-5', '2013-7', '2013-8', '2013-9', '2013-10', '2013-11', '2013-12', '2014-1', '2014-2', '2014-3', '2014-4', '2013-12', '2014-1', '2014-2', '2014-3', '2014-4', '2014-5']
datalist6_2=[0.9, 0.8571, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.7778, 1.0, 0.9286, 0.8519, 0.9286, 1.0, 1.0]
datalist6_3=[-0.1, -0.1429, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.2222, 0.0, -0.0714, -0.1481, -0.0714, 0.0, 0.0]
	
datalist7_1=['2013-8-1', '2013-9-1', '2013-10-1', '2013-11-1', '2013-12-1', '2014-1-1','2014-2-1', '2014-3-1']
datalist7_2=[2, 1, 2, 4, 3, 2, 2, 5]
datalist7_3=[34.28, 32.28, 32.22, 31.98, 31.91, 31.17, 32.74, 32.95]

datalist8_1=[
                ['1',   3],
                ['2',   6],
                ['3',   6],
                ['4',   12],
                ['5',   16]
        ]

#normal 第三件商品是动态数据
ASIN='B00CAAJA2W'

list1=function8(ASIN)
normallist1_1=list1[0]
normallist1_2=list1[1]
normallist1_3=list1[2]

list2=function3(ASIN)
normallist2_1=['2013-10-26', '2013-11-10', '2013-11-17', '2013-12-23', '2014-02-18', '2014-03-04', '2014-04-23', '2014-05-08']
normallist2_2=[	    [26.140,29.99,30.640,32.99,35.140],
	            [29.210,29.99,29.990,30.51,30.770],
	            [29.930,29.95,29.990,29.99,30.050],
	            [25.540,29.99,30.040,32.99,34.540],
	            [28.610,29.99,29.990,30.91,31.370],
                [27.590,28.39,29.990,29.99,32.390],
                [28.145,30.90,31.730,33.29,35.315],
                [25.950,29.99,30.900,33.29,35.850],
	    ]

list3=function4(ASIN)
normallist3_1=list3[0]
normallist3_2=list3[1]

list4=function1(ASIN)
normallist4_1=list4[0]
normallist4_2=list4[1]
normallist4_3=list4[2]
normallist4_4=list4[3]

list5=function5(ASIN)
normallist5_1=list5[0]
normallist5_2=list5[1]

list6=imotion_percentage(ASIN)
normallist6_1=list6[0]
normallist6_2=list6[1]
normallist6_3=list6[2]

list7=function2(ASIN)
normallist7_1=list7[0]
normallist7_2=list7[1]
normallist7_3=list7[2]		

list8=function7(ASIN)		
normallist8_1=list8		
		
#category 分类是静态数据
category1_1=['0-50','50-100','100-200','>200']
category1_2=[611,407,366,14]		

category2_1=[
                ['0-20', 1290],
                ['20-40',210],
                ['40-60', 63],
                ['>60',   177]
            ]			

category3_1=['2005/08', '2006/01', '2006/03', '2006/06', '2006/07', '2006/08', '2006/09', '2006/11', '2006/12', '2007/01', '2007/02', '2007/03', '2007/04', '2007/05', '2007/07', '2007/08', '2007/09', '2007/10', '2007/11', '2007/12', '2008/01', '2008/02', '2008/03', '2008/04', '2008/05', '2008/06', '2008/07', '2008/08', '2008/09', '2008/10', '2008/11', '2008/12', '2009/01', '2009/02', '2009/03', '2009/04', '2009/05', '2009/06', '2009/07', '2009/08', '2009/09', '2009/10', '2009/11', '2009/12', '2010/01', '2010/02', '2010/03', '2010/04', '2010/05', '2010/06', '2010/07', '2010/08', '2010/09', '2010/10', '2010/11', '2010/12', '2011/01', '2011/02', '2011/03', '2011/04', '2011/05', '2011/06', '2011/07', '2011/08', '2011/09', '2011/10', '2011/11', '2011/12', '2012/01', '2012/02', '2012/03', '2012/04', '2012/05', '2012/06', '2012/07', '2012/08', '2012/09', '2012/10', '2012/11', '2012/12', '2013/01', '2013/02', '2013/03', '2013/04', '2013/05', '2013/06', '2013/07', '2013/08', '2013/09', '2013/10', '2013/11', '2013/12', '2014/01', '2014/02', '2014/03', '2014/04', '2014/05']
category3_2=[1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 3, 3, 1, 2, 2, 3, 2, 1, 5, 5, 6, 3, 2, 4, 6, 2, 

4, 5, 5, 7, 10, 12, 9, 11, 11, 10, 10, 6, 9, 13, 14, 15, 23, 19, 18, 22, 16, 13, 

12, 10, 19, 16, 23, 24, 25, 23, 25, 21, 24, 20, 16, 19, 16, 19, 24, 28, 28, 28, 28, 

28, 23, 28, 25, 27, 29, 29, 30, 30, 31, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 

31, 31, 28, 31, 30, 7]

category4_1=['2013-1', '2013-2', '2013-3', '2013-4', '2013-5', '2013-6', '2013-7', '2013-8', '2013-9', '2013-10', '2013-11', '2013-12', '2014-1', '2014-2', '2014-3', '2014-4', '2014-5']
category4_2=[0.918, 0.9257, 0.9195, 0.9315, 0.9134, 0.9034, 0.9095, 0.9118, 0.8942, 0.913, 0.9065, 0.9158, 0.8968, 0.922, 0.8923, 0.8983, 0.8783]
category4_3=[-0.082, -0.0743, -0.0805, -0.0685, -0.0866, -0.0966, -0.0905, -0.0882, -0.1058, -0.087, -0.0935, -0.0842, -0.1032, -0.078, -0.1077, -0.1017, -0.1217]

#image&name		只有当选择的分类是	Clothing & Accessories>Women>Jeans 时使用静态数据
bigList=[["Dickies Women's Slim Straight Leg Jean", 'http://ecx.images-amazon.com/images/I/31MZLMLvfhL._SX342_.jpg'], 
["Dickies Women's Flannel Lined Jean", 'http://ecx.images-amazon.com/images/I/41eNCdbC49L._SY445_.jpg'], 
["Levi's Women's 512 Perfectly Slimming Boot Cut Jean", 'http://ecx.images-amazon.com/images/I/41k6Pg0PqML._SX342_.jpg'], 
["Levi's Women's 512 Perfectly Slimming Boot Cut Jean", 'http://ecx.images-amazon.com/images/I/31CwFoSSnNL._SX342_.jpg'],
["Levi's Women's 512 Perfectly Slimming Boot Cut Jean", 'http://ecx.images-amazon.com/images/I/31-%2BgJjwcvL._SY445_.jpg'], 
["Lee Women's Relaxed Fit Straight Leg Jean", 'http://ecx.images-amazon.com/images/I/41ZCWZLgZ2L._SX342_.jpg'], 
["Levi's Women's 535 Legging Jean", 'http://ecx.images-amazon.com/images/I/418QUdENWhL._SX342_.jpg'], 
["Levi's Women's 515 Boot Cut Jean", 'http://ecx.images-amazon.com/images/I/41vgkMOh3nL._SX342_.jpg'], 
["Levi's Women's 505 Straight Leg Jean", 'http://ecx.images-amazon.com/images/I/31d27CVZnJL._SX342_.jpg'], 
["Levi's Women's 525 Straight Leg Perfect Waist Jean", 'http://ecx.images-amazon.com/images/I/41OLw7lq4VL._SX342_.jpg'], 
["Dickies Women's Relaxed Boot-Cut Jean", 'http://ecx.images-amazon.com/images/I/41OjQrZjdqL._SY445_.jpg'], 
["Levi's Women's 580 Plus-Size Curvy Boot Cut Jean", 'http://ecx.images-amazon.com/images/I/41zegC6hCoL._SX342_.jpg'],
["Levi's Women's 580 Plus-Size Curvy Boot Cut Jean", 'http://ecx.images-amazon.com/images/I/41K8u8vbdbL._SX342_.jpg'], 
["Levi's Women's 580 Plus-Size Curvy Boot Cut Jean", 'http://ecx.images-amazon.com/images/I/41zegC6hCoL._SX342_.jpg'], 
["Lee Women's Plus Hidden Side-Elastic Stretch Jean", 'http://ecx.images-amazon.com/images/I/31DtLRNpmzL._SX342_.jpg'], 
["Wrangler Blues Women's Relaxed Jean", 'http://ecx.images-amazon.com/images/I/41SqxxfohZL._SX342_.jpg'], 
["Levi's Women's 512 Plus-Size Perfectly Shaping Straight Leg Jean", 'http://ecx.images-amazon.com/images/I/41SSJRgS2jL._SX342_.jpg'], 
["Gloria Vanderbilt Women's Plus 5 Pocket Amanda Jean", 'http://ecx.images-amazon.com/images/I/41ZakvfM8yL._SY445_.jpg'],
["Gloria Vanderbilt Women's Plus 5 Pocket Amanda Jean", 'http://ecx.images-amazon.com/images/I/31ZIFy4eJDL._SY445_.jpg'], 
["Levi's Women's Petite Mid Rise Skinny Jean", 'http://ecx.images-amazon.com/images/I/41ZOGJzzmrL._SX342_.jpg']]		




		
def test(request):
	if request.method == 'POST':
		a = request.POST.get('first','null')
		b = request.POST.get('second','null')
		c = request.POST.get('third','null')
		total=a+'>'+b+'>'+c
		if (a=="Clothing & Accessories")& (b=='Women')& (c=='Jeans'):
			return render_to_response('change.html', {'image1':bigList[0][1],'commodity1':bigList[0][0],
											 'image2':bigList[1][1],'commodity2':bigList[1][0],
											 'image3':bigList[2][1],'commodity3':bigList[2][0],
											 'image4':bigList[3][1],'commodity4':bigList[3][0],
											 'image5':bigList[4][1],'commodity5':bigList[4][0],
											 'image6':bigList[5][1],'commodity6':bigList[5][0],
											 'image7':bigList[6][1],'commodity7':bigList[6][0],
											 'image8':bigList[7][1],'commodity8':bigList[7][0],
											 'image9':bigList[8][1],'commodity9':bigList[8][0],
											 'image10':bigList[9][1],'commodity10':bigList[9][0],
											 'image11':bigList[10][1],'commodity11':bigList[10][0],
											 'image12':bigList[11][1],'commodity12':bigList[11][0],
											 'image13':bigList[12][1],'commodity13':bigList[12][0],
											 'image14':bigList[13][1],'commodity14':bigList[13][0],
											 'image15':bigList[14][1],'commodity15':bigList[14][0],
											 'image16':bigList[15][1],'commodity16':bigList[15][0],
											 'image17':bigList[16][1],'commodity17':bigList[16][0],
											 'image18':bigList[17][1],'commodity18':bigList[17][0],
											 'image19':bigList[18][1],'commodity19':bigList[18][0],
											 'image20':bigList[19][1],'commodity20':bigList[19][0],
											 
											}, context_instance=RequestContext(request))
		else:
			nameImage=get_assigned_cate(total)
			return render_to_response('normal.html', {'image1':nameImage[0][1],'commodity1':nameImage[0][0],
											 'image2':nameImage[1][1],'commodity2':nameImage[1][0],
											 'image3':nameImage[2][1],'commodity3':nameImage[2][0],
											 'image4':nameImage[3][1],'commodity4':nameImage[3][0],
											 'image5':nameImage[4][1],'commodity5':nameImage[4][0],
											 'image6':nameImage[5][1],'commodity6':nameImage[5][0],
											 'image7':nameImage[6][1],'commodity7':nameImage[6][0],
											 'image8':nameImage[7][1],'commodity8':nameImage[7][0],
											 'image9':nameImage[8][1],'commodity9':nameImage[8][0],
											 'image10':nameImage[9][1],'commodity10':nameImage[9][0],
											 'image11':nameImage[10][1],'commodity11':nameImage[10][0],
											 'image12':nameImage[11][1],'commodity12':nameImage[11][0],
											 'image13':nameImage[12][1],'commodity13':nameImage[12][0],
											 'image14':nameImage[13][1],'commodity14':nameImage[13][0],
											 'image15':nameImage[14][1],'commodity15':nameImage[14][0],
											 'image16':nameImage[15][1],'commodity16':nameImage[15][0],
											 'image17':nameImage[16][1],'commodity17':nameImage[16][0],
											 'image18':nameImage[17][1],'commodity18':nameImage[17][0],
											 'image19':nameImage[18][1],'commodity19':nameImage[18][0],
											 'image20':nameImage[19][1],'commodity20':nameImage[19][0],
											 
											}, context_instance=RequestContext(request))  
	else:
		a = "get"
		return render_to_response('index.html', {}, context_instance=RequestContext(request))
	
feature2=get_feature2()	
	
def first(request):
	return render_to_response('single121.html',{'picture2':get_image2(),
												'name2':get_name2(),
												'price2':get_price2(),
												'feature00':feature2[0],
												'feature11':feature2[1],
												'feature22':feature2[2],
												'feature33':feature2[3],
												'feature44':feature2[4],
												#'feature55':feature2[5],
												'star2':get_star2(),
	
												'list1_1':list1_1,'list1_2':list1_2,'list1_3':list1_3,
												'list2_1':list2_1,'list2_2':list2_2,
												'list3_1':list3_1,'list3_2':list3_2,
												'list4_1':list4_1,'list4_2':list4_2,'list4_3':list4_3,'list4_4':list4_4,
												'list5_1':list5_1,'list5_2':list5_2,
												'list6_1':list6_1,'list6_2':list6_2,'list6_3':list6_3,
												'list7_1':list7_1,'list7_2':list7_2,'list7_3':list7_3,
												'list8_1':list8_1,
												}, context_instance=RequestContext(request))
												
feature=get_feature()
												
def second(request):
	return render_to_response('single113.html',{'picture':get_image(),
												'name':get_name(),
												'price':get_price(),
												'feature0':feature[0],
												'feature1':feature[1],
												'feature2':feature[2],
												'feature3':feature[3],
												'feature4':feature[4],												
												'star':get_star(),		
												'datalist1_1':datalist1_1,'datalist1_2':datalist1_2,'datalist1_3':datalist1_3,
												'datalist2_1':datalist2_1,'datalist2_2':datalist2_2,
												'datalist3_1':datalist3_1,'datalist3_2':datalist3_2,
												'datalist4_1':datalist4_1,'datalist4_2':datalist4_2,'datalist4_3':datalist4_3,'datalist4_4':datalist4_4,
												'datalist5_1':datalist5_1,'datalist5_2':datalist5_2,
												'datalist6_1':datalist6_1,'datalist6_2':datalist6_2,'datalist6_3':datalist6_3,
												'datalist7_1':datalist7_1,'datalist7_2':datalist7_2,'datalist7_3':datalist7_3,
												'datalist8_1':datalist8_1,
												}, context_instance=RequestContext(request))

def category(request):
	return render_to_response('category.html',{#'category1_1':category1_1,'category1_2':category1_2,
											   'category2_1':category2_1,
											   'category3_1':category3_1,'category3_2':category3_2,
											   'category4_1':category4_1,'category4_2':category4_2,'category4_3':category4_3,
	
												},context_instance=RequestContext(request))

feature3=get_feature3()
def lab(request):
	return render_to_response('singleDynamic.html',{'picture3':get_image3(),
												'name3':get_name3(),
												'price3':get_price3(),
												'feature000':feature3[0],
												'feature111':feature3[1],
												'feature222':feature3[2],
												'feature333':feature3[3],
												'feature444':feature3[4],
												'feature555':feature3[5],
												'star3':get_star3(),
												#"hh":get_single_data3(),
	
												'normallist1_1':normallist1_1,'normallist1_2':normallist1_2,'normallist1_3':normallist1_3,
												'normallist2_1':normallist2_1,'normallist2_2':normallist2_2,
												'normallist3_1':normallist3_1,'normallist3_2':normallist3_2,
												'normallist4_1':normallist4_1,'normallist4_2':normallist4_2,'normallist4_3':normallist4_3,'normallist4_4':normallist4_4,
												'normallist5_1':normallist5_1,'normallist5_2':normallist5_2,
												'normallist6_1':normallist6_1,'normallist6_2':normallist6_2,'normallist6_3':normallist6_3,
												'normallist7_1':normallist7_1,'normallist7_2':normallist7_2,'normallist7_3':normallist7_3,
												'normallist8_1':normallist8_1,
												}, context_instance=RequestContext(request))