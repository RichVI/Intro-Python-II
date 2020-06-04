# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = "invalid"
        self.s_to = "invalid"
        self.e_to = "invalid"
        self.w_to = "invalid"