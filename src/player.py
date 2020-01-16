# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, currentRoom, name, description, playerItems=[]):
        self.currentRoom = currentRoom
        self.name = name
        self.description = description
        self.playerItems = playerItems
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
    def __str__(self):
        return f"{self.name}"
    def inventory(self):
        s = ''
        for x in self.playerItems:
            s += f"{x.name} - ({x.description})\n"
        return s