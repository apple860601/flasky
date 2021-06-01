def PChomecrub(itname):    
    import requests
    from bs4 import BeautifulSoup
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    resq=requests.Session()
    import json
    import sqlite3
    import mysql.connector as mysql
    itemdb=mysql.connect(
    host = "127.0.0.1",
    user = "root",
    password = "apple80558",
    database='itemdb'
    )
    cursor=itemdb.cursor()
    sqlstr="drop table if exists PCitem"
    cursor.execute(sqlstr)
    sqlstr="create table IF NOT exists PCitem (shop char(7),name char(100), price char(10), URL char(150))"
    cursor.execute(sqlstr)
    resq2=resq.get(f"https://ecshweb.pchome.com.tw/search/v3.3/all/results?q={itname}&page=1&sort=sale/dc")
    ress=resq2.text
    jd=json.loads(ress)
    items=[]
    prices=[]
    urls=[]
    mainurl="http://24h.pchome.com.tw/prod/"
    for item in jd['prods']:
        itemname=item['name']
        itemprice=item['price']
        url=mainurl+item['Id']
        print (item['name'])
        print ("價格",item['price'])
        print("URL:",mainurl+item["Id"])
        sqlstr=f"insert into PCitem values('PChome','{itemname}','{itemprice}','{url}')"
        cursor.execute(sqlstr)
        itemdb.commit()

