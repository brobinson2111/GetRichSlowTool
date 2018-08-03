'''
Created on August 2nd, 2018
Created By: Brandon Robinson (brobinson2111)
'''

import json
import logging
import os

from src.entities.security_info import SecurityInfo
from src.util import logger_config
from src.util import file_content_util

class Application(object):
    """
    This class behaves as the entrance to the application. It will be called with configurations from the CLI and
    perform all of the work for the application.
    """

    __logger = logging.getLogger('src.Application')
    __root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    __security_configurations_path = __root_dir + '/configuration/security_configurations.json'

    def __init__(self, total_capitol, number_of_days_to_spend, output_location):
        logger_config.set(self.__logger)
        self.__logger.info("Application has been initialized...")

        self.total_capitol = total_capitol
        self.number_of_days_to_spend = number_of_days_to_spend
        self.output_location = output_location

    def run(self):
        self.__logger.info('Running Application...')
        self.__logger.info('Starting Marshalling of Configurations.')
        security_info_list = self.__security_info_list()
        self.__logger.info('The amount of configurations after marshalling is: ' + str(len(security_info_list)))

        content_to_write = file_content_util.get_introduction(self.total_capitol, self.number_of_days_to_spend)
        for security_info in security_info_list:
            content_to_write.append(file_content_util.print_security_info(security_info))

        with open(self.output_location, 'w') as output_file:
            output_file.write(''.join(map(str, content_to_write)))


    def __security_info_list(self):
        with open(self.__security_configurations_path, "r") as security_configurations_file:
            security_configurations = json.load(security_configurations_file)
            self.__logger.info('This is the configuration used for this Application run: ' + json.dumps(security_configurations))
            return self.__marshall_configurations(security_configurations)


    def __marshall_configurations(self, security_configurations):
        marshalled_configurations = []
        for configuration in security_configurations:
            marshalled_configurations.append(
                SecurityInfo(configuration, self.total_capitol, self.number_of_days_to_spend))
        return marshalled_configurations