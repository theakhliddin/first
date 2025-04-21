class Bicycle:
    __slots__ = ['color', 'gears', 'seat', 'training_wheels']

    def __init__(self, color, seat):
        self.color = color
        self.gears = 21
        self.seat = seat
        self.training_wheels = False

bike = Bicycle('red', 'banana')
print(bike.training_wheels)