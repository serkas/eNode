__author__ = 'Serhii Kashuba kashubasv@gmail.com'
import math

class rfModel():

    DB = "DB"
    TIMES = "TIMES"

    c = 3 * math.pow(10, 8)

    def attenuation(self, freq, distance, value_type="TIMES"):
        attenuation = 4 * math.pi * freq * distance / self.c

        if value_type == self.DB:
            return 10 * math.log10(attenuation)
        return attenuation