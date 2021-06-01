def retencrub(itname):
    import requests
    from bs4 import BeautifulSoup
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    resq=requests.Session()
    import json
    from fake_useragent import UserAgent
    import sqlite3
    import mysql.connector as mysql
    ua = UserAgent()
    headers = {
        'User-Agent': ua.random
    }
    itemdb=mysql.connect(
    host = "127.0.0.1",
    user = "root",
    password = "apple80558",
    database='itemdb'
    )
    cursor=itemdb.cursor()
    sqlstr="drop table if exists rutenitem"
    cursor.execute(sqlstr)
    cursor.execute("CREATE TABLE IF NOT exists rutenitem(shop char(7),name char(100), price char(10), URL char(150))")
    cookies={'_ts_id':"3705360E39093E0D3403.1576945008"}
    resq2=resq.get(f"https://rtapi.ruten.com.tw/api/search/v3/index.php/core/prod?q={itname}&type=direct&sort=rnk%2Fdc&offset=1&limit=48&2628348&_callback=jsonpcb_CoreProd",headers=headers)
    ress=BeautifulSoup(resq2.text,"html.parser")
    str1=resq2.text
    start=str1.find("Id")-3
    last=str1.find("catch")-4
    str2=str1[start:last]
    jd=json.loads(str2)
    for itemid in jd:
        resq3=resq.get(f"https://rtapi.ruten.com.tw/api/prod/v2/index.php/prod?id={itemid['Id']}&_callback=jsonpcb_Prod",headers=headers)
        str3=resq3.text
        start2=str3.find("ProdId")-3
        last2=str3.find("catch")-3
        str4=str3[start2:last2]
        jd2=json.loads(str4)
        itemname=jd2[0]['ProdName']
        itemprice=jd2[0]['PriceRange'][1]
        url="https://goods.ruten.com.tw/item/show?"+itemid['Id']
        print(url)
        print(jd2[0]['ProdName'])
        print("price:",jd2[0]['PriceRange'][1])
        print("")
        sqlstr=f"insert into rutenitem values('ruten','{itemname}','{itemprice}','{url}')"
        cursor.execute(sqlstr)
        itemdb.commit()