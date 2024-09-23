from pico2d import *
from math import *

open_canvas()

x = 10
y = 90

turn = True

while True:

    clear_canvas_now()
    grass = load_image('grass.png')
    character = load_image('character.png')
    
    grass.draw_now(400, 30)

    if(turn == True):
        if(x <= 600 and y <= 90):
            x = x+10
            character.draw_now(x, y)
        elif(x >= 600 and y <= 500):
            y = y+10
            character.draw_now(x, y)
        elif(x >= 0 and y >= 500):
            x = x-10
            character.draw_now(x, y)
        elif(x <= 0 and y >= 90):
            y = y-10
            if(x == 10 and y == 90):
                turn = False
            character.draw_now(x, y)
    elif(turn == False):
        x = x+3
        
        
    delay(0.1)



close_canvas()
