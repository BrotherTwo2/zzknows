# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from films.models import Raw,Fresh,Mature
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers 
from utils.urlfilter import BloomFilter

import urllib2
import json
import os
import imghdr

# Create your views here.
#https://crab-net-storage.oss-cn-shanghai.aliyuncs.com/XskyWalkerForMac_1.4.dmg?Expires=1515736223&OSSAccessKeyId=LTAISyeSZ1BGuw1H&Signature=P15130werPRsEpMpv89UdKwjAzU%3D
def home(request):
	return render(request,'home.html')

def hotfilms(request):
	# Films.objects.all()
	print serializers.serialize("json",Films.objects.all())
	return HttpResponse('aaaaaaa')

def addfilm(request):
	if request.POST:
		url1 = request.POST['url']
		title = request.POST['title']
		raw = Raw()
		raw.title = title
		raw.url = url1
		test = file_extension(title)
		msg={}
		if(getHttpStatusCode(url1) == 200):#url存在
			bf = BloomFilter()
			if bf.isContains(url1):
				msg['body'] = "url Already Exist!"
				print 'exits!'
				return jsonreturn(msg,False)
			else:
				print 'not exists!'
				filename('',)
				f = urllib2.urlopen(url1) 
				data = f.read()
				with open("demo2.zip", "wb") as code: 
					code.write(data)
				# bf.insert(url1)
				# raw.save();
				# return jsonreturn('',True)
				return HttpResponse(jsonreturn('',True))
		else:
			msg['body'] = "url are unreachable!"
			print("not equal")
			return jsonreturn(msg,False)
	return HttpResponse('aba')

import requests
def getHttpStatusCode(url):
    try:
        request = requests.get(url)
        httpStatusCode = request.status_code
        print (httpStatusCode)
        return httpStatusCode
    except requests.exceptions.HTTPError as e:
        return e
def jsonreturn(msg,success = True):
	ret={}
	if(success == True):
		ret['code'] = 200;
	else:
		ret['code'] = 500;

	ret['msg'] = msg;
	return json.dumps(ret)
def filename(dir,filename,ext):
	if os.path.exists(dir+'/'+filename+ext):
		filename(dir,filename+'_copy',ext)
	else:
		print "filename is"+filename
		return filename

def file_extension(path):  
    return os.path.splitext(path)[1] 
