__author__ = 'Serhii Kashuba kashubasv@gmail.com'

class GeometryException(Exception):

    def __init__(self, *args):
        self.args = args