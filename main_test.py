from main import isLeapYear


def test_isLeapYear_True_when_divisible_by_4_but_not_100():
    assert isLeapYear(4) == True
    assert isLeapYear(100) == False

def test_isLeapYear_True_when_divisible_by_400():
    assert isLeapYear(400) == True

def test_isLeapYear_False_when_not_divisible_by_4():
    assert isLeapYear(4) != False

def test_isLeapYear_False_when_divisible_by_100_but_not_400():
    assert isLeapYear(100) != True
    assert isLeapYear(400) != False
