from vehicle import Vehicle


class Car(Vehicle):

    def __init__(self):
        self.ccm = None
        self.top_speed = None
        self.is_running = None

    def start_engine(self):
        self.is_running = True

    def stop_engine(self):
        self.is_running = False
