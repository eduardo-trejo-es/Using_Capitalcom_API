import datetime
import numpy as np
import time


import pandas as pd

from Class_Retriving_Data_and_Saving import CapitalAPI_Retriver_Piceses_Data



Capital_Retriver = CapitalAPI_Retriver_Piceses_Data ('33cyVAO5vCC6y9Fp')
#2022-09-30

#Capital_Retriver.SavingDataPrices("2020-02-25T03:00:00", "2020-02-25T10:00:00","Twttr/DataMinuteTwttr.csv")

Capital_Retriver.SavingDataPrices("OIL_CRUDE","2012-05-01T00:00:00", "2012-06-01T00:00:00","/Users/eduardo/Desktop/Using_Capitalcom_API/Day_Scope/CRUDE_OIL/DataHourCRUDE_OIL.csv")
 

    
print("done... :D")