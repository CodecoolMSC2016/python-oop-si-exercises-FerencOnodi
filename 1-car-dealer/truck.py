from vehicle import Vehicle


class Truck(Vehicle):

    def __init__(self):
        self.ccm = None
        self.top_speed = None
        self.carry_limit = 0
        self.current_carriage_weight = 0

    def has_carriage(self):
        return self.current_carriage_weight > 0

    def attach_carriage(self, weight):
        result = self.current_carriage_weight + weight
        return result <= self.carry_limit

    def detach_carriage(self):
        self.current_carriage_weight = None
        return self.current_carriage_weight
