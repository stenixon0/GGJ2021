import random
import json
import text
class GameState:
    # list users, themes, soulmates, hellmates, points, has_guessed
    def __init__(self):
        self.user_ids = {}
        self.users = []
        self.themes = []
        self.soulmates = {}
        self.hellmates = {}
        self.points = {}
        self.has_guessed = {}
    
    def join(self, user):
        if user not in self.users:
            self.users.append(user.name)
            self.user_ids[user.name] = user

    def game_start(self):
        self.themes = text.themes()
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
        self.users = list(self.users)
        random.shuffle(self.users)
        self.themes = list(self.themes)
        random.shuffle(self.themes)
        self.manual_pop()
        # x = 0
        # populates soulmates
        # may cause performance issues
        # while x < 4:#change to len
        #     u = self.users
        #     print(u[x] + '\n')
        #     print(u[x+1] + '\n')
        #     print(self.themes[x])
        #     self.soulmates[self.themes[x]] = (u[x], u[x+1])
        #     # this is the best computation I could come up with (it's buggy)
        #     # unintended consequence is that the soulmates have hellmates of the same theme
        #     if (x == len(u) - 2):
        #         self.hellmates[u[x]] = u[x-2] (should be x-1?)
        #         self.hellmates[u[x+1]] = u[0]
        #     else:
        #         self.hellmates[u[x]] = u[x+3]
        #         self.hellmates[u[x+1]] = u[x+2]
        #     x = x + 2
        # self.print_dicts()
    
    def manual_pop(self):
        self.soulmates.clear()
        self.hellmates.clear()
        s = self.soulmates
        u = self.users
        h = self.hellmates
        #soulmates
        s[u[0]] = u[2]
        s[u[1]] = u[3]
        #hellmates
        h[u[0]] = u[1]
        h[u[1]] = u[2]
        h[u[2]] = u[3] #x-2 
        h[u[3]] = u[0] #x-2
        # self.print_dicts()

     
    def check_players(self):
        #https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/
        return ' '.join(map(str, self.users))

    def print_dicts(self):
        # #https://careerkarma.com/blog/python-print-dictionary/
        result = ""
        result += "Soul Mates: \n"
        for key, value in self.soulmates.items():
	        result += str(key) + ', ' + str(value) + '\n'
        result += "\nHell Mates: \n"
        for key, value in self.hellmates.items():
	        result += str(key) + ', ' + str(value) + '\n'
        result += "\nPoints: \n"
        for key, value in self.points.items():
	        result += str(key) + ', ' + str(value) + '\n'
        result += "\nhas_guessed: \n"
        for key, value in self.has_guessed.items():
	        result += str(key) + ', ' + str(value) + '\n'
        result += "\nuser_ids: \n"
        for key, value in self.user_ids.items():
	        result += str(key) + ', ' + str(value) + '\n'
        return result
    
    def get_users(self):
        return self.users
    
    def get_themes(self):
        return self.themes   

    def get_soulmates(self):
        return self.soulmates
    
    def get_hellmates(self):
        return self.hellmates

    def get_points(self):
        return self.points

    def get_has_guessed(self):
        return self.has_guessed
    
    def get_user_ids(self):
        return self.user_ids

        