import random
class GameState:
    # list users, themes, soulmates, hellmates, points, has_guessed
    def __init__(self):
        self.users = []
        self.themes = []
        self.soulmates = {}
        self.hellmates = {}
        self.points = {}
        self.has_guessed = {}
    
    def join(self, user):
        if user not in self.users:
            self.users.append(user)
    
    def round_start(self):
        self.pop_dictionaries()

    def pop_dictionaries(self):
        random.shuffle(self.users)
        random.shuffle(self.themes)
        x = 0
        #populates soulmates
        while x < len(self.users):
            u = self.users
            self.soulmates[self.themes[x]] = (u[x], u[x+1])
            #this is the best computation I could come up with, 
            #unintended consequence is that the soulmates have hellmates of the same theme
            if (x == len(u) - 2):
                self.hellmates[u[x]] = u[x-2]
                self.hellmates[u[x+1]] = u[0]
            else:
                self.hellmates[u[x]] = u[x+3]
                self.hellmates[u[x+1]] = u[x+2]
            x = x + 2
        #populates hellmates
        random.shuffle(self.users)

        

        
    
    def round_end(self):
        pass
    
    def check_players(self):
        #https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/
        return ' '.join(map(str, self.users))