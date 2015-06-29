__author__ = 'serhii'

import json


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
        with open("/".join(["config", p_type, name + ".enode" ])) as conf:
            conf_data = json.load(conf)

        return conf_data