class Bicycle:
    __slots__ = ['name', 'color', 'gears', 'seat', 'training_wheels', 'streamers']

    def __init__(self, color, seat, streamers = False):
        self.color = color
        self.gears = 21
        self.seat = seat
        self.training_wheels = False
        self.streamers = streamers

    def ride(self, name):
        print(name,"rides their", self.color ,"bicycle with", self.gears, "gears and a", self.seat, "seat.")
    
bike = Bicycle('red', 'banana', streamers=True)
bike.ride('Alex')

def main():
    bike = Bicycle('blue', 'racing')
    bike.ride('Jordan')

if __name__ == "__main__":
    main()
    