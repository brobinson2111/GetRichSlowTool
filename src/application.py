import json
import os

class Application(object):

    def __init__(self):
        print("Application has been initialized...")
        self.__root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        self.__security_configurations_path = self.__root_dir + '/configuration/security_configurations.json'

    def run(self):
        print('Running Application...')
        with open(self.__security_configurations_path, "r") as security_configurations:
            data = json.load(security_configurations)
            print('This is the first entry in data: ' + json.dumps(data[0]))
