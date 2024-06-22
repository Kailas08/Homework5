class House:
    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.floors = floors
        self.numberOfFloors = floors
        print(self.numberOfFloors)

h_1 = House()
h_1.setNewNumberOfFloors(7)