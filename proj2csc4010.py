import tkinter as tk
import turtle
import random
import sys
import time


class PythonPong():

    def variables(self):
        # Variables
        self.top_border = 270
        self.bottom_border = -270
        self.right_border = 480
        self.left_border = -480
        self.paddle_speed = 70
        self.paddle_boundary_top = self.top_border
        self.paddle_boundary_bottom = self.bottom_border
        self.max_score = 5
        self.playerA = 0
        self.playerB = 0

    def draw(self):
        # Screen Setup
        self.screen = turtle.Screen()
        self.screen.title("Python Pong")
        self.screen.setup(width=1280, height=720)

        # Draw Court and Service Lines
        self.background = turtle.Turtle()
        self.background.speed(0)
        self.background.color("green")
        self.background.penup()
        self.background.goto(-480, 270)
        self.background.pendown()
        self.background.begin_fill()
        self.background.goto(480, 270)
        self.background.goto(480, -270)
        self.background.goto(-480, -270)
        self.background.goto(-480, 270)
        self.background.end_fill()
        self.background.hideturtle()

        self.left_line = turtle.Turtle()
        self.left_line.speed(0)
        self.left_line.color("white")
        self.left_line.penup()
        self.left_line.goto(0, 0)
        self.left_line.pendown()
        self.left_line.goto(-240, 0)
        self.left_line.goto(-240, 200)
        self.left_line.goto(-480, 200)
        self.left_line.goto(-240, 200)
        self.left_line.goto(0, 200)

        self.left_line.penup()
        self.left_line.goto(-240, 0)
        self.left_line.pendown()
        self.left_line.goto(-240, -200)
        self.left_line.goto(-480, -200)
        self.left_line.goto(-240, -200)
        self.left_line.goto(0, -200)
        self.left_line.hideturtle()

        self.right_line = turtle.Turtle()
        self.right_line.speed(0)
        self.right_line.color("white")
        self.right_line.penup()
        self.right_line.goto(0, 0)
        self.right_line.pendown()
        self.right_line.goto(240, 0)
        self.right_line.goto(240, 200)
        self.right_line.goto(480, 200)
        self.right_line.goto(240, 200)
        self.right_line.goto(0, 200)

        self.right_line.penup()
        self.right_line.goto(240, 0)
        self.right_line.pendown()
        self.right_line.goto(240, -200)
        self.right_line.goto(480, -200)
        self.right_line.goto(240, -200)
        self.right_line.goto(0, -200)
        self.right_line.hideturtle()

    # Draw the center net
        self.net = turtle.Turtle()
        self.net.speed(0)
        self.net.color("white")
        self.net.penup()
        self.net.goto(0, 270)
        self.net.pendown()
        self.net.setheading(270)
        while self.net.ycor() > -270:
            self.net.forward(20)
            self.net.penup()
            self.net.forward(20)
            self.net.pendown()

    # Draw paddles
        self.paddle1 = turtle.Turtle()
        self.paddle1.speed(0)
        self.paddle1.shape("square")
        self.paddle1.color("red")
        self.paddle1.shapesize(stretch_wid=6, stretch_len=1)
        self.paddle1.penup()
        self.paddle1.goto(-375, 0)

        self.paddle2 = turtle.Turtle()
        self.paddle2.speed(0)
        self.paddle2.shape("square")
        self.paddle2.color("blue")
        self.paddle2.shapesize(stretch_wid=6, stretch_len=1)
        self.paddle2.penup()
        self.paddle2.goto(375, 0)

    # Draw ball
        self.ball = turtle.Turtle()
        self.ball.speed(0)
        self.ball.shape("circle")
        self.ball.color("white")
        self.ball.penup()
        self.ball.goto(0, 0)
        self.ball.dx = 8
        self.ball.dy = -8

    # Draw scoreboard
        self.score = turtle.Turtle()
        self.score.speed(0)
        self.score.penup()
        self.score.hideturtle()
        self.score.goto(0, 300)
        self.score.write("Player A: {:<2}    Player B: {:>2}".format(self.playerA, self.playerB), align="center", font=("Courier", 20, "bold"))

    def increase_ball_speed(self):
        if abs(self.ball.dx) < 12.5:
            self.ball.dx *= 1.05
            self.ball.dy *= 1.05

    def movePad1Up(self):
        y = self.paddle1.ycor() + self.paddle_speed
        if y < self.paddle_boundary_top:
            self.paddle1.sety(y)

    def movePad1Down(self):
        y = self.paddle1.ycor() - self.paddle_speed
        if y > self.paddle_boundary_bottom:
            self.paddle1.sety(y)

    def movePad2Up(self):
        y = self.paddle2.ycor() + self.paddle_speed
        if y <= self.paddle_boundary_top:
            self.paddle2.sety(y)

    def movePad2Down(self):
        y = self.paddle2.ycor() - self.paddle_speed
        if y >= self.paddle_boundary_bottom:
            self.paddle2.sety(y)

    def ai_player_2(self):
        if self.ball.dx > 0:
            reaction_time = random.uniform(0.1, 0.3)
            paddle_center = self.paddle2.ycor() + (self.paddle2.shapesize()[0] * 20 / 2)
            predicted_y = self.ball.ycor() + random.uniform(-20, 20) + ((self.right_border - self.ball.xcor()) / self.ball.dx) * self.ball.dy
            optimal_y = paddle_center + (self.ball.xcor() - self.paddle2.xcor()) * (self.ball.dy / self.ball.dx)
            self.screen.ontimer(lambda: self.move_ai_paddle(predicted_y, optimal_y), int(reaction_time * 1000))
        self.screen.ontimer(self.ai_player_2, 200)

    def move_ai_paddle(self, predicted_y, optimal_y):
        if abs(predicted_y - optimal_y) > 10:
            if predicted_y > optimal_y:
                self.movePad2Up()
            elif predicted_y < optimal_y:
                self.movePad2Down()

    def reset_game(self):
        self.paddle1.goto(-375, 0)
        self.paddle2.goto(375, 0)
        self.ball.goto(0, 0)
        self.ball.dx = random.choice([-8, 8])
        self.ball.dy = random.choice([-8, 8])
        self.score.write("Player A: {:<2}    Player B: {:>2}".format(self.playerA, self.playerB), align="center", font=("Courier", 20, "bold"))
        time.sleep(1)
        self.score.clear()

    def countdown(self):
        self.score.clear()
        self.score.write("Get ready!", align="center", font=("Courier", 20, "bold"))
        time.sleep(1)
        self.score.clear()
        
    def run_game(self):
        self.screen.listen()
        self.screen.onkeypress(self.movePad1Up, "w")
        self.screen.onkeypress(self.movePad1Down, "s")
        self.screen.onkeypress(self.movePad2Up, "Up")
        self.screen.onkeypress(self.movePad2Down, "Down")

        while True:
            self.screen.update()  # Update the screen

            # Move the ball
            self.ball.setx(self.ball.xcor() + self.ball.dx)
            self.ball.sety(self.ball.ycor() + self.ball.dy)

            # Check for collisions with walls
            if self.ball.ycor() >= self.top_border or self.ball.ycor() <= self.bottom_border:
                self.ball.dy *= -1

            # Check for collisions with paddles
            if (self.ball.dx > 0 and self.paddle2.xcor() - 25 <= self.ball.xcor() <= self.paddle2.xcor() and
                    self.paddle2.ycor() - 75 <= self.ball.ycor() <= self.paddle2.ycor() + 75):
                self.ball.dx *= -1
                self.increase_ball_speed()

            elif (self.ball.dx < 0 and self.paddle1.xcor() + 25 >= self.ball.xcor() >= self.paddle1.xcor() and
                self.paddle1.ycor() - 75 <= self.ball.ycor() <= self.paddle1.ycor() + 75):
                self.ball.dx *= -1
                self.increase_ball_speed()

            # Check for scoring
            if self.ball.xcor() >= self.right_border:
                self.playerA += 1
                self.score.clear()
                self.score.write("Player A: {:<2}    Player B: {:>2}".format(self.playerA, self.playerB), align="center", font=("Courier", 20, "bold"))
                if self.playerA >= self.max_score:
                    self.score.clear()
                    self.ball.goto(0, 0)
                    self.ball.dx = 0
                    self.ball.dy = 0
                    self.score.write("Player A wins!", align="center", font=("Courier", 20, "bold"))
                    time.sleep(5)
                    break
                self.reset_game()

            elif self.ball.xcor() <= self.left_border:
                self.playerB += 1
                self.score.clear()
                self.score.write("Player A: {:<2}    Player B: {:>2}".format(self.playerA, self.playerB), align="center", font=("Courier", 20, "bold"))
                if self.playerB >= self.max_score:
                    self.score.clear()
                    self.ball.goto(0, 0)
                    self.ball.dx = 0
                    self.ball.dy = 0
                    self.score.write("Player B wins!", align="center", font=("Courier", 20, "bold"))
                    time.sleep(5)
                    break
                self.reset_game()


