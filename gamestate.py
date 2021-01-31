import random
import json
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

    def game_start(self):
        self.reset_points()
        self.round_start()
    
    def round_start(self):
        self.pop_dictionaries()
        self.reset_has_guessed()
    
    def reset_has_guessed(self):
        self.has_guessed = {}
        for user in self.users:
            self.has_guessed[user] = False
    
    def reset_points(self):
        self.points = {}
        for user in self.users:
            self.points[user] = 0

    def pop_dictionaries(self):
        random.shuffle(self.users)
        random.shuffle(self.themes)
        x = 0
        #populates soulmates
        #may cause performance issues?
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
        self.print_dicts()
     
    def check_players(self):
        #https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/
        return ' '.join(map(str, self.users))

    def print_dicts(self):
        #https://careerkarma.com/blog/python-print-dictionary/
        print("Soul Mates: \n")
        formatted = json.dumps(self.soulmates, indent=4) + '\n'
        print(formatted)
        print("\nHell Mates: \n")
        formatted = json.dumps(self.hellmates, indent=4) + '\n'
        print(formatted)
        print("\nPoints: \n")
        formatted = json.dumps(self.points, indent=4) + '\n'
        print(formatted)
        print("\nhas_guessed: \n")
        formatted = json.dumps(self.has_guessed, indent=4) + '\n'
        print(formatted)