from src.RetailPriceOptimization.logger import logging
from src.RetailPriceOptimization.exception import CustomException
import sys

if __name__=="__main__":
    logging.info("The Execution has started")

    try:
        pass

    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)