import configparser
import os.path
import os
from .utils import *
class WorkPlace(object):
    workplace_name = ""
    path_path = ""
    __options__ = {}
    def __init__(self,workplace_name):

        self.workplace_name = workplace_name

        config = configparser.RawConfigParser()
        config.read('config.ini')

        base_dir = config['header']['WorkPlacePath']
        file_path = base_dir+self.workplace_name
        if os.path.isdir(file_path):
            self.path_path = file_path
            return

        os.mkdir(file_path)
        self.path_path = file_path
        print_info("Success to create workplace {}".format(self.workplace_name))

    def save(self,cache,module_name):
        pass
