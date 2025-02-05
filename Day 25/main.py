import turtle
import pandas as pd

screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
states = pd.read_csv("50_states.csv")
all_states = states.state.to_list()
guessed_list = []

while len(guessed_list)<50:
    answer_prompt = screen.textinput(f"{len(guessed_list)}/50 States Correct","What's another state name?").title()
    if answer_prompt == "Exit":
        missing_states = [state for state in all_states if state not in guessed_list]
        m_df = pd.DataFrame(missing_states)
        m_df.to_csv("states_to_learn.csv")
        break

    if answer_prompt in all_states:
        ans = states[states.state == answer_prompt]
        t = turtle.Turtle()
        t.hideturtle()
        t.teleport(ans.x.item(), ans.y.item())
        guessed_list.append(answer_prompt)
        t.write(answer_prompt)

