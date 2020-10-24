from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
import pandas as pd
import numpy as np
import requests 
from bs4 import BeautifulSoup 


@api_view(['POST','GET'])
def webs(request):
	if request.method == 'GET':
			
		return Response("PLEASE ENTER DETAILS!")

	elif request.method == 'POST':
		looking_for = request.data['looking_for']
		place = request.data['place']

		searching = looking_for.split(' ')
		looking_for = "+".join(searching)
		# print(looking_for)

		nexty = True
		count = 0
		page = 1
		vendors=[]
		while nexty is True:
			URL = 'https://www.yellowpages.com/search?search_terms='+looking_for+'&geo_location_terms='+place+'&page='+str(page)

			r = requests.get(URL) 
			# print(r.content) 
			soup = BeautifulSoup(r.content, 'html5lib')
			# print(soup.prettify()) 
			table = soup.findAll('div', attrs = {'class':'info'})

			if_pages = soup.find('a', attrs = {'class':'next ajax-page'})
			if if_pages is not None:
				page = page+1
				nexty = True
			else:
				nexty = False

			for row in table:
				vendor = {}
				# print(row) 
				vendor["id"] = count+1
				count += 1
				name = row.find('a', attrs = {'class':'business-name'}).text
				vendor['name'] = name

				call = row.find('div', attrs = {'class': 'phone'}).text
				vendor['phone'] = call
				
				address = row.find('p', attrs = {'class': 'adr'})
				if address is not None:
					if len(address.text)>0:
						vendor['address'] = address.text
					else:
						address = row.find('div', attrs = {'class': 'street-address'})
						if address is not None:
							address = address.text
							vendor['address'] = address
						else:
							vendor['address'] = row.find('div', attrs = {'class': 'locality'}).text

				info_all = row.findAll('a', attrs = {'data-analytics':'{"click_id":1171,"adclick":false}'})
				if len(info_all)>0:
					info_reqd = []
					for ele in info_all:
						info_reqd.append(ele.text)
					vendor['Information'] = info_reqd
				else:
					info_all = row.findAll('a',attrs = {'data-analytics':'{"click_id":1171,"adclick":false,"listing_features":"category","events":""}'})
					info_reqd = []
					for ele in info_all:
						info_reqd.append(ele.text)
					vendor['Information'] = info_reqd

				website = row.find('div', attrs = {'class':'links'})
				# print("website",name,website)
				if website is not None:
					if website.a is not None:
						website = website.a['href']
						vendor['Website'] = website
				else:
					vendor['Website'] = ""

				vendors.append(vendor)


		# print(page)
		df = pd.DataFrame(vendors)
		# print(df)
		# df.to_csv('/home/dell/live/hostbooks_api/output.ods', sep='\t')
		writer = pd.ExcelWriter(str(looking_for)+'_'+str(place)+'.xlsx')
		df.to_excel(writer,'Sheet1')
		# df2.to_excel(writer,'Sheet2')
		writer.save()
		
		return Response(vendors)








@api_view(['GET', 'POST', 'PUT'])
def check(request):
	if request.method == 'GET':

		data = [

		{"get":"gaurav"},
		{"get":"akshat"},
		{"get":"himanshu"},
		{"get":"viraj"},
		{"get":"prakhar"},
		{"get":"aashrey"},
		{"get":"toni"}

		]

		return Response(data)


	elif request.method == 'POST':

		new = request.data

		print("new")
		print(new)

		data = [

		{"post":"India"},
		{"post":"Australia"},
		{"post":"New Zealand"},
		{"post":"Scotland"},
		{"post":"Amsterdam"},
		{"post":"HUngry"},
		{"post":"Malasia"},
		{"post":"Toni Stark"},

		{'post':new}

		]

		return Response(data)


	elif request.method == 'PUT':

		new = request.data
		
		print("new")
		print(new)

		data = [

		{"put":"India"},
		{"put":"Australia"},
		{"put":"New Zealand"},
		{"put":"Scotland"},
		{"put":"Amsterdam"},
		{"put":"HUngry"},
		{"put":"Malasia"},
		{"put":"Toni Stark"},

		{'put':new}

		]

		return Response(data)




'''


{"gaurav":"asdfghjk"}



'''






