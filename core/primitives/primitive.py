__author__ = 'serhii'

import json
import os

import logging

class Primitive:
    """ Superclass for all abstractions of physical objects
    """
    p_type = ""
    name = ""
    config = {}

    def log(self, text):
        print text

    def apply_config(self, values=None):
        if values is None:
            values = self.get_config(self.p_type, "default")
        for key in values:
            self.config[key] = values[key]


    def get_config(self, p_type, name, part=False):
        conf_data = {}

        conf = os.path.join("config", p_type, name + ".json" )
        config_path = os.path.join(os.path.dirname(__file__), '..', conf)
        config_path = os.path.abspath(config_path)

        with open(config_path) as conf:
            conf_data = json.load(conf)

        return conf_data


    def get_name(self):
        """
        :return: Object hash
        """
        return id(self)

    def accept(self, message):
        """
        Receive and handle message
        :param message: message object
        :return:
        """
        self.log("Node %s received message" % self.get_name())
        return True


    def log(self, m, level=logging.INFO):
        logging.info(m)