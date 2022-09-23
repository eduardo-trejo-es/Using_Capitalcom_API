import datetime
import numpy as np
import time


import pandas as pd

from Class_Retriving_Data_and_Saving import CapitalAPI_Retriver_Piceses_Data



Capital_Retriver = CapitalAPI_Retriver_Piceses_Data ('7GqXIC9z32VU8xfR')

dates_From, DatesTo=Capital_Retriver.generateBussinesDaysrange("2020-04-10","2022-09-22")
#Capital_Retriver.SavingDataPrices("2020-02-25T03:00:00", "2020-02-25T10:00:00","Twttr/DataMinuteTwttr.csv")


for i in range(0,len(dates_From)):
    date_from=str(dates_From[i])
    date_from=date_from[:10]+"T"+date_from[11:]
    date_to=str(DatesTo[i])
    date_to=date_to[:10]+"T"+date_to[11:]
    print(date_from+" and "+date_to)
    time.sleep(1)
    Capital_Retriver.SavingDataPrices(date_from, date_to,"Twttr/DataMinuteTwttr.csv")
    
    
print("done... :D")