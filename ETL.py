import os
import argparse
import numpy as np
import pandas as pd


def process_meta_data(df):
    if 'meta-data' in df.columns:
        for record in (df[df['meta-data'].astype('|S') != b'nan'].iterrows()): # which will by default set the length to the max len it encounters
            dict_meta_data = ( record[1]['meta-data'] ) ## 1 as it is tuple with 0 the key and 1 the values
            for key,value in dict_meta_data.items():
                df.loc[record[0],key] = record[1]['meta-data'][key]
                #print(df.loc[record[0],key])
                

def ETL_pipeline(path = 'tagaddod-d8ffe--MsZkGFSCtYxntenMuVF-export.json'):
    df = pd.read_json(path) 
    df = df.T ## to edit the format
    
    if 'meta-data' in df.index:
        collector_id = df.loc['meta-data']['collector_id']
        df['collector_id'] = collector_id 
        df.drop(index= 'meta-data',inplace = True)
    
    df['latitude'] = pd.to_numeric(df['latitude'])
    df['longitude'] = pd.to_numeric(df['longitude'])
    df['snapshot_datetime'] = pd.to_datetime(df['snapshot_datetime'])#,format='%y-%m-%d %H:%M:%S')#.%f')
    
    if 'meta-data' in df.columns:
        process_meta_data(df)
        df.drop(columns = ['meta-data'] , inplace = True)
    return df


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--in_path', type=str, required=True)
    parser.add_argument('--out_path', type=str, default= '')
    args = parser.parse_args()
    df = ETL_pipeline(args.in_path)
    name = args.in_path.split('/')[-1].split('.')[0] ## to get the name without json 
    df.to_csv(args.out_path+'/'+name+'.csv',index = False)
    
    
if __name__ == '__main__':
    main()
    
    