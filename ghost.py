from turtle import *
from random import choice
from freegames import vector
class Ghost:
    def __init__(self,position,course):
        self.position = position
        self.course = course

    def move(self, game):
        if game.valid(self.position + self.course):
            self.position =self.position + self.course
        else:
            options = [
                vector(1.5,0),
                vector(-1.5,0),
                vector(0,1.5),
                vector(0,-1.5),
            ]
            plan = choice(options)
            self.course.x = plan.x
            self.course.y = plan.y
        up()
        goto(self.position.x + 2,self.position.y + 3)
        dot(20,"red")