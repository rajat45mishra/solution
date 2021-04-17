# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
"""import libs
pandas for dataframe and types also to generate csv file
timedelta for calculate diffrences for date 
sys for pass system args for filepath
if useing anaconda no need to install anything else install pandas using pip install pandas
"""
import sys
import pandas as pd
from datetime import timedelta

"""pass system args for filepath"""
filename=str(sys.argv[1])
"""read csv"""
df=pd.read_csv(filename)
"""initilize variable fval"""
Fval=1
"""forment date with pandas"""
df['date'] = pd.to_datetime(df['date']).dt.date
"""set dataframe index"""
df.set_index("date", inplace = True)
"""create new df from old df with filterd value Y"""
newdf = df[(df.value_overlayed == "Y")]
"""initialize variable n"""
n=0
"""initialize variable finalvalue"""
finalvalue=[]
"""start dataframe loop"""
for i,row in df.iterrows():
    """get Tval"""
    Tval=row['value']
    """apply condition for value_overlayed """
    if str(row['value_overlayed'])=='Y':
        """loop through newdf"""
        for f,v in newdf.iterrows():
            """initialize nc variable"""
            nc=i-f
            """initialize condition for n value"""
            if nc<=timedelta(days=365)and nc>=timedelta(days=0):
                """assign value for n"""
                n=nc
                """assign value for fval"""
                Fval=v['value']
        """assign value for reversal"""
        reversal=Tval-(Fval-150)*(365-n.days)
        """check condition for reversal"""
        if reversal<=450 and reversal>=150:
            """assign value for finalvalue if condition met"""
            finalvalue.append(reversal)
        else:
            """assign value for finalvalue if condition not met"""
            finalvalue.append(150)
    else:
        """assign value for finalvalue if condition not met"""
        finalvalue.append(row['value'])
"""df final value col"""
df['final_value']=finalvalue
"""generate csv of result"""
df.to_csv('result.csv')

