# https://leetcode.com/problems/design-parking-system/description/

class ParkingSystem:
    __slots__ = ['vehicle']

    def __init__(self, big: int, medium: int, small: int):
        self.vehicle = [None,big,medium,small]

    def addCar(self, carType: int) -> bool:
        self.vehicle[carType] -= 1
        
        return self.vehicle[carType] > -1

