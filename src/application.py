'''
Created on August 2nd, 2018
Created By: Brandon Robinson (brobinson2111)
'''

import json
import logging
import os

from src.util import logger_config

class Application(object):
    """
    This class behaves as the entrance to the application. It will be called with configurations from the CLI and
    perform all of the work for the application
    """

    __logger = logging.getLogger('src.Application')
    __root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    __security_configurations_path = __root_dir + '/configuration/security_configurations.json'

    def __init__(self):
        logger_config.set(self.__logger)
        self.__logger.info("Application has been initialized...")

    def run(self):
        self.__logger.info('Running Application...')

        with open(self.__security_configurations_path, "r") as security_configurations:
            data = json.load(security_configurations)
            self.__logger.info('This is the first entry in data: ' + json.dumps(data[0]))