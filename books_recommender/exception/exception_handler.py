import os
import sys

class AppException(Exception):
    """
    AppException is customized exception class designed to capture refined details about exception
    such as python script file line number along with error message
    With custom exception one can easily spot source of error and provide quick fix.
    """

    def __init__(self, error_message: Exception, error_detail: sys):


