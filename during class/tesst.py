from area_test import *

def test_add(add):
    addResult = add(4,3)
    assert addResult==7

def test_min(subtract):
    subtractResult = subtract(4,3)
    assert subtractResult==1

def test_mult(multiple):
    multipleResult = multiple(4,3)
    assert multipleResult==12
    
def test_divi(devision):
    diviResult = division(4,3)
    assert diviResult==1