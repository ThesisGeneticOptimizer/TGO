class Guest:
    totalguests = 0
    guests = []
    def __init__(self, name):
        self.name = name
        Guest.totalguests+=1
        Guest.guests.append(name)

    def displayName(self):
        return self.name

    def displayTotal(self):
        return Guest.totalguests
