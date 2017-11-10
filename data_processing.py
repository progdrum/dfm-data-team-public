import pandas as pd
from shared import db


def read_and_clean_data(path):
    """
    Receives a path to the CSV data file and reads and cleans 
    the data according to the data types defined in the model 
    in ucc_model.py.
    
    :param path: The path to the CSV file containing the data to be processed
    :return: A squeaky clean data frame, ready for database insertion
    """
    data = pd.read_csv(path)

    # Convert ID fields to strings (allows more than just numeric characters)
    data[['Customer ID', 'Campaign ID']] = \
        data[['Customer ID', 'Campaign ID']].astype(str)

    # Convert percentage string values to floats
    data[['Conv. rate', 'CTR', 'Search Lost IS (rank)', 'Interaction Rate']] = \
    data[['Conv. rate', 'CTR', 'Search Lost IS (rank)', 'Interaction Rate']]\
        .applymap(lambda x: float(x.rstrip('%').replace(',', '')))

    return data


def insert_into_db(table_name, clean_data):
    """
    Takes cleaned data and inserts it in the database.
    
    :param table_name: The name of the table to insert the data into
    :param clean_data: A data frame of sanitized data
    :return: None
    """
    clean_data.to_sql(table_name, db.engine)


def query_data():
    """
    Queries the database for the data in the table.
    
    :return: The requested data
    """
    pass
