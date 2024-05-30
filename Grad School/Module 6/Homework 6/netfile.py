"""
Author: Emeka Udogwu
Comment: MET CS 521 - Fall 2
Date: December 7 2019
Final Project
Function and Class Object for project
"""


def wildcard(octet):
    """Function that is used to calculate Wildcard"""
    # Add assert to make sure the correct Values are inputted
    assert octet > 0, "Octet Can not be negative"
    assert octet < 256, "Octet Can not be Higher than 255"
    result = 255 - octet
    return result


class Net_Check:
    """This Class Constructs the Net_Check object and its Contents"""

    def __init__(self, octet, netmask_override=None, ip_class=None):
        # Add assert to make sure the correct Values are inputted
        assert octet > 0, "Octet Can not be negative"
        assert octet < 256, "Octet Can not be Higher than 255"
        self.__octet = octet
        self.ip_class = ip_class
        self.netmask__override = netmask_override

    def __str__(self):
        """Prints out the Results for readability"""
        return "The IP Address is a {clas} address and has a {mask} Subnet " \
               "Mask" \
            .format(clas=self.get_class(),
                    mask=self.__get_netmask_override())

    def __repr__(self):
        return "{self.__class__.name__}".format(self=self)

    def get_oct(self):
        """Returns the octet"""
        return self.__octet

    def get_class(self):
        """Takes the Octet and finds out what class it belongs to"""
        first_oct = self.__octet
        if first_oct in range(1, 127):
            return "Class A"
        elif first_oct in range(128, 192):
            return "Class B"
        elif first_oct in range(192, 224):
            return "Class C"
        elif first_oct in range(224, 240):
            return "Class D"
        elif first_oct in range(240, 255):
            return "Class E"
        else:
            return "Not a Class"

    def __get_netmask_override(self):
        """Compares the class and returns the subnet mask """
        if self.get_class() == "Class A":
            return "/8"
        elif self.get_class() == "Class B":
            return "/16"
        elif self.get_class() == "Class C":
            return "/24"
        else:
            return "Reserved Class"


if __name__ == '__main__':
    # Test to make sure the correct error codes print
    test_oct = 300
    # Tests the Net_Check Class that was created
    test_net = Net_Check(test_oct)
    # Tests the wildcard function
    test_wild = wildcard(test_oct)
