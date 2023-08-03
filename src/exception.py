'''
built-in sys module, which provides access to various system-specific parameters and functions.
'''
import sys
from src.logger import logging

# get the error details 
def error_message_details(error, error_detail:sys):
    '''
    error: The error message that you want to include in the formatted error message.
    error_detail: sys: The sys module is passed to access the traceback information.
    The function uses sys.exc_info() to get the traceback information of the most recent exception. 
    It extracts the file name and line number where the error occurred and formats the error message 
    with this information.
    '''
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(file_name,
    exc_tb.tb_lineno, str(error))
    
    return error_message

'''
The CustomException class inherits from the built-in Exception class, making it a custom exception class.
'''
class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        '''
        The __init__ method: The constructor takes two parameters:
        error_message: The error message to be stored and later used in the formatted error message.
        error_detail: sys: The sys module is passed to access the traceback information.
        '''
        super().__init__(error_message)
        '''
        Inside the __init__ method, it calls the constructor of the base class (Exception) 
        using super().__init__(error_message). This sets the error message for the exception.
        '''
        self.error_message = error_message_details(error_message, error_detail=error_detail)


    def __str__(self):
        return self.error_message




