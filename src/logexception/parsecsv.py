# from src.logexception.exceptionhandler import CustomUserException
# Error & Exception handling
import os
import sys
import logging
import logframework
from CustomException import CustomException

logger = logging.getLogger('parsecsv')
def parse_csv_and_get_columns(filename):
    if os.path.isfile(filename):
        csvFile = open(filename, 'r')
        lines = csvFile.readlines()
    else:
        raise CustomException('Given file isn\'t available')

    for line in lines[1:]:
        val = line.split(',')

        try:
            test_zero_div =  (int(val[0]) / int(val[11]))
            print(test_zero_div)

        except TypeError:
            logger.error('Exception Occured TypeError')
            raise CustomException('Invalid Types')
        except ZeroDivisionError:
            logger.error('Exception Occured ZeroDivisionError')
        except ValueError:
            logger.error('Exception Occured ValueError')    

if __name__ == '__main__':

    logframework.setup_logging()
    logger.info('input File: ' + sys.argv[1])
    parse_csv_and_get_columns(filename = sys.argv[1])