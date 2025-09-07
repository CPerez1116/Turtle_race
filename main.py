from turtle import Turtle, Screen
import random

# Flag to determine if the race has started
is_race_on = False

# Set up the screen for the race
screen = Screen()
screen.setup(width=500, height=400)

# Ask the user to place a bet on which turtle will win
user_bet = screen.textinput(
    title="Make your bet",
    prompt="Which turtle will win the race? Enter a color: "
)

# List of turtle colors
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Y positions for the turtles so they don't overlap
y_positions = [-70, -40, -10, 20, 50, 80]

# List to keep track of all turtle objects
all_turtles = []

# Create the turtles and place them at the starting line
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")        # Create a turtle
    new_turtle.color(colors[turtle_index])     # Assign a color
    new_turtle.penup()                         # Lift pen so it doesn't draw
    new_turtle.goto(x=-230, y=y_positions[turtle_index])  # Position at start
    all_turtles.append(new_turtle)             # Add to the list

# Start the race if the user placed a bet
if user_bet:
    is_race_on = True

# Main race loop
while is_race_on:
    for turtle in all_turtles:
        # Check if a turtle has crossed the finish line
        if turtle.xcor() > 230:
            is_race_on = False  # Stop the race
            winning_color = turtle.pencolor()  # Get the winning turtle's color
            # Check if user's bet was correct
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        # Move the turtle forward a random distance
        random_distance = random.randint(0, 10)
