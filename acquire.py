#!/usr/bin/env python
# coding: utf-8

# In[8]:


# List of imports

import pandas as pd
import numpy as np
import os
from env import host, username, password


def get_connection(db, user=username, host=host, password=password):
    '''
    This function accesses my .csv file for telco
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'
    
def new_telco_data():
    '''
    This function creates a query that joins contract types, internet service types
    and payment types tables to the customers table
    '''
    sql_query = """
                select * from customers
                join contract_types using (contract_type_id)
                join internet_service_types using (internet_service_type_id)
                join payment_types using (payment_type_id)
                """
    
    # Accessing the telco_churn database
    df = pd.read_sql(sql_query, get_connection('telco_churn'))
    
    return df

def get_telco_data():
    '''
    This function creates a .csv file for the telco db
    '''
    if os.path.isfile('telco.csv'):
        
        # If the csv file exists make it the df
        df = pd.read_csv('telco.csv', index_col=0)
        
    else:
        
        # Set the dataframe equal to the new_telo_data
        df = new_telco_data()
        
        # Cache data
        df.to_csv('telco.csv')
        
    return df


# In[ ]:




