import pandas as pd
from shared import db
from ucc_model import UsedCarCampaign


def read_and_clean_data(path):
    """
    Receives a path to the CSV data file and reads and cleans 
    the data according to the data types defined in the model 
    in ucc_model.py.
    
    :param path: The path to the CSV file containing the data to be processed
    :return: A squeaky clean data frame, ready for database insertion
    """
    data = pd.read_csv(path)

    # Add ID column
    # data.insert(0, 'id', range(1, 1 + len(data)))

    # Convert ID fields to strings (allows more than just numeric characters)
    data[['Customer ID', 'Campaign ID']] = \
        data[['Customer ID', 'Campaign ID']].astype(str)

    # Convert percentage string values to floats
    data[['Conv. rate', 'CTR', 'Search Lost IS (rank)', 'Interaction Rate']] = \
    data[['Conv. rate', 'CTR', 'Search Lost IS (rank)', 'Interaction Rate']]\
        .applymap(lambda x: float(x.rstrip('%').replace(',', '')))

    # Close parenthesis on a column is causing an issue
    data = data.rename(columns={'Search Lost IS (rank)': 'Search Lost IS <rank>'})

    # Also, write the results to a CSV
    data.to_csv('clean_test_report.csv')

    return data


def insert_into_db(table_name, clean_data):
    """
    Takes cleaned data and inserts it in the database.
    
    :param table_name: The name of the table to insert the data into
    :param clean_data: A data frame of sanitized data
    :return: None
    """
    for index, row in clean_data.iterrows():
        row_to_add = UsedCarCampaign(day=row[0],
                                     customer_id=row[1],
                                     campaign_id=row[2],
                                     campaign=row[3],
                                     campaign_state=row[4],
                                     campaign_serving_status=row[5],
                                     clicks=row[6],
                                     start_date=row[7],
                                     end_date=row[8],
                                     budget=row[9],
                                     invalid_clicks=row[10],
                                     budget_explicitly_shared=row[11],
                                     label_ids=row[12],
                                     labels=row[13],
                                     conversions=row[14],
                                     conv_rate=row[15],
                                     ctr=row[16],
                                     cost=row[17],
                                     impressions=row[18],
                                     search_lost_is=row[19],
                                     avg_position=row[20],
                                     interaction_rate=row[21],
                                     interactions=row[22])
        db.session.add(row_to_add)
        db.session.commit()


def query_data():
    """
    Queries the database for the data in the table.
    
    :return: The requested data
    """
    rows = UsedCarCampaign.query.all()
    return [result.__dict__ for result in rows]
