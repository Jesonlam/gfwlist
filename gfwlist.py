# -*- coding: utf-8 -*-

import os,base64,sys
import urllib
import requests
import string

url = 'https://raw.githubusercontent.com/gfwlist/gfwlist/master/gfwlist.txt'
print = "downloading with GFWList"
urllib.request.urlretrieve (url,"gfw_list.txt")

gfw_list = "gfw_list.txt"
oneself=r"oneself.txt"
gfwlist=r"gfwlist.txt"

def Tofile(txt,file):
    with open(txt,'r') as fileObj:
        base64_data = fileObj.read()
        gfw_list_txt = base64.b64decode(base64_data)
        gfw_name = open(file,'wb')
        gfw_name.write(gfw_list_txt)
        gfw_name.close()

Tofile("./gfw_list.txt",'gfw_list.txt')

fpa=open(gfw_list)
fpb=open(oneself)
fpc=open(gfwlist,"w")
 
arrB=[]
for lineb in fpb.readlines():
    arrB.append(lineb)
 
index=0
for linea in fpa.readlines():
    index=index+1
    fpc.write(linea)
    for i in range((index-1)*10,(index)*10):
        try:
           fpc.write(arrB[i])
        except:
            pass

fpa.close()
fpb.close()
fpc.close()

def ToBase64(file, txt):
    with open(file, 'rb') as fileObj:
        gfwlist_name = fileObj.read()
        base64_data = base64.b64encode(gfwlist_name)
        fout = open(txt, 'w')
        fout.write(base64_data.decode())
        fout.close()

ToBase64("./gfwlist.txt",'gfwlist.txt') 