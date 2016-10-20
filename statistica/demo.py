import pandas as pd
from stopnie.models import *
import pygal
import datetime
from datetime import date
import functools

def createDataFrame():
    kandydat = pd.DataFrame.from_records(Kandydat.objects.all().values())
    stopien = pd.DataFrame.from_records(Stopien.objects.all().values())
    kierunek = pd.DataFrame.from_records(Kierunek.objects.all().values())
    
    df = kandydat.merge(stopien, left_on='stopien_id', right_on='id').merge(kierunek, left_on='kierunek_id', right_on='id')
    
    return df


choices =   {
            'data_rej': 0,
            'kierunek_id': 0
            }

def createChart():
    pass

def filterDataFrame(df, **kwargs):
    criterias = []
    for key, value in kwargs.iteritems():
        if key == 'kierunek_id':
            if value != 0:
                criterias.append(df[key]==value)
        elif key == 'data_rej':
            if value != 0:
                criterias.append(df[key] >= (datetime.datetime.now()-datetime.timedelta(days=value)))
              
    if not criterias:
        return df
    
    allCrit = functools.reduce(lambda x,y: x & y, criterias)
    
    return df[allCrit]
    
df1 = filterDataFrame(createDataFrame(), **choices)