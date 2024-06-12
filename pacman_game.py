import turtle
from turtle import *
from freegames import floor,vector
from pacman import Pacman
from ghost import Ghost
from high_scor import HighScore
from screen import Screen

def func_a():
    from pacman import Pacman
    func_a()

class PacmanGame:
    def __init__(self):
        self.screen = Screen()
        self.screen.clear()
        self.high_score = HighScore()
        self.pacman1_entry = turtle.textinput("Pacman 1", "Enter username for Pacman 1:")
        self.pacman2_entry = turtle.textinput("Pacman 2", "Enter username for Pacman 2:")
        self.tiles = [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
            0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0,
            0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0,
            0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0,
            0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0,
            0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0,
            0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0,
            0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0,
            0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0,
            0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0,
            0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0,
            0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0,
            0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0,
            0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0,
            0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        ]
        self.ghosts = [
            Ghost(vector(-170,60), vector(0,1.5)),
            Ghost(vector(1,0), vector(1.5,0)),
            Ghost(vector(-170,-60), vector(0,-1.5)),
            Ghost(vector(1,0), vector(-1.5,0)),
            Ghost(vector(100,60), vector(0,1.5)),
            Ghost(vector(0,-1), vector(0,-1.5)),
            Ghost(vector(-170,-60), vector(0,1.5)),
            Ghost(vector(-1,0), vector(1.5,0))
        ]
        self.pacman1 = Pacman(vector(-40, -80), vector(1.5, 0),1)
        self.pacman2 = Pacman(vector(50, 80), vector(0, 1.5),2)

    def offset(self, point):
        x = (floor(point.x, 20) + 200) / 20
        y = (180 - floor(point.y, 20)) / 20
        index = int(x + y * 20)
        return index

    def valid(self, point):
        index = self.offset(point)
        if self.tiles[index] == 0:
            return False
        if point.x < -170 or point.x > 170 or point.y < -180 or point.y > 170:
            return False
        return True

    def gameplay(self):
        self.screen.display_score(self.screen.score1,self.screen.lives1,self.screen.score2,self.screen.lives2,self.high_score,self.pacman1_entry,self.pacman2_entry)

        clear()

        self.pacman1.move(self)
        self.pacman2.move(self)

        for ghost in self.ghosts:
            ghost.move(self)

        if all(tile == 2 for tile in self.tiles if tile > 0):
            self.replenish()

        for ghost in self.ghosts:
            if abs(self.pacman1.position - ghost.position)< 20:
                self.screen.lives1 -= 1
                self.pacman1.position = vector(-40,-80)
                self.pacman1.aim = vector(1.5, 0)
            if abs(self.pacman2.position - ghost.position)< 20:
                self.screen.lives2 -= 1
                self.pacman2.position = vector(40,80)
                self.pacman2.aim = vector(0,1.5)

        if self.screen.lives1 == 0:
            self.pacman1.position = vector(290,290)
        if self.screen.lives2 == 0:
            self.pacman2.position = vector(290,290)
        if self.screen.lives1 == 0 and self.screen.lives2 == 0:
            self.high_score.update_high_score(max(self.screen.score1, self.screen.score2))
            self.screen.game_over(self.screen.score1, self.screen.score2, self.high_score, self.pacman1_entry, self.pacman2_entry)
            self.game_over_screen()
        else:
            ontimer(self.gameplay,25)

    def replenish(self):
        self.tiles = [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
            0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0,
            0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0,
            0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0,
            0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0,
            0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0,
            0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0,
            0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0,
            0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0,
            0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0,
            0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0,
            0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0,
            0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0,
            0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0,
            0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        ]
        self.screen.draw_tiles(self.tiles)
        self.gameplay()


    def retry(self):
        self.screen.lives1 = 3
        self.screen.lives2 = 3
        self.screen.score1 = 0
        self.screen.score2 = 0
        self.pacman1.position = vector(-40,-80)
        self.pacman1.aim = vector(1,0)
        self.pacman2.position = vector(50,80)
        self.pacman2.aim = vector(0,1)
        self.tiles = [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
            0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0,
            0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0,
            0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0,
            0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0,
            0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0,
            0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0,
            0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0,
            0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0,
            0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0,
            0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0,
            0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0,
            0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0,
            0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0,
            0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        ]
        self.ghosts = [
            Ghost(vector(-170,60), vector(0,1.5)),
            Ghost(vector(1,0), vector(1.5,0)),
            Ghost(vector(-170,-60), vector(0,-1.5)),
            Ghost(vector(1,0), vector(-1.5,0)),
            Ghost(vector(100,60), vector(0,1.5)),
            Ghost(vector(0,-1), vector(0,-1.5)),
            Ghost(vector(-170,-60), vector(0,1.5)),
            Ghost(vector(-1,0), vector(1.5,0))
        ]
        self.screen.draw_tiles(self.tiles)
        self.gameplay()

    def quit(self):
        bye()

    def game_over_screen(self):
        listen()
        onkeypress(lambda: self.retry(),"r")
        onkeypress(lambda: self.quit(),"q")

    def change1(self,x,y):
        new_position = self.pacman1.position + vector(x, y)
        if self.valid(new_position):
            self.pacman1.aim.x = x
            self.pacman1.aim.y = y

    def change2(self,x,y):
        new_position = self.pacman2.position + vector(x,y)
        if self.valid(new_position):
            self.pacman2.aim.x = x
            self.pacman2.aim.y = y

    def run(self):
        self.screen.screen.setup(420,420,370,0)
        hideturtle()
        tracer(False)
        self.screen.writer.goto(170,170)
        self.screen.writer.color("white")
        self.screen.writer.write(self.screen.score1)
        listen()
        onkeypress(lambda: self.change1(1.5, 0),"Right")
        onkeypress(lambda: self.change1(-1.5, 0),"Left")
        onkeypress(lambda: self.change1(0, 1.5),"Up")
        onkeypress(lambda: self.change1(0, -1.5),"Down")
        onkeypress(lambda: self.change2(1.5, 0),"d")
        onkeypress(lambda: self.change2(-1.5, 0),"a")
        onkeypress(lambda: self.change2(0, 2),"w")
        onkeypress(lambda: self.change2(0, -1.5),"s")
        self.screen.draw_tiles(self.tiles)
        self.gameplay()
        self.game_over_screen()
        done()

