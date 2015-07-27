__author__ = 'Serhii Kashuba kashubasv@gmail.com'

class NodeBus():

    registered = {}

    def register(self, primitive):
        self.registered[primitive.get_name()] = primitive

    def broadcast(self, message):
        for pr in self.registered:
            self.registered[pr].accept(message)