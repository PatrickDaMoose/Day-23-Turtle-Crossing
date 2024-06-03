from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    """Initializes Movable Turtle at (0, -280) and defines reset_pos, m_forward, and m_backward"""

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.seth(90)
        self.penup()
        self.cor = self.ycor()

    def reset_pos(self):
        self.goto(STARTING_POSITION)

    # Movement Methods
    def m_forward(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)

    def m_backward(self):
        new_y = self.ycor() - 10
        self.goto(self.xcor(), new_y)
