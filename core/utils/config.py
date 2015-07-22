__author__ = 'Serhii Kashuba kashubasv@gmail.com'


class Config():

    data = {}

    def __init__(self):
        conf = os.path.join("config", "main.json")
        config_path = os.path.join(os.path.dirname(__file__), '..', conf)
        config_path = os.path.abspath(config_path)

        with open(config_path) as conf:
            conf_data = json.load(conf)

            self.data = conf_data
