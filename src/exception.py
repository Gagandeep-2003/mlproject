# ======================================
# ⚠️ CUSTOM EXCEPTION HANDLER MODULE ⚠️
# ======================================
# This script defines a CustomException class that helps format error messages
# with rich context — including the filename, line number, and error text.
# It makes debugging easier in larger projects by producing clear, readable logs.

import sys  # Used to get detailed traceback info from the Python runtime
import logging

def error_message_detail(error, error_detail: sys):
    """
    Returns a detailed error message string that includes:
    - the file name where the error occurred
    - the line number
    - and the original error message
    """
    _, _, exc_tb = error_detail.exc_info()  # Get the traceback object
    file_name = exc_tb.tb_frame.f_code.co_filename  # Get file name where error occurred
    error_message = "Error occurred in python script name: [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)  # Format error details into a string
    )
    return error_message  # Return the full formatted error message

class CustomException(Exception):
    """
    Custom exception class to return a well-formatted error message
    using error_message_detail(). Inherits from Python's built-in Exception.
    """
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)  # Call the parent Exception constructor
        # Store the detailed error message
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        # When printed or logged, this will return the detailed error message
        return self.error_message


# if __name__ == "__main__":
#     try:
#         a=1/0
#     except Exception as e:
#         logging.info("Divide by Zero Error")
#         raise CustomException(e, sys)