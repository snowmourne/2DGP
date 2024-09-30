from pico2d import *


open_canvas()

grass = load_image('grass.png')
character = load_image('run_animation.png')

frame = 0
x = 0
mr = True

while True:
    if mr:
        for y in range(0, 800, 10):
            clear_canvas()
            grass.draw(400, 30)
            x = y
            character.clip_draw(frame * 100, 0, 100, 100, x, 90, 100, 100)
            update_canvas()
            frame = (frame+1) % 8
            delay(0.05)
    if not mr:
        for y in range(800, 0, -10):
            clear_canvas()
            grass.draw(400, 30)
            x = y
            character.clip_composite_draw(frame * 100, 0, 100, 100, 0, 'h', x, 90, 100, 100)
            update_canvas()
            frame = (frame+1) % 8
            delay(0.05)
    if x >= 790:
        mr = False
    elif x <= 10:
        mr = True

close_canvas()

