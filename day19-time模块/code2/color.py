"""__author__ = 余婷"""
from random import randint


class Color:
    """颜色类"""
    white = 255, 255, 255

    @staticmethod
    def rand_color():
        return randint(0, 255), randint(0, 255), randint(0, 255)