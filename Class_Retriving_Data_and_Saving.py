#Imports
import requests
import json

import http.client
import pandas as pd

import datetime
import numpy as np

from pathlib import Path



####    Create_Session_Get_CTSandX-Security   ####


class CapitalAPI_Retriver_Piceses_Data:
    def __init__(self,X_CAP_API_KEY):
        Response=self.Create_session_Capital_API(X_CAP_API_KEY)
        self.X_SECURITY_TOKEN=Response['X-SECURITY-TOKEN']
        self.cst=Response['CST']

    def Create_session_Capital_API(self, X_CAP_API_KEY):

        api_url = "https://api-capital.backend-capital.com/api/v1/session"
        credencial= {
        "identifier": "paginalalo9@gmail.com",
        "password": "MyCarPantera1?"
        }
        headers =  {'X-CAP-API-KEY': X_CAP_API_KEY,'Content-Type': 'application/json'}
        response = requests.post(api_url,data=json.dumps(credencial),headers=headers)
        print(type(response.headers))
        
        return response.headers


    def SavingDataPrices(self,From, to,csvFileName):
        HistoricalPriceRequests="/api/v1/prices/TWTR?resolution=MINUTE&max=1000&from={}&to={}".format(From,to)
        ####    Historical_pricesCapitalAPI   ########
        conn = http.client.HTTPSConnection("api-capital.backend-capital.com")
        payload = ''
        headers = {'X-SECURITY-TOKEN': self.X_SECURITY_TOKEN,
        'CST': self.cst,
        'Content-Type': 'application/json'
        }
        
        conn.request("GET", HistoricalPriceRequests, payload, headers)
        res = conn.getresponse()
        data = res.read()
        data=data.decode("utf-8")

        data_json= json.loads(data)
        print(data_json)
        try:
            prices_Data=data_json['prices']
            self.saving_data(prices_Data,csvFileName)
        except:
            print(data_json)

        #####      Saving Data In CSV file   ####
    
    def saving_data(self, prices_Data,csvFileName):

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
    
    def generateBussinesDaysrange(self,Datefrom, Dateto):
        fromDates=[]
        Bdate=pd.bdate_range(start=Datefrom, end=Dateto)
        for i in Bdate:
            fromDates.append(i+np.timedelta64(3,'h'))
            
        toDates=[]
        for i in Bdate:
            toDates.append(i+np.timedelta64(14,'h'))
        return fromDates,toDates