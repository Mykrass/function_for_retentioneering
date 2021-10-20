#
import pandas as pd

def data_prep(df_raw):
    df_raw.drop(['location', 'locationid', 'segmentvalues'], axis=1, inplace=True)  # 100% missing data

    # select data
    select = ['devtodevid', 'eventtime', 'country', 'created', 'device',
              'deviceid', 'eventlevel', 'paymentcount', 'paymentsum',
              'tester', '_State', '_QuestId']
    df = df_raw[select].copy()
    df['devtodevid'] = df['devtodevid'].astype(str)
    df['eventtime'] = pd.to_datetime(df['eventtime'])
    df['date'] = pd.to_datetime(df['eventtime']).dt.date
    df['created'] = pd.to_datetime(df['created'])
    df['deviceid'] = df['deviceid'].astype(str)
    df['eventlevel'] = df['eventlevel'].astype(str)
    df['_QuestId'] = df['_QuestId'].astype(str)

    return DF