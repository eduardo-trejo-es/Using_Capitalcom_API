#Imports
import requests
import json

import http.client
import pandas as pd

from pathlib import Path



####    Create_Session_Get_CTSandX-Security   ####

def Create_session_Capital_API(X_CAP_API_KEY):

    api_url = "https://api-capital.backend-capital.com/api/v1/session"
    credencial= {
    "identifier": "paginalalo9@gmail.com",
    "password": "MyCarPantera1?"
    }
    headers =  {'X-CAP-API-KEY': X_CAP_API_KEY,'Content-Type': 'application/json'}
    response = requests.post(api_url,data=json.dumps(credencial),headers=headers)
    print(response)
    print(response.headers)


def SavingDataPrices(From, to,csvFileName):
    HistoricalPriceRequests="/api/v1/prices/TWTR?resolution=HOUR&max=1000&from={}&to={}".format(From,to)
    ####    Historical_pricesCapitalAPI   ########
    conn = http.client.HTTPSConnection("api-capital.backend-capital.com")
    payload = ''
    headers = {'X-SECURITY-TOKEN': 'NHxRwiOzP8izsiiJdpBtTrmAKK4SUcC',
    'CST': '0tsoCV1tjHgbNr2BMKrFuYdz',
    'Content-Type': 'application/json'
    }
    conn.request("GET", HistoricalPriceRequests, payload, headers)
    res = conn.getresponse()
    data = res.read()
    data=data.decode("utf-8")

    data_json= json.loads(data)
    print(data_json)
    prices_Data=data_json['prices']

    #####      Saving Data In CSV file   ####

    columnsNames=["openPrice","closePrice","highPrice","lowPrice","lastTradedVolume"]
    DateIndexName=[]
    columnsValues=[]
    DataGrouped=[]
    for i in prices_Data:
        DateIndexName.append(i["snapshotTime"])
        columnsValues.append(i["openPrice"]["bid"])
        columnsValues.append(i["closePrice"]["bid"])
        columnsValues.append(i["highPrice"]["bid"])
        columnsValues.append(i["lowPrice"]["bid"])
        columnsValues.append(i["lastTradedVolume"])
        DataGrouped.append(columnsValues)
        columnsValues=[]

    df = pd.DataFrame(DataGrouped,index=DateIndexName, columns=columnsNames)
     
    try:
        existing=pd.read_csv(csvFileName, index_col="Unnamed: 0")
        #print(existing)
        #print(type(existing))
        existing = existing.append(df)
        print("was try")
        print(existing)
        existing.to_csv(path_or_buf=csvFileName,index=True)
        
    except :
        print("was execpt")
        df.to_csv(path_or_buf=csvFileName,index=True)
    
    


#Create_session_Capital_API('FTtqwDf12e08Fy0d')

SavingDataPrices("2022-09-01T06:00:00", "2022-09-06T21:00:00","TestingDataCSV.csv")