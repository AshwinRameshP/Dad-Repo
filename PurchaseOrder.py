# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 00:25:18 2022
RATHISH MOTORS
@author: ashwin
"""
#Packages
import pandas as pd

def filter_PartNO(dataFrame):
    updated_dataFrame = dataFrame
    updated_dataFrame['PART NO'] = updated_dataFrame['PART NO'].str.split(r'\*|\s',expand=False).str[0]
    return updated_dataFrame

def QuantityCheck(dataframe):
    checkParts=dataframe[dataframe['Quantity'] in range(1,10) ]
    #checkParts=dataframe[dataframe['QTY']<0]
    print(checkParts)
    return 

if __name__ == "__main__":
    #Read Excel file
    df = pd.read_excel('PUR-ORDER-RATHISH-RISHABH-15.07.2024.xlsx')
    #print(df)
    #Pre-Processing
    updated_df = filter_PartNO(df)
    #print(updated_df)
    #QuantityCheck(updated_df)
    updated_df.to_excel("output.xlsx",index=False)
        



  