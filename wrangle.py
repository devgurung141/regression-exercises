# imports

import pandas as pd
import numpy as np

import os
from env import get_connection

import warnings
warnings.filterwarnings("ignore")

from sklearn.model_selection import train_test_split

      
def wrangle_zillow():
    '''
    This function reads in zillow data from Codeup database using sql querry into a df, 
    return cleaned df
    '''
    
    
    querry = """
       SELECT bedroomcnt, bathroomcnt, calculatedfinishedsquarefeet, taxvaluedollarcnt, yearbuilt,    taxamount, fips 
       FROM properties_2017
       WHERE propertylandusetypeid = 261;
       """
    
    filename = "zillow.csv"
    
    # check if a file exits in a local drive
    #if yes, read data from a file
    if os.path.isfile(filename):
        df = pd.read_csv(filename)
    # if no, read data from database into a dataframe and write data frame into a CSV file.
    else:
        # read the SQL query into a dataframe
        df = pd.read_sql(querry, get_connection('zillow'))

        # Write that dataframe to disk for later. Called "caching" the data for later.
        df.to_csv(filename, index=False)
    
    # rename columns
    df = df.rename(columns= { 'bedroomcnt':'bedrooms',
                         'bathroomcnt': 'bathrooms',
                         'calculatedfinishedsquarefeet': 'sqft',
                         'taxvaluedollarcnt': 'tax_value',
                         'yearbuilt': 'year_built'
                        })
    
    # drop Null values
    df = df.dropna()
    
    # set seed
    seed = 42
    
    # split data into 80% train_validate, 20% test
    train_validate, test = train_test_split(df, test_size=0.2, 
                                            random_state=seed)
    
    # split train_validate data into 70% train, 30% validate
    train, validate = train_test_split(train_validate, test_size=0.3, 
                                       random_state=seed)
    
    # train, validate, test 
    return train, validate, test
    