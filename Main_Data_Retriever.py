import datetime
import numpy as np
import time


import pandas as pd

from Class_Retriving_Data_and_Saving import CapitalAPI_Retriver_Piceses_Data



Capital_Retriver = CapitalAPI_Retriver_Piceses_Data ('iVxVv4E6D2Xl6YH4')
#2022-09-30

dates_From, DatesTo=Capital_Retriver.generateBussinesDaysrange("2018-03-26","2022-10-02")
#Capital_Retriver.SavingDataPrices("2020-02-25T03:00:00", "2020-02-25T10:00:00","Twttr/DataMinuteTwttr.csv")
for i in range(0,len(dates_From)):
    date_from=str(dates_From[i])
    date_from=date_from[:10]+"T"+date_from[11:]
    date_to=str(DatesTo[i])
    date_to=date_to[:10]+"T"+date_to[11:]
    print(date_from+" and "+date_to)
    print(date_from)
    print(date_to)
    time.sleep(1)
    Capital_Retriver.SavingDataPrices(date_from, date_to,"Twttr/DataHourTwttr.csv")

Capital_Retriver.Generating_Time_colum("Twttr/DataHourTwttr.csv","Twttr/TimeColumHOUR.csv")
    
print("done... :D")