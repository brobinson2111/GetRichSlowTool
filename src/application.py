import json
import logging
import os

class Application(object):

    __logger = logging.getLogger('GetRichSlowTool')
    __root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    __security_configurations_path = __root_dir + '/configuration/security_configurations.json'

    def __init__(self):
        self.__set_logger_config()
        self.__logger.info("Application has been initialized...")

    def run(self):
        self.__logger.info('Running Application...')

        with open(self.__security_configurations_path, "r") as security_configurations:
            data = json.load(security_configurations)
            self.__logger.info('This is the first entry in data: ' + json.dumps(data[0]))


    def __set_logger_config(self):
        self.__logger.setLevel(logging.DEBUG)
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
        self.__logger.addHandler(file_handler)
        self.__logger.addHandler(console_handler)
