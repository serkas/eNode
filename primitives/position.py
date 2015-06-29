__author__ = 'serhii'


class Position():

    x_axe = 0
    y_axe = 0
    z_axe = 0

    rotation = 0

    def get_position(self):
        return (self.x_axe, self.y_axe, self.z_axe)


    def set_position(self, x_axe, y_axe, z_axe=0):
        self.x_axe = x_axe
        self.y_axe = y_axe
        self.z_axe = z_axe

        return True