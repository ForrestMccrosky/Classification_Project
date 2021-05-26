import pandas as pd
import numpy as np
import os
from env import host, user, password


#############################Connect To SQL database Function##############################

def sql_connect(db, user=user, host=host, password=password):
    '''
    This function allows me to connect the Codeup database to pull SQL tables
    Using private information from my env.py file.
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'


#############################Acquire Telco Customer Table from SQL##########################

def get_telco_data():
    '''
    This function connects to the SQL Codeup database and reads the customer table 
    from the Telco database into a pandas dataframe
    '''

    query = 
    '''
    SELECT *
    FROM customers
    JOIN contract_types USING(contract_type_id)
    JOIN internet_service_types USING(internet_service_type_id)
    JOIN payment_types USING(payment_type_id);
    '''

    df = pd.read_sql(query, sql_connect('telco_churn'))

    return df


################################Acquire Telco_Churn CSVs Lightspeed###############################

def get_telco_df(cached=False):
    '''
    This funciton is going to check if there is already a local csv file for the titanic data and pull the dataframe locally
    to be faster. If there is not a local file it is going to create a local csv file
    '''
    if cached == False or os.path.isfile('telco_churn.csv') == False:
        df = get_telco_data()
        df.to_csv('telco_churn.csv')
    else:
        df = pd.read_csv('telco_churn.csv', index_col=0)
    return df