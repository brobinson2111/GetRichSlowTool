'''
Created on August 2nd, 2018
Created By: Brandon Robinson (brobinson2111)
'''

import logging

"""
Sets the provided logger for the application.

:logger The logger object to be configured.
"""  
def set(logger):
    logger.setLevel(logging.DEBUG)
    # create file handler which logs even debug messages
    file_handler = logging.FileHandler('application.log')
    file_handler.setLevel(logging.DEBUG)
    # create console handler with a debug level
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    # add the handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)