#!/usr/bin/python3
"""
Contains class MyInt that inherits from int
Sneaky --> has == and != operators inverted!
"""


class MyInt(int):
    """Invert int operators == and !=."""
    def __eq__(self, value):
        """invert == operator"""
        return self.real != value

    def __ne__(self, value):
        """invert != operator"""
        return self.real == value
