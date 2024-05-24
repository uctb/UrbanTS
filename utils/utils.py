import pandas as pd

def convert2UTC(dt:pd.Timestamp,city:str):
    return dt.tz_localize(city).tz_convert('UTC')

def convert2Local(dt:pd.Timestamp,city:str):
    return dt.tz_localize('UTC').tz_convert(city)