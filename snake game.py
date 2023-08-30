# snake game

from tkinter import *
import random

game_width = 800
game_height = 800
speed = 80
space_size = 30
body_parts = 3
snake_color = "green"
food_color = "red"
background_color = "black"

#-----classes-----

class Snake:
    def __init__(self):
        self.body_size = body_parts
        self.coordinates = []
        self.squares = []

        for i in range(0,body_parts):
            self.coordinates.append([0,0])
        
        for x,y in self.coordinates:
            square = game_canvas.create_rectangle(x,y,(x+space_size),(y+space_size),fill=snake_color,tag="snake")
            self.squares.append(square)

class Food:
    def __init__(self):
        x = random.randint(0,(game_width/space_size)-1) * space_size
        y = random.randint(0,(game_height/space_size)-1) * space_size
        self.coordinates = [x,y]
        game_canvas.create_oval(x,y,x+space_size,y+space_size,fill=food_color,tag="food")

#-----functions-----

def next_turn(snake,food):
    x,y = snake.coordinates[0]
    if direction == "up":
        y -= space_size
    elif direction == "down":
        y += space_size
    elif direction == "left":
        x -= space_size
    elif direction == "right":
        x += space_size

    snake.coordinates.insert(0,(x,y))
    square = game_canvas.create_rectangle(x,y,x+space_size,y+space_size,fill=snake_color)

    snake.squares.insert(0,square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1

        score_label.config(text="score: {}".format(score))

        game_canvas.delete("food")
        food = Food()
    else:
        del snake.coordinates[-1]
        game_canvas.delete(snake.squares[-1])
        del snake.squares[-1]
    
    if check_colisions(snake):
        game_over()
    else:
        window.after(speed, next_turn,snake,food)
    
def change_direction(new_direction):
    global direction
    if new_direction == "left":
        if direction != "right":
            direction = new_direction
    elif new_direction == "right":
        if direction != "left":
            direction = new_direction
    elif new_direction == "up":
        if direction != "down":
            direction = new_direction
    elif new_direction == "down":
        if direction != "up":
            direction = new_direction

def check_colisions(snake):
    x, y = snake.coordinates[0]
    if x < 0 or x >= game_width:
        print("game over")
        return True
    elif y < 0 or y >= game_height:
        print("game over")
        return True
    
    for body_parts in snake.coordinates[1:]:
        if x == body_parts[0] and y == body_parts[1]:
            print("game over")
            return True
    return False

def game_over():
    game_canvas.delete(ALL)
    game_canvas.create_text(game_canvas.winfo_width()/2,game_canvas.winfo_height()/2,font=("comic sans",70),text="GAME OVER",fill="red")

#-----start-----

window = Tk()
window.title("Snake game")
window.resizable(False,False)

#---start score and direction

score = 0
direction = "down"

#---window elements

score_label = Label(window,text="score: {}".format(score),font=("comic sans",20))
score_label.pack()

game_canvas = Canvas(window,width=game_width,height=game_height,bg=background_color)
game_canvas.pack()

window.update()

#---screen star position

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

xstar_position = int((screen_width/2)-(window_width/2))
ystar_position = int((screen_height/2)-(window_height/2))

window.geometry(f"{window_width}x{window_height}+{xstar_position}+{ystar_position}")

#---key bindings

window.bind("<Left>",lambda event:change_direction("left"))
window.bind("<Right>",lambda event:change_direction("right"))
window.bind("<Down>",lambda event:change_direction("down"))
window.bind("<Up>",lambda event:change_direction("up"))

#---class and function call

snake = Snake()
food = Food()

next_turn(snake,food)

window.mainloop()