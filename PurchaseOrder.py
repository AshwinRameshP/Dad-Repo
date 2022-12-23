# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 00:25:18 2022
RATHISH MOTORS
@author: ashwin
"""
#Packages
import pandas as pd

def pre_process(dataFrame):
    updated_dataFrame = dataFrame
    updated_dataFrame['PART NO'] = updated_dataFrame['PART NO'].str.split().str[0]
    return updated_dataFrame

if __name__ == "__main__":
    #Read Excel file
    df = pd.read_excel('PUR-ORDER-RATHISH-NILESH-23.12.2022.xlsx')
    print(df)
    #Pre-Processing
    updated_df = pre_process(df)
    print(updated_df)
    #updated_df.to_excel("output.xlsx")
    


