# Import the necessary tools from Flask
from flask import Flask, render_template, request

# Import random so the computer can make a random choice
import random

# Create a Flask web app
app = Flask(__name__)

# List of choices for the game
choices = ['rock', 'paper', 'scissors']

# Function to decide who wins
def determine_winner(user, computer):
    if user == computer:
        return "It's a Draw!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        return "You Win!"
    else:
        return "You Lose!"

# This is the homepage route. It runs when you open the website.
@app.route('/', methods=['GET', 'POST'])
def index():
    # Empty values to start with
    result = ''
    user_choice = ''
    computer_choice = ''

    # If the user clicks a button (POST method)
    if request.method == 'POST':
        user_choice = request.form['choice']               # What the user picked
        computer_choice = random.choice(choices)           # What the computer picks randomly
        result = determine_winner(user_choice, computer_choice)  # Decide who won

    # Show the webpage with the results
    return render_template('rps.html', result=result, user=user_choice, computer=computer_choice)

# This tells Python to run the app only when this file is executed directly
if __name__ == '__main__':
    app.run(debug=True, port=5002)
