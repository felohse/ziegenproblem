class Gate:

    def __init__(self):
        self.is_opened = False
        self.has_ziege = False

    def open(self):
        return self.has_ziege

    def set_ziege(self):
        self.has_ziege = True