def play_vs_play():
    # Create an instance of PythonPong
    pong = PythonPong()
    # Initialize variables
    pong.variables()

    # Draw the game elements and set up the game
    pong.draw()
    pong.countdown()
    root.destroy()
    # Run Player vs Player
    pong.run_game()

def play_vs_cpu():
    # Create an instance of PythonPong
    pong = PythonPong()
    # Initialize variables
    pong.variables()

    # Draw the game elements and set up the game
    pong.draw()
    pong.countdown()
    pong.ai_player_2()
    root.destroy()
    # Run Player vs CPU
    pong.run_game()

def exit_game():
    sys.exit()

root = tk.Tk()
root.title("Python Pong")

frame = tk.Frame(root)
frame.pack(expand=False, fill=tk.BOTH)

btn_ping_pong = tk.Button(frame, text="Player VS Player", command=play_vs_play, height=3, width=20)
btn_ping_pong.pack(side=tk.LEFT, padx=10, pady=30)

btn_pong_cpu = tk.Button(frame, text="Player VS CPU", command=play_vs_cpu, height=3, width=20)
btn_pong_cpu.pack(side=tk.LEFT, padx=10, pady=30)

btn_exit = tk.Button(frame, text="Exit", command=exit_game, height=3, width=20)
btn_exit.pack(side=tk.LEFT, padx=10, pady=30)

root.mainloop()