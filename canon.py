
import colorama
from colorama import Back, Fore, Style
import time

class Canon:
    canonsList = []
    def __init__(self,xCoordinate,yCoordinate):
        self.coordinates = [xCoordinate,yCoordinate]
        self.health = 10
        self.occupied = False  # Is cannon free?
        self.victim = None     # wth; Maybe who attacks the object? No. Something else.
        self.target = None     # Target it shoots?
        self.init = time.time()
        self.death = False     # Was cannon destroyed?

    def render(self,colorArray,):
        # Rendering has set a cannon image on the board.
        ## canons
        if(self.health>0):
            self.color = Back.BLACK + " " + Style.RESET_ALL
        else:
            self.color = Back.LIGHTBLACK_EX + "  " + Style.RESET_ALL
            self.death = True

        colorArray[self.coordinates[0]][self.coordinates[1]] = self.color
        return colorArray

    def idUpdate(self, idArray):
        idArray[self.coordinates[0]][self.coordinates[1]] = 3
        return idArray

    def shoot(self,king,Barbarians):
        min_distance = 10
        print(self.occupied)
        
        self.target = None
        if(self.victim!=None):
            # Prints stuff if victim is in range? How it is different from target?
            if(abs(self.victim.coordinates[0]-self.coordinates[0])<5 
                    and abs(self.victim.coordinates[1]-self.coordinates[1])<5):
                print('yess')

            # The victim went out of range.
            else:
                print('nooo')
                self.victim = None  # Redundant
                self.occupied = False # It is free.
       
       if(abs(king.coordinates[0]-self.coordinates[0])<5 and 
               abs(king.coordinates[1]-self.coordinates[1])<5 
               and king.death == False):
            # If alive king is in range? 
            distance = abs(king.coordinates[0]-self.coordinates[0])
            + abs(king.coordinates[1]-self.coordinates[1])
            # Change min_distance? But why?
            # Target of cannon is a king.

            # Also we are checking for distance twice.
            if(distance<min_distance):
                min_distance = distance
                self.target = king

        for barbarian in Barbarians.barbariansList:
            if(abs(barbarian.coordinates[0]-self.coordinates[0])<5 and 
                    abs(barbarian.coordinates[1]-self.coordinates[1])<5):
                # If a barbarian is in range:
                distance = abs(barbarian.coordinates[0]-self.coordinates[0]) + 
                abs(barbarian.coordinates[1]-self.coordinates[1])
                # And it is alive
                # Again why change min_distance?
                # And target barbarian.
                if(barbarian.death == False):
                    if(distance<min_distance):
                        min_distance = distance
                        self.target = barbarian

        # Targeted only a single attacker
        # Why even target if occupied?
        # Ok. we 'target' the closest soldier


        '''Idea was
        1) Check if there was a victim.
        2) Check if it is in range. (Should check for death.)
        3) Select best target, (closest ig).
        4) If victim existed/cannon was free, switch to new victim=target.
        5) If cannon was not free - continue fire if victim is in range. If not in range switch to target.
        '''
        print(self.target)
        if(self.target!=None):
            # If cannon was free,
            if(self.occupied==False):
                self.victim = self.target # Why we need both?
                self.occupied = True
            
                if(min_distance<10):      # It should be distance, right? As min_distance is constant? Also it must be max_distance, no?
                    self.victim.health -= 1  # Reduce health, 1st contact
                    self.occupied = True     # Cannon is occupied
                    if(self.victim.health <=0):  # Victim is dead, or died in action, also victim was an object
                        self.victim = None
                        self.occupied = False
            # Cannon continues fire.
            else:
                print(self.coordinates, self.victim.coordinates)
                print(abs(self.victim.coordinates[0]-self.coordinates[0])<5 and abs(self.victim.coordinates[0]-self.coordinates[0])<5)
                # wth this means?
                if(self.target != self.victim):
                    if(abs(self.victim.coordinates[0]-self.coordinates[0])<5 and abs(self.victim.coordinates[1]-self.coordinates[1])<5):
                        # If in range, then some error testing?
                        print('yes')
                        # Else if not in range, then we assign target to victim?
                        # But it is not even in range
                    else:
                        self.victim = self.target
                print(self.victim)
                # Current time has exceded 1 sec
                if(time.time()-self.init > 1):
                    # The health decreases one per second.
                    self.init = time.time()
                    self.victim.health -= 1 # Victim has decreasing health, target may not?
                # Victim died. We were already checking that. Can be generalized.
                if(self.victim.health <=0):
                    self.victim = None
                    self.occupied = False
        
        
