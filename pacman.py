from turtle import *

def func_a():
    from pacman_game import Screen
    func_a()

class Pacman:
    def __init__(self,position,aim,player_number):
        self.position = position
        self.aim = aim
        self.player_number = player_number
        self.screen = Screen()

    def move(self, game):
        new_position = self.position + self.aim
        if game.valid(new_position):
            self.position = new_position

        index = game.offset(self.position)
        if game.tiles[index] == 1:
            game.tiles[index] = 2
            if self.player_number == 1:
                game.screen.score1 = game.screen.score1 + 1
            else:
                game.screen.score2 = game.screen.score2 + 1
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            game.screen.square(x,y)

        up()
        goto(self.position.x, self.position.y + 5)
        if self.player_number == 1:
            dot(20, "yellow")
        else:
            dot(20, "green")