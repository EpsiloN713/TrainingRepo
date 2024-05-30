"""
Marc Lowenthal
Class: CS 521
Date: 12/4/2019
Class Object Example Mug.py
"""

import datetime
import sys


class Mug():
    """This class constructs the Mug Object and its contents"""

    def __init__(self, color, material='ceramic', contents='water'):
        self.__units = 'F'
        self.__tempf = None
        assert isinstance(material, str), 'material not string!'

        self.color = color
        self.material = material
        self.contents = contents
        # Keep track of the created timestamp as a private attribute
        self.__created_ts = datetime.datetime.now()

    def __str__(self):
        return ("Marc's {color} {mat} mug contains {cont} at {temp:,.1f}"
                " degrees {units} as of {ts}.".format(
            color=self.color,
            mat=self.material,
            cont=self.contents,
            temp=self.get_temp(),
            units='Fahrenheit' if self.__units == 'F' else 'Celsius',
            ts=self.__created_ts.strftime('%Y-%m-%d %H:%M:%S')))

    def set_as_fahrenheit(self):
        """set temperature units to Fahrenheit"""
        self.__units = 'F'
        return self

    def set_as_celsius(self):
        """set temperature units to Celsius"""
        self.__units = 'C'
        return self

    def set_temp(self, temp):
        """ set the temp of the mug contents"""
        if self.__units == 'F':
            self.__tempf = temp
        elif self.__units == 'C':
            self.__tempf = temp * 9 / 5 + 32
        else:
            assert False, 'Temperature Units Not Set'
        return self

    def __get_tempf(self):
        """return the temperature"""
        if self.__tempf is None:
            assert False, 'Temperature Not Set'
        return self.__tempf

    def __get_tempc(self):
        """return the temperature"""
        return (self.__tempf - 32) * 5 / 9

    def get_temp(self):
        """return the temperature"""
        if self.__units == 'F':
            return self.__get_tempf()
        elif self.__units == 'C':
            return self.__get_tempc()
        else:
            assert False, 'Temperature Units Not Set'


# Unit Tests
if __name__ == '__main__':

    temp = 212
    tempc = 100

    # instantiate mug object
    marc_mug = Mug('blue', contents='tea')

    # This will use __str__()
    # print(marc_mug)

    # set temperature
    marc_mug.set_temp(temp)

    # Test that get_tempf() is the same as just fetching that temp attribute
    if marc_mug.get_temp() != temp:
        print('Error setting temperature {} != {}'.format(marc_mug.get_temp(),
                                                          temp))
        sys.exit()

    # Same test but with assert
    assert marc_mug.get_temp() == temp, (
        'Error matching temperatures {} != {}'.format(marc_mug.get_temp(),
                                                      temp))

    marc_mug.set_as_celsius()
    assert marc_mug.get_temp() == tempc, (
        'Error matching temperatures {} != {}'.format(marc_mug.get_temp(),
                                                      temp))

    # This will use __str__()
    print(marc_mug)

    marc_mug.contents = 'hot chocolate'
    marc_mug.set_as_celsius()

    print(marc_mug)
