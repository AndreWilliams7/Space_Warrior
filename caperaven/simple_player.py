class SimplePlayer:
    def __init__(self, name, **kwargs):
        self.name = name
        self.vitality = 100
        self.armour = 100

        # check if vitality is in kwargs and if so change this instance's vitality
        # check if armour is in kwargs and if so change this instance's armour
        return

    def damage(self, value):
        if self.armour > 0:
            self.armour -= value  # same as "self.armour = self.armour - value"
            return  # we have damaged the armour do nothing else so exit function

        self.vitality -= value

        if self.vitality <= 0:
            self.die()

        return

    def die(self):
        print(self.name, "has died")


player = SimplePlayer("Andre")
player.damage(100) # breaks the armour
player.damage(100) # kill the player
