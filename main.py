import turtle
import pandas

def get_mouse_click_coor(x, y):
    print(x, y)

screen = turtle.Screen()
screen.title("Brasil., States Game")
image = "br-states.gif"
screen.addshape(image)
turtle.shape(image)

turtle.onscreenclick(get_mouse_click_coor)

data = pandas.read_csv("states_brasil.csv")
states = data.state.tolist()
x = data.x.tolist()
y = data.y.tolist()

t = turtle.Turtle()
t.penup()
t.color("black")
t.hideturtle()

guessed_states=[]
while len(guessed_states) < 27:
    answer_state = screen.textinput(title="Advinhe o Estado", prompt="Diga o nome de um Estado (digite 'Sair' para parar):" ).title()

    if answer_state == "Sair":
        missing_states = []
        for state in states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missing_states.csv")
        break

    if answer_state in states:
        guessed_states.append(answer_state)
        index = states.index(answer_state)
        x_move = x[index]
        y_move = y[index]
        t.goto(x_move, y_move)
        t.write(f"{answer_state}", align="left", font=("Courier", 9, "normal"))

# Keep the screen open
# turtle.mainloop()
