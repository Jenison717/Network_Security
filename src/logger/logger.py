import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log" # create a file using this format
log_path = os.path.join(os.getcwd(),"logs")                      # Specifies where the folder should be created. 
os.makedirs(log_path,exist_ok=True)                              # if the log_path already exist it wont raise any error

LOG_FILE_PATH = os.path.join(log_path,LOG_FILE)                  # overall file path

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)