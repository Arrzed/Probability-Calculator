# Probability Calculator

Suppose there is a hat containing 5 blue balls, 4 red balls, and 2 green balls. What is the probability that a random draw of 4 balls will contain at least 1 red ball and 2 green balls?

It has a Hat class with a draw() method. Examples:

hat1 = Hat(yellow=3, blue=2, green=6) // Creates a hat with 3 yellow balls, 2 blue balls and 6 green balls

draw(quantity) // Returns a  quantity number of balls at random from the hat, also removing them from the hat

## Function

experiment(hat,expected_balls,num_balls_drawn,num_experiments) // Returns a probability

Arguments:
- hat: a Hat object
- expected_balls: receives a dictionary (e.g. {"red":2,"green":1})
- num_balls_drawn: number of balls per draw
- num_experiments: how many draws the program will do
