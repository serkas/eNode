__author__ = 'serhii'

import json
import os

class Primitive:
    """ Superclass for all abstractions of physical objects
    """

    config = {}

    def log(self, text):
        print text

    def apply_config(self, values):
        for key in values:
            self.config[key] = values[key]


    def get_config(self, p_type, name, part=False):
        conf_data = {}

        conf = os.path.join("config", p_type, name + ".enode" )
        config_path = os.path.join(os.path.dirname(__file__), '..', conf)
        config_path = os.path.abspath(config_path)

        with open(config_path) as conf:
            conf_data = json.load(conf)

        return conf_data