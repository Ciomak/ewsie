# -*- coding: utf-8 -*-

from enum import Enum

class Plec(Enum):
    M = 'Mężczyzna'
    K = 'Kobieta'
    
class Wiek(object):
    def __init__(self):
        self._18_25 = {
                  'name': '_18_25',
                  'verbose_name': '18-25',
                  'from': 18,
                  'to': 25,
                  }
        
        self._26_35 = {
                  'name': '_26_35',
                  'verbose_name': '26-35',
                  'from': 26,
                  'to': 35,
                  }
        
        self._36_45 = {
                  'name': '_36_45',
                  'verbose_name': '36-45',
                  'from': 36,
                  'to': 45,
                  }
        
        self._46_55 = {
                  'name': '_46_55',
                  'verbose_name': '46-55',
                  'from': 46,
                  'to': 55,
                  }
        
        self._GT_56 = {
                  'name': '_GT_56',
                  'verbose_name': '56+',
                  'from': 56,
                  'to': 150,
                  }