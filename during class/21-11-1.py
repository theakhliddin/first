class Graph:
    __slots__ = ['__xcor', '__ycor']
    def __init__(self, xcor, ycor):
        self.__xcor = xcor
        self.__ycor = ycor

    def getXcor(self):
        return self.__xcor
    def getYcor(self):
        return self.__ycor
    
    def setYcor(self, newYcor):
        self.__ycor = newYcor
    
    def __str__(self):
        return "****The x coord is: " + str(self.xcor) + " and the y coord is: " + str(self.ycor)
    def __repr__(self):
        return "The x coord is: " + str(self.xcor) + ", and the ycor is" + str(self.ycor)
    
    def __eq__(self, secondobj):
        if type(self)==type(secondobj):
            return self.__xcor == secondobj.__xcor
        else:
            return False
    def __ne__(self, secondobj):
        return not self.__eq__(secondobj)
    
    def __lt__(self, otherobj):
        return self.__ycor < otherobj.__ycor
    def __gt__(self, otherobj):
        return self.__ycor > otherobj.__ycor

def main():
    my_instance = Graph(4, 5)
    my_instance2 = Graph(6, 2)
    print(my_instance.getXcor())
    print("YCor before change: ", my_instance.getYcor())
    my_instance.setYcor(13.4)
    print("Ycor after changing the value: ", my_instance.getYcor())
    print(my_instance == my_instance2)
    print(my_instance != my_instance2)
    print(my_instance < my_instance2)
    print(my_instance > my_instance2)