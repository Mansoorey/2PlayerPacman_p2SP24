import turtle
class Screen:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.bgcolor("black")
        self.path = turtle.Turtle(visible=False)
        self.writer = turtle.Turtle(visible=False)
        self.score1 = 0
        self.score2 = 0
        self.lives1 = 3
        self.lives2 = 3

    def draw_tiles(self, tiles):
        self.path.color("blue")
        for i in range(len(tiles)):
            tile = tiles[i]

            if tile > 0:
                x = (i % 20) * 20 - 200
                y = 180 - (i // 20) * 20
                self.square(x, y)

            if tile == 1:
                self.path.up()
                self.path.goto(x+10,y+10)
                self.path.dot(2, "white")

    def square(self, x, y):
        self.path.up()
        self.path.goto(x, y)
        self.path.down()
        self.path.begin_fill()

        for count in range(4):
            self.path.forward(20)
            self.path.left(90)
        self.path.end_fill()

    def clear(self):
        self.screen.clearscreen()
        self.screen.bgcolor("black")

    def display_score(self, score1,lives1,score2,lives2,high_score,username1,username2):
        self.writer.clear()
        self.writer.write(
            "{}: {}  Lives: {}  {}: {}  Lives: {} High Score: {}\n".format(username1,score1,lives1,username2,score2,lives2,high_score.high_score),align="right", font=("Arial", 10, "bold"))

    def game_over(self,score1,score2,high_score,username1,username2):
        self.writer.clear()
        self.writer.write(
            "{}: {}  {}: {} High score {} R (Retry)/ Q (quit)\n".format(username1,score1,username2,score2,high_score.high_score), align="right",font=("Arial", 10, "bold"))