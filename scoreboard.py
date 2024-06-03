from turtle import Turtle


FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    """Initializes scoreboard for game"""

    # Creates a turtle to display text and defines level variable.
    def __init__(self):
        super().__init__()
        self.color("black")
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(0, 265)
        self.update_scoreboard()

    # Updates the scoreboard with given variants
    def update_scoreboard(self):
        self.write(arg=f"Level {self.level}", align=ALIGNMENT, move=False, font=FONT)

    # Game over trigger
    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)

    # Simple level up trigger that updates level variable
    def level_up(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()

