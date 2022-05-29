from turtle import Turtle, Screen

class Scoreboard(Turtle):
    score = 0
    style = ('Arial', 30, 'italic')

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.write(f"Score : {self.score}",font=self.style,align='center')

    def updateScore(self):
        self.reset()
        self.score += 1
        self.__init__()
        # self.hideturtle()
        # self.penup()
        # self.goto(0, 230)
        # self.write(f"Your score is : {self.score}", font=self.style, align='center')

    def endGame(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Game over! Score : {self.score}", font=self.style, align='center')



