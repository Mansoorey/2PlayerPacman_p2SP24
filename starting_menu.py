import turtle
from high_scor import HighScore
from pacman_game import PacmanGame
class StartingMenu:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.bgcolor("black")
        self.writer = turtle.Turtle(visible=False)
        self.writer.color("white")
        self.writer.penup()
        self.writer.goto(-150,100)
        self.high_score = HighScore()

    def draw_menu(self):
        self.screen.setup(420,420,370,0)
        self.screen.title("2 Player Pacman Game (Mansoor Khan)")  # Change the name of the tkinter window
        self.writer.clear()
        self.writer.write("2 Player Pacman Game", align="left", font=("Arial", 20, "bold"))
        self.writer.goto(-150,-60)
        self.writer.write("Options:", align="left", font=("Arial", 15, "bold"))
        self.writer.goto(-150,-90)
        self.writer.write("1. Play", align="left", font=("Arial", 15, "normal"))
        self.writer.goto(-150,-120)
        self.writer.write("2. Exit", align="left", font=("Arial", 15, "normal"))
        self.writer.goto(-150,-150)
        self.writer.write("High Score: {}".format(self.high_score.high_score), align="left", font=("Arial", 15, "normal"))


    def play(self):
        game = PacmanGame()
        game.run()

    def exit(self):
        self.screen.bye()

    def run(self):
        self.draw_menu()
        self.screen.listen()
        self.screen.onkeypress(lambda: self.play(),"1")
        self.screen.onkeypress(lambda: self.exit(),"2")
        self.screen.mainloop()

