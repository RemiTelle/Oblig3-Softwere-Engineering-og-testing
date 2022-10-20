"""
Software Engineering og testing
Oblig 2 - Testing

Remi Telle 04/10/2022
"""

def isLeapYear(year):
    if (((year % 4) == 0) and ((year % 100) != 0)) or (year % 400 == 0):
        return True
    else:
        return False
