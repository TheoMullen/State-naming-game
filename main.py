import time
import turtle
import pandas
from label import Label
from score import Score

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
new_dict = data.to_dict()
correct_answers = []
states_to_learn = []


game_is_on = True
while game_is_on:

    answer = screen.textinput(title="Guess", prompt="Enter a state (or 'Exit'): ")

    # End game, show score and make a csv of answers to learn
    if answer == "Exit":
        game_is_on = False
        score = Score(len(correct_answers))
        time.sleep(2)

        for _ in new_dict["state"].values():
            if _ not in correct_answers:
                states_to_learn.append(_)
        new_data = pandas.DataFrame(states_to_learn).to_csv("States to learn.csv")

    for a, b in new_dict["state"].items():
        if b == answer and b not in correct_answers:
            key = a
            state_label = Label(state=new_dict["state"][key], x=new_dict["x"][key], y=new_dict["y"][key])
            correct_answers.append(b)


