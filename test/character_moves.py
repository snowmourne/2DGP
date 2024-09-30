from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

move_right = True
x = 0

while True:
    if move_right:
        for y in range(0, 800, 5):
            clear_canvas()
            grass.draw(400,30)
            x = y
            character.draw(x ,90)
            update_canvas()
            delay(0.01)
    elif not move_right:
        for y in range(800, 0, -5):
            clear_canvas()
            grass.draw(400,30)
            x = y
            character.composite_draw(0, 'h', x, 90)
            update_canvas()
            delay(0.01)
    if x >= 795:
        move_right = False
    elif x <= 5:
        move_right = True

close_canvas()

