# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers 
from utils.urlfilter import BloomFilter
from zz.models import Raw,Fresh,Mature
from zz.task import add

import PIL.Image
import pytesseract
import Levenshtein
import urllib2
import json
import os
import imghdr
import shutil
import chardet
import time

bufferdir = os.getcwd()+"/temp"
# Create your views here.
#https://crab-net-storage.oss-cn-shanghai.aliyuncs.com/XskyWalkerForMac_1.4.dmg?Expires=1515736223&OSSAccessKeyId=LTAISyeSZ1BGuw1H&Signature=P15130werPRsEpMpv89UdKwjAzU%3D
def home(request):
	return render(request,'home.html')

def hotfilms(request):
	# Films.objects.all()
	# print serializers.serialize("json",Films.objects.all())
	s='我是中文';
	print chardet.detect(s)
	add.delay(2,2)
	return HttpResponse('aaaaaaa')

def addfilm(request):
	if request.POST:
		url1 = request.POST['url']
		title = request.POST['title']
		raw = Raw()
		raw.title = title
		raw.url = url1
		fileext = file_extension(title)
		filemain = file_main(title)
		msg={}
		print "before:"+GetNowTime()
		if(getHttpStatusCode(url1) == 200):#url存在
			print "after:"+GetNowTime()
			bf = BloomFilter()
			if bf.isContains(url1):
				msg['body'] = "url Already Exist!"
				print 'exists!'
				return HttpResponse(jsonreturn(msg,False))
			else:
				print 'url not exists!'
				newname1 = title
				newname1 = uniquename(bufferdir,filemain,fileext)
				print "before:"+GetNowTime()
				f = urllib2.urlopen(url1) 
				data = f.read()
				with open(bufferdir+"/"+newname1, "wb") as code:
					code.write(data)
					print "after:"+GetNowTime()
				print newname1
				raw.local_uri = bufferdir+"/"+newname1
				#可以对视频文件进行检查
				# av2image(os.getcwd()+'/'+newname1,os.getcwd()+'/pics')
				# keepdiff(os.getcwd()+'/pics',os.getcwd()+'/result')
				bf.insert(url1)
				raw.save();
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
def uniquename(dir,filename,ext):
	if os.path.exists(dir+'/'+filename+ext):
		filename1 = filename + '-copy'
		return uniquename(dir,filename1,ext)
	else:
		# print "filename is"+filename
		return filename+ext

def file_extension(path):  
    return os.path.splitext(path)[1] 
def file_main(path):  
    return os.path.splitext(path)[0] 

def av2image(avuri,picdir):
	tempdir = os.getcwd()+'/temp'
	# print tempdir
	if os.path.exists(picdir):
		shutil.rmtree(picdir)
	os.mkdir(picdir)
	ffmpeg = "ffmpeg -i "+avuri+" -r 2 "+ picdir + "/%04d.png"
	print (ffmpeg)
	os.system(ffmpeg)

def keepdiff(inputdir,outputdir):
	lasttext = ""
	stringratio = 0
	subdir = os.getcwd()+'/subpng'
	if os.path.exists(subdir):
		shutil.rmtree(subdir)
	os.mkdir(subdir)
	if os.path.exists(outputdir):
		shutil.rmtree(outputdir)
	os.mkdir(outputdir)
	print inputdir
	for files in os.walk(inputdir,True):
		newfiles = sorted(files[2])
		for pngfile in newfiles:
			fullsubpng = inputdir+"/"+str(pngfile)
			img = PIL.Image.open(fullsubpng)
			# print ('png file'+str(fullsubpng))
			region = (0,img.size[1]*5/6,img.size[0],img.size[1])
			cropImg = img.crop(region)
			# print ('crop png file'+str(subdir+"/"+pngfile))
			cropImg.save(subdir+"/"+pngfile)
	for files in os.walk(subdir):
		newfiles = sorted(files[2])
		for pngfile in newfiles:
			fullpng = subdir+"/"+str(pngfile)
			fullsubpng = inputdir+"/"+str(pngfile)
			txt = files[0]+"/"+str(pngfile)+".txt"
			print ('png file'+str(pngfile))
			if(fullpng.find("png",0,len(fullpng))>0):
				print ("------------"+pngfile+"-------------")
				image = PIL.Image.open(fullpng)
				image.load()
				vcode = pytesseract.image_to_string(image,lang='chi_sim')
				if(len(vcode)<2):
					os.remove(fullpng)
					os.remove(fullsubpng)
					print ("\033[1;31;40mtesseract see nothing\033[0m")
					continue
				# unicodea = lasttext.decode("ascii")
				# unicodeb = vcode.decode("ascii")
				print chardet.detect(str(vcode))
				# stringratio = Levenshtein.ratio(str(lasttext),str(vcode))
				print (lasttext)
				print ("vs-----vs----vs:"+str(stringratio))
				print (vcode)
				lasttext = vcode
				if(lasttext==str("")):
					print ("init wenben")
				elif(stringratio<0.9):
					print ("the string is very different!"+str(stringratio))
#						print vcode
				else:
					print ("\033[1;31;40mfile "+pngfile+" has been delete\033[0m")
					os.remove(fullpng)
					os.remove(fullsubpng)

def GetNowTime():
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
