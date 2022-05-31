from turtle import Turtle, Screen

class Scoreboard(Turtle):
    score = 0
    style = ('Arial', 30, 'italic')

    def __init__(self):
        with open('pythonsnakehighscore.txt') as file:
            self.highscore = file.read()
            self.highscore = int(self.highscore)

        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.write(f"Score : {self.score} Highscore : {self.highscore}",font=self.style,align='center')

    def updateScore(self):
        self.clear()
        self.score += 1
        self.__init__()
        # self.hideturtle()
        # self.penup()
        # self.goto(0, 230)
        # self.write(f"Your score is : {self.score}", font=self.style, align='center')

    def endGame(self):
        self.clear()
        self.goto(0,0)
        if self.score > self.highscore:
            self.highscore = self.score
            with open('pythonsnakehighscore.txt',mode="w") as file:
                file.write(str(self.score))
        self.write(f"Game over! Score : {self.score} High score : {self.highscore}", font=self.style, align='center')




