#Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 08:06:12) [MSC v.1900 64 bit (AMD64)] on win32
#Type "copyright", "credits" or "license()" for more information.
#！/user/bin/python
#-*- coding:utf-8 -*-
import os
def gci(filepath):
    #遍历filepath下所有文件，包括子目录
	files=os.listdir(filepath)
	for fi in files:
		fi_d=os.path.join(filepath,fi)
		if os.path.isdir(fi_d):
			gci(fi_d)
		else:
			print os.path.join(filepath,fi_d)

