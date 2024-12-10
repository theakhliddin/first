import polygon as poly

#Step 1 - Danay
'''Test code for the created class and 
constructors.'''

test_polygon="Triangle"
test_sides=[10,6,7]
def test_polygon_initialization():
    polygon=poly.Polygon(test_polygon,test_sides)
    assert polygon.name=="Triangle"
    assert polygon.sides==test_sides
    
def test_name_getter_setter():
    polygon=poly.Polygon(test_polygon,test_sides)
    assert polygon.get_name()=="Triangle"
    setter="Pentagon"
    assert polygon.set_name(setter)=="Pentagon"

def test_sides_getter_setter():
    polygon=poly.Polygon(test_polygon,test_sides)
    assert polygon.get_sides()==test_sides
    setter=[9,5,3]
    assert polygon.set_sides(setter)==[9,5,3]

#Step 2 - Saad 
'''Test code to check the equality and inequality '''

def test_polygon_equality():
    polygon=poly.Polygon(test_polygon,test_sides)
    test_poly=poly.Polygon(test_polygon,test_sides)
    assert test_poly==polygon
    
def test_polygon_inequality():
    polygon=poly.Polygon(test_polygon,test_sides)
    test_poly=poly.Polygon("Pentagon",[4,6,2,6,7])
    assert test_poly!=polygon

#Step 3 - Akhliddin 
'''Test code to represent the __str__ function '''    

def test_polygon_str():
    polygon=poly.Polygon(test_polygon,test_sides)
    test=test_polygon+" with sides: "+str(test_sides)
    assert polygon.__str__()==test

#Step 4 - Eshaan
'''Test code to check the calculation of
circumference '''

def test_polygon_circumference():
    polygon=poly.Polygon(test_polygon,test_sides)
    circ=sum(test_sides)
    assert polygon.calculate_circumference()==circ