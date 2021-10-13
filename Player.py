class Player:
    def __init__(self):
        self.starting_position = (400, 300)
        self.y = self.starting_position[1]
        self.direction = 0
        self.speed = 0
        self.maxSpeed = 20
        self.negativeVelocity = False
        try:
            #self.image = REPLACE THIS WITH THE SPRITE
            pass
        except:
            print "The main character sprite could not be found"
    def toString(self):
        return "Speed: " + str(self.speed) + " Direction: " + str(self.direction) + " Staring position: " + str(self.starting_position)
