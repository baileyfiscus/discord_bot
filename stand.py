class Stand:
    name
    user
    description
    __destructivePower
    __speed
    __range
    __durability
    __precision
    __developmentPotential

    standCount
    def __init__(self, name, user, description, destructivePower, speed, range, durability, precision, developmentPotential):
    self.name = name
    self.user = user
    self.description = description
    self.destructivePower = destructivePower
    self.speed = speed
    self.range = range
    self.durability = durability
    self.precision = precision
    self.developmentPotential = developmentPotential

    def die(self):
    
    def readInfo(self):
        return "|Stand Name| {}\n|Stand Master| {}\n|Description| {}\n|Destructive Power| {}\n|Speed| {}\n|Range| {}\n|Durability| {}\n|Precision| {}\n|Development Potential| {}\n".format(self.name, self.user, self.description, self.destructivePower, self.speed, self.range, self.durability, self.precision, self.developmentPotential)

    def change(self, var, newValue):
        self.var = newValue

    def howMany():
        return standCount