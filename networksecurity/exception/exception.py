# Import the sys module to access system-specific parameters and functions
import sys
# Import the logger from the logging module in the networksecurity package
from networksecurity.logging import logger

# Define a custom exception class for network security errors
class NetworkSecurityException(Exception):
    # Initialize the exception with an error message and error details
    def __init__(self, error_message, error_details: sys):
        # Store the error message
        self.error_message = error_message
        # Extract the traceback information from the error details
        _, _, exc_tb = error_details.exc_info()

        # Get the line number where the exception occurred
        self.lineno = exc_tb.tb_lineno
        # Get the file name where the exception occurred
        self.file_name = exc_tb.tb_frame.f_code.co_filename

    # Define the string representation of the exception
    def __str__(self):
        return "error occurred in python script name[{0}] line number [{1}] error message [{2}]".format(
            self.file_name, self.lineno, str(self.error_message))

# Test block to demonstrate the exception handling
if __name__ == '__main__':
    try:
        # Log the entry into the try block
        logger.logging.info("enter the try block")
        # Intentionally cause a division by zero error
        a = 1 / 0
        # This line will not be printed due to the error
        print("this will not be printed", a)
    except Exception as e:
        # Raise the custom exception with the caught exception details
        raise NetworkSecurityException(e, sys)
