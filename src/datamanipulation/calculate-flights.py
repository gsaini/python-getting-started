# from src.logexception.exceptionhandler import CustomUserException
# Error & Exception handling
import sys
import pandas

def calculate_flights(filename):
    data = pandas.read_csv(filename, nrows =1)
    print(data)
        

if __name__ == '__main__':

    calculate_flights(filename = sys.argv[1])