import os 
import re
from ETL import ETL_pipeline
lst = os.listdir()
OUT_DIR = 'outputs'
PROCESSED_DIR = 'processed'
for name in lst:
    string_pattern = '\.json'
    regex_pattern = re.compile(string_pattern)
    result = regex_pattern.findall(name)
    if len(result)!=0:
        print(name)
        ##.json exists
        ##call etl file
        ## if success remove the json
        df = ETL_pipeline(name)
        name_without_json = name.split('.')[0] ## to get the name without json 
        if not os.path.isdir(OUT_DIR):
            os.mkdir(OUT_DIR)
        df.to_csv(OUT_DIR+'/' + name_without_json+'.csv',index = False)
        
        ## move the file to processed folder:
        if not os.path.isdir(PROCESSED_DIR):
            os.mkdir(PROCESSED_DIR)
        os.rename(name , PROCESSED_DIR +'/'+name_without_json + '_processed.json')