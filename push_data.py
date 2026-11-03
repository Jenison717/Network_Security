import os
import json
import sys
import pymongo
import pandas as pd
import certifi

from dotenv import load_dotenv
from src.exception.exception import CustomException

load_dotenv()
MONGO_DB_URI=os.getenv("MongoDB_URI")

ca = certifi.where()

class DataExtract:
    def __init__(self):
        pass
    
    def csv_to_json_convertor(self,file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records=list(json.loads(data.T.to_json()).value())
            return records
        
        except Exception as e:
            raise CustomException(e,sys)

    def insert_data_mongodb(self,records,database,collection):
        try:
            client = pymongo.MongoClient(MONGO_DB_URI,tlsCAFile=ca)
            db = client[database]
            collection =db[collection]
            collection.insert_many(records)
            return len(records)

        except Exception as e:
            raise CustomException(e,sys)

if __name__=="__main__":
    FILE_PATH = "D:\Network_Security\data\phisingData.csv"
    DATABASE = "JENISON_J"
    COLLECTION = "NetworkData"
    obj = DataExtract()
    records = obj.csv_to_json_convertor(FILE_PATH)
    count = obj.insert_data_mongodb(records,DATABASE,COLLECTION)
    print("Records inserted:",count)