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

    query = '''
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

####################################Column range function#######################################


def col_range(df):
    stats_df = df.describe().T
    stats_df['range'] = stats_df['max'] - stats_df['min']
    return stats_df

####################################Summary function for all columns#######################################


def summarize_df(df):
    '''
    This is a format function that prints out a summary of the data types and values in in each column
    '''
    print(f'This dataframe has {df.shape[0]} rows and {df.shape[1]} columns.')
    print('-------------------------------------------')
    print(df.info())
    print('-------------------------------------------')
    print(col_range(df))
    
############################Value Count function for Categorical Variables#####################################

    
def df_value_counts(df):
    '''
    Function that displays the value counts for all the categorical variables that I want to 
    display the value counts for
    '''
    cats = ['gender', 'senior_citizen', 'partner',
           'dependents', 'phone_service', 'multiple_lines',
           'paperless_billing', 'churn', 'contract_type', 'internet_service_type', 'payment_type']
    for col in df[cats]:
        print(df[col].value_counts())
        print("-----------------")