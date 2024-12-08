'''Activity 4 - Group 8
This activity requires us to implement a class in Python with appropriate methods,
attributes, and accessors. We use TDD to iteratively develop functionality, and
write pytest tests to validate class methods and attributes'''

# This is the link to Mohammed Eshaans's github repository : https://github.com/me3574/NoTrofy2.0
# This is the link to Mohammad Saad's github repository : https://github.com/ms5810/GCIS-Group-9.git
# This is the link to Akhliddin Koziboev's github repository : https://github.com/theakhliddin/first/tree/master
# This is the link to Danay Sultanov's github repository : https://github.com/ds4449/swag.inc.git

#Step 1 - Danay
'''Here we create a class, and constructors, define
getters (get_name), and setters (set_name).'''

class Polygon:
    def __init__(self,name="triangle",sides=[10,10,10]):
        self.name=name
        self.sides=sides
    def get_name(self):
        return self.name
    def get_sides(self):
        return self.sides
    def set_name(self, name):
        self.name=name
        return self.name
    def set_sides(self, sides):
        self.sides=sides
        return self.sides
    
    # Step 2 - Saad
    '''Implement equality and inequailty methods and 
    writing test codes '''

    def __eq__(self,other):
        if type(self)==type(other):
            if self.name==other.name and self.sides==other.sides:
                return True
        else:
            return False
    def __ne__(self,other):
        return not self.__eq__(other)
    
    #Step 3 - Akhliddin 
    '''Implementing the string (str) representation method'''

    def __str__(self):
        return self.name+" with sides: "+str(self.sides)
    
    #Step 4 & 5 - Eshaan
    '''Implementing the calculation and
    creating a main script'''
    
    def calculate_circumference(self):
        circumference=0
        for i in self.sides:
            circumference+=i
        return circumference

def main():
    poly1=Polygon("Triangle",[4,5,6])
    poly2=Polygon("Square",[4,4,4])
    poly3=Polygon("Hexagon",[4,5,6,7,8,9])
    poly=[poly1,poly2,poly3]
    for i in poly:
        print(i)
        print("Circumference is :",i.calculate_circumference())
    
if __name__=="__main__":
    main()