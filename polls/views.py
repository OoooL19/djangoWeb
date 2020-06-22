from django.shortcuts import render
import json
import requests
import json
from time import sleep
import requests
import yaml
import re
# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string
from django.urls import reverse
from selectorlib import Extractor
from polls.models import Output
from polls.forms import OutputForm
from datetime import datetime
from django.contrib import messages

e = Extractor.from_yaml_file('polls/selectors.yml')
def index(request):
    return render(request, 'polls/base.html', {})


def is_valid_queryparam(param):
    return param != '' and param is not None

def output(request):
	if request.method == 'GET' and 's_bt' in request.GET:
		alldata = Output.objects.all()
		brand_name_query = request.GET.get('brand_name')
		cpu_exact_query = request.GET.get('cpu_exact')
		screen_filter_query = request.GET.get('screen_filter')
		upc_filter_query = request.GET.get('upc_filter')
		view_count_min = request.GET.get('view_count_min')
		view_count_max = request.GET.get('view_count_max')
		view_price_min = request.GET.get('view_price_min')
		view_price_max = request.GET.get('view_price_max')
		date_min = request.GET.get('date_min')
		date_max = request.GET.get('date_max')
		temp = request.session.get('temp')
		new = []
		for i in alldata:
			new.append(i.asin)	
		request.session['temp'] = new
		if is_valid_queryparam(brand_name_query):
			alldata = alldata.filter(brand__contains = brand_name_query)
			new = []
			for i in alldata:
				new.append(i.asin)	
			request.session['temp'] = new
		if is_valid_queryparam(cpu_exact_query):
			alldata = alldata.filter(cpu__contains = cpu_exact_query)
			new = []
			for i in alldata:
				new.append(i.asin)	
			request.session['temp'] = new
		if is_valid_queryparam(screen_filter_query):
			alldata = alldata.filter(screen__contains = screen_filter_query)
			new = []
			for i in alldata:
				new.append(i.asin)	
			request.session['temp'] = new
		if is_valid_queryparam(upc_filter_query):
			alldata = alldata.filter(upc__contains = upc_filter_query)
			new = []
			for i in alldata:
				new.append(i.asin)	
			request.session['temp'] = new
		if is_valid_queryparam(view_count_min):
			alldata = alldata.filter(rank__gte = view_count_min)
			new = []
			for i in alldata:
				new.append(i.asin)	
			request.session['temp'] = new
		if is_valid_queryparam(view_count_max):
			alldata = alldata.filter(rank__lt = view_count_max)
			new = []
			for i in alldata:
				new.append(i.asin)	
			request.session['temp'] = new
		if is_valid_queryparam(view_price_min):
			alldata = alldata.filter(price__gte = view_price_min)
			new = []
			for i in alldata:
				new.append(i.asin)	
			request.session['temp'] = new
		if is_valid_queryparam(view_price_max):
			alldata = alldata.filter(price__lt = view_price_max)
			new = []
			for i in alldata:
				new.append(i.asin)	
			request.session['temp'] = new
		if is_valid_queryparam(date_min):
			alldata = alldata.filter(date__gte = date_min)
			new = []
			for i in alldata:
				new.append(i.asin)	
			request.session['temp'] = new
		if is_valid_queryparam(date_max):
			alldata = alldata.filter(date__lt = date_max)
			new = []
			for i in alldata:
				new.append(i.asin)	
			request.session['temp'] = new
		print(request.POST.getlist('brand'))
		alldata = alldata.order_by('rank')
		return render(request, 'polls/base.html', {'alldata': alldata})



	if request.method == 'POST' and 'url_bt' in request.POST:
		urls = request.POST.get('url')
		print(urls)
		myDate = datetime.now()
		formatedDate = myDate.strftime("%Y-%m-%d")
		headers = {
			'authority': 'www.amazon.com',
			'pragma': 'no-cache',
			'cache-control': 'no-cache',
			'dnt': '1',
			'upgrade-insecure-requests': '1',
			'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
			"apikey": "b50b92c0-afeb-11ea-9d8a-5dc1a2b8f2ee"
		}
		params = (
			("url", urls),
			 # ("location", "na"),
			("premium", "true"),
			("location", "us"),
	    )

		# Download the page using requests
		# print("Downloading %s"%url)
		# r = requests.get('https://app.zenscrape.com/api/v1/get', headers=headers, params=params)
		# r = requests.get(urls, headers=headers)
		r = requests.get('https://app.zenscrape.com/api/v1/get', headers=headers, params=params)
		# Simple check to check if page was blocked (Usually 503)
		if r.status_code > 500:
			if "To discuss automated access to Amazon data please contact" in r.text:
				print("Page %s was blocked by Amazon. Please try using better proxies\n"%urls)
			else:
				print("Page %s must have been blocked by Amazon as the status code was %d"%(urls,r.status_code))
			return None
		# Pass the HTML of the page and create
		# print(e.extract(r.text))
		# return e.extract(r.text)
		print(e.extract(r.text))
		data = e.extract(r.text)
		data['date'] = formatedDate
		data['link'] = urls
		data['List'] = 'List'
		data['brand'] = 'brand'
		data['cpu'] = 'cpu'
		data['screen'] = 'screen'
		data['ram'] = 'ram'
		data['ssd'] = 'ssd'
		data['hhd'] = 'hhd'
		data['Type'] = 'type'
		data['model'] = 'model'
		data['os'] = 'os'
		data['DVD'] = 'DVD'
		data['keyboard'] = 'keyboard' 
		data['security'] = 'security'
		data['vc'] = 'vc'
		data['upc'] = 'upc'
		data['sku'] = 'sku'
		data['office'] = 'office'
		data['note'] = 'note'
		form = OutputForm(data)
		# print(data['price'])

		if form.is_valid():
			asin_list = []
			alldata = Output.objects.all()
			if Output.objects.exists():
				
				for i in alldata:
					asin_list.append(i.asin)
				if data['asin'] not in asin_list:
					obj = Output(price = data['price'].replace('$','').replace(',',''), asin = data['asin'], rank = re.sub("[^0-9]", "", data['rank'].replace('#','').replace(',','')), link = data['link'], date = data['date'])
					obj.save()
					alldata = Output.objects.all()
					messages.success(request, 'The Link was added successfully.')
			else:
				obj = Output(price = data['price'].replace('$','').replace(',',''), asin = data['asin'], rank = re.sub("[^0-9]", "", data['rank'].replace('#','').replace(',','')), link = data['link'], date = data['date'])
				obj.save()
				alldata = Output.objects.all()
				messages.success(request, 'The Link was added successfully.')
		elif data['price'] == None and data['asin'] != None:
			obj = Output(price = None, asin = data['asin'], rank = re.sub("[^0-9]", "", data['rank'].replace('#','').replace(',','')), link = data['link'], date = data['date'])
			obj.save()
			alldata = Output.objects.all()
			messages.success(request, 'The Link was added successfully.')
		elif data['rank'] == None and data['price'] == None and data['asin'] != None:
			obj = Output(price = None, asin = data['asin'], rank = None, link = data['link'], date = data['date'])
			obj.save()
			alldata = Output.objects.all()
			messages.success(request, 'The Link was added successfully.')
		elif data['rank'] == None and data['asin'] != None:
			obj = Output(price = data['price'].replace('$','').replace(',',''), asin = data['asin'], rank = None, link = data['link'], date = data['date'])
			obj.save()
			alldata = Output.objects.all()
			messages.success(request, 'The Link was added successfully.')
		else:
			print(form.is_valid())
			print(form.errors)
			alldata = Output.objects.all()
			messages.error(request, 'The Link was not add, please try again.')
		return render(request, 'polls/base.html', {'alldata': alldata})
	
	alldata = Output.objects.all()
	if 'price_sort' in request.POST:
		alldata = alldata.order_by('-price')
		flag = request.session.get('flag')
		flag = 'price'
		request.session['flag'] = flag
		return render(request, 'polls/base.html', {'alldata': alldata})

	elif 'rank_sort' in request.POST:
		
		alldata = alldata.order_by('rank')
		flag = request.session.get('flag')
		flag = 'rank'
		request.session['flag'] = flag
		return render(request, 'polls/base.html', {'alldata': alldata})

	elif 'date_sort' in request.POST:
		
		alldata = alldata.order_by('date')
		flag = request.session.get('flag')
		flag = 'date'
		request.session['flag'] = flag
		return render(request, 'polls/base.html', {'alldata': alldata})

	if request.method == 'POST' and 'update_bt' in request.POST:
		 
		i = 0
		asin = []
		temp = request.session.get('temp')
		flag = request.session.get('flag')
		if flag == 'price':
			alldata = Output.objects.all().order_by('-price')
			for j in alldata:
				asin.append(j.asin)
				print(j.asin)
			
		elif flag == 'rank':
			alldata = Output.objects.all().order_by('rank')
			for j in alldata:
				asin.append(j.asin)
				print(j.asin)
			
		elif flag == 'date':
			alldata = Output.objects.all().order_by('date')
			for j in alldata:
				asin.append(j.asin)
				print(j.asin)
			
		elif temp:
			for x in temp:
				asin.append(x)
				print(x)
			
		else:
			alldata = Output.objects.all()
			for j in alldata:
				asin.append(j.asin)
				print(j.asin)
		
		
		while i < len(request.POST.getlist('brand')):
			Output.objects.filter(asin = asin[i]).update(List = request.POST.getlist('list')[i])
			Output.objects.filter(asin = asin[i]).update(brand = request.POST.getlist('brand')[i])
			Output.objects.filter(asin = asin[i]).update(cpu = request.POST.getlist('cpu')[i])
			Output.objects.filter(asin = asin[i]).update(screen = request.POST.getlist('screen')[i])
			Output.objects.filter(asin = asin[i]).update(ram = request.POST.getlist('ram')[i])
			Output.objects.filter(asin = asin[i]).update(ssd = request.POST.getlist('ssd')[i])
			Output.objects.filter(asin = asin[i]).update(hhd = request.POST.getlist('hhd')[i])
			Output.objects.filter(asin = asin[i]).update(Type = request.POST.getlist('type')[i])
			Output.objects.filter(asin = asin[i]).update(model = request.POST.getlist('model')[i])
			Output.objects.filter(asin = asin[i]).update(os = request.POST.getlist('os')[i])
			Output.objects.filter(asin = asin[i]).update(DVD = request.POST.getlist('DVD')[i])
			Output.objects.filter(asin = asin[i]).update(keyboard = request.POST.getlist('keyboard')[i])
			Output.objects.filter(asin = asin[i]).update(security = request.POST.getlist('security')[i])
			Output.objects.filter(asin = asin[i]).update(vc = request.POST.getlist('vc')[i])
			Output.objects.filter(asin = asin[i]).update(upc = request.POST.getlist('upc')[i])
			Output.objects.filter(asin = asin[i]).update(sku = request.POST.getlist('sku')[i])
			Output.objects.filter(asin = asin[i]).update(office = request.POST.getlist('office')[i])
			Output.objects.filter(asin = asin[i]).update(note = request.POST.getlist('note')[i])

			i += 1
		
		request.session['flag'] = None	
		request.session['temp'] = None
		alldata = Output.objects.all()
		return render(request, 'polls/base.html', {'alldata': alldata})
		# # Output.objects.filter(brand = 'None').delete()
		# # print(request.POST['brand'])
	if 'refresh_bt' in request.POST:
		# temp = 0
		# while temp < request.POST.get('range'):
		# for i in range(int(request.POST.get('range_f')), int(request.POST.get('range_t'))):
		# 	print(i)
		# and request.POST.get('range_f') and request.POST.get('range_t')

		alldata = Output.objects.all()
		for i in alldata:
			if i.price == None:
				urls = i.link
				print(urls)
				myDate = datetime.now()
				formatedDate = myDate.strftime("%Y-%m-%d")
				headers = {
					'authority': 'www.amazon.com',
					'pragma': 'no-cache',
					'cache-control': 'no-cache',
					'dnt': '1',
					'upgrade-insecure-requests': '1',
					'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
					'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
					'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
					"apikey": "b50b92c0-afeb-11ea-9d8a-5dc1a2b8f2ee"
				}
				params = (
					("url", urls),
					# ("location", "na"),
					("premium", "true"),
					("location", "us"),
				)

				# Download the page using requests
				# print("Downloading %s"%url)
				# r = requests.get('https://app.zenscrape.com/api/v1/get', headers=headers, params=params)
				# r = requests.get(urls, headers=headers)
				r = requests.get('https://app.zenscrape.com/api/v1/get', headers=headers, params=params)
				# Simple check to check if page was blocked (Usually 503)
				if r.status_code > 500:
					if "To discuss automated access to Amazon data please contact" in r.text:
						print("Page %s was blocked by Amazon. Please try using better proxies\n"%urls)
					else:
						print("Page %s must have been blocked by Amazon as the status code was %d"%(urls,r.status_code))
					return None
				# Pass the HTML of the page and create
				# print(e.extract(r.text))
				# return e.extract(r.text)
				print(e.extract(r.text))
				data = e.extract(r.text)
				data['date'] = formatedDate
				data['link'] = urls
				if data['rank'] == None and data['price'] == None:
					Output.objects.filter(asin = i.asin).update(price = None, asin = data['asin'], rank = None, link = data['link'], date = data['date'])
				elif data['price'] == None:
					Output.objects.filter(asin = i.asin).update(price = None, asin = data['asin'], rank = re.sub("[^0-9]", "", data['rank'].replace('#','').replace(',','')), link = data['link'], date = data['date'])
				elif data['rank'] == None:
					Output.objects.filter(asin = i.asin).update(price = data['price'].replace('$','').replace(',',''), asin = data['asin'], rank = None, link = data['link'], date = data['date'])
				else:
					Output.objects.filter(asin = i.asin).update(price = data['price'].replace('$','').replace(',',''), asin = data['asin'], rank = re.sub("[^0-9]", "", data['rank'].replace('#','').replace(',','')), link = data['link'], date = data['date'])
			else:
				continue
		return render(request, 'polls/base.html', {'alldata': alldata})
	
	
	else:
		for row in Output.objects.all().reverse():
			if Output.objects.filter(asin=row.asin).count() > 1:
				row.delete()
		alldata = Output.objects.all()
		for i in alldata:
			if i.asin == None:
				Output.objects.filter(asin = i.asin).delete()
		request.session['flag'] = None	
		request.session['temp'] = None
		return render(request, 'polls/base.html', {'alldata': alldata})
	
def home(request):
	if request.method =='POST': 
		uploaded_file = request.FILES['fileToUpload']
		fs = FileSystemStorage()
		fs.save(uploaded_file.name, uploaded_file)
	return render(request, 'polls/home.html')












