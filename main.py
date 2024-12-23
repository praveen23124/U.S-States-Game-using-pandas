import turtle

import pandas as pd
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
correct_guessed_count = 0
while correct_guessed_count<50:
    answer_state = screen.textinput(title=f"{correct_guessed_count}/50 Guess the state", prompt="what's another state name?")
    title_answer_state = answer_state.title()

    if title_answer_state == "Exit":
        break

    #check if answered state is in the states of 50_states.csv
    if title_answer_state in all_states:
        state_row = data[data.state == title_answer_state]
        x = state_row.x.values[0]
        y = state_row.y.values[0]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x,y)
        t.write(title_answer_state, align="center", font=("Arial", 12,"normal"))
        correct_guessed_count += 1
        guessed_states.append(title_answer_state)

# states to learn.csv
not_guessed_states = []

for state in all_states:
    if state not in guessed_states:
        not_guessed_states.append(state)
print(not_guessed_states)


df = pd.DataFrame(not_guessed_states)
df.to_csv("states_to_learn.csv")
print(df)






