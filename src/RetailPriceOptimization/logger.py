import logging
import os

from datetime import datetime

import warnings
warnings.filterwarnings('ignore')

log_file_name = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_file_path = os.path.join(os.getcwd(), "logs", log_file_name)
os.makedirs(log_file_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(log_file_path, log_file_name)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)