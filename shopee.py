#coding=utf-8
import requests
import sqlite3
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
resq=requests.Session()
import json
from fake_useragent import UserAgent 
itemdb=sqlite3.connect(r"C:\Users\applejimmy\Desktop\SHOP CRUB\itemdb2.db")
cursor=itemdb.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS item('shop' ,'name', 'price' , 'URL' )")
#objnm=pd.read_excel(r'C:\Users\applejimmy\Desktop\SHOP CRUB')
#print(objnm.iloc[1,0])
#keyword=objnm.iloc
ua = UserAgent()
headers = {
    'User-Agent':ua.random,
    "accept":"*/*","accept-language":"zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,fr;q=0.6,zh-CN;q=0.5,ja;q=0.4","if-none-match-":"55b03-8d0921efa26ce36dc7e5d22dd3809627","sec-fetch-mode":"cors","sec-fetch-site":"same-origin","x-api-source":"pc","x-requested-with":"XMLHttpRequest",
    "cookie": 'SPC_IA=-1; SPC_EC=-; SPC_F=OW8PBHY2MY7Mh3Kj5edr7aqocMOL9BHK; REC_T_ID=fb66e424-12be-11ea-ba19-f8f21e1ab3e0; SPC_U=-; _gcl_au=1.1.1066991571.1575042205; cto_lwid=9dfc81e6-2d9e-4eb8-b68a-0fbc1df4c800; __BWfp=c1575042208137xd58dbafb1; _ga=GA1.2.159683728.1576165839; _med=refer; SPC_SI=9ovcrqg8qc9ohsmipjz600vr4ywu5qi7; AMP_TOKEN=%24NOT_FOUND; _gid=GA1.2.2147462459.1578991202; csrftoken=SRntjTlmen5QDjlP8orKsBEY7g5Hgp9q; REC_MD_41_1000020=1578991504_0_50_0_15; REC_MD_20=1578991229; REC_MD_30_2000657904=1578991263; welcomePkgShown=true; SPC_T_IV="FXIpPeZNIdtWLl776wg4MQ=="; SPC_T_ID="qN6OKlrKC8J988jXgl+oDiK2Uk+TPUYtftx/Ktj0FHP/FVAQ99KVwR16ZG6TRNcD9l4DyKydeILBWH3GjNFE1cc3lFqYRbQEgBMiPuN5Gt0="',
    'if-none-match-': "55b03-8d0921efa26ce36dc7e5d22dd3809627"
}
resq2=resq.get(f"https://shopee.tw/api/v2/search_items/?by=relevancy&keyword=GSP600&limit=50&newest=0&order=desc&page_type=search&version=2",headers=headers,allow_redirects=False)
ress=resq2.text
jd=json.loads(ress)
# items=[]
# prices=[]
# urls=[]
mainurl='https://shopee.tw/'
for item in jd['items']:
    if item['ads_keyword']==None:
        itemname=str(item['name'])
        itemprice=str(int(item['price'])/100000)
        print(item['flag'])
        url=mainurl+item['name']+"-i."+str(item['shopid'])+"."+str(item['itemid'])
        print(url)
        print("price:",itemprice)
        print("")
        sqlstr=f"insert into item values ('shopee','{itemname}','{itemprice}','{url}')"
        cursor.execute(sqlstr)
        itemdb.commit()
cursor.close   

# for item in jd['items']:
#     for item2 in item
#     if item['ads.keyword']==0:
#         print (item['name'])
    