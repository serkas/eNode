__author__ = 'Serhii Kashuba kashubasv@gmail.com'



class Message():

    DEFAULT = "default_m"
    TIME = "time_m"

    value = None
    message_type = DEFAULT

    def __init__(self, message_tepe, value):
        self.message_type = message_tepe
        self.value = value

    def type_of(self, check_type):
        return check_type == self.message_type