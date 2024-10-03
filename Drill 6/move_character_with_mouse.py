from pico2d import *
from random import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

def random_hand():
    global hand_x, hand_y, goal
    hand_x, hand_y = randint(0, TUK_WIDTH), randint(0, TUK_HEIGHT)
    goal = 0

def trace_hand():
    global x, y, hand_x, hand_y, goal, frame
    near = 10

    if goal == 0:
        if abs(hand_x - x) > near:
            x += (hand_x - x) // 10
        if abs(hand_y - y) > near:
            y += (hand_y - y) // 10
        if abs(hand_x - x) <= near and abs(hand_y - y) <= near:
            goal = 1
            random_hand()

    hand.draw(hand_x, hand_y)

    if hand_x > x:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    elif hand_x < x:
        character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)



running = True

x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
hand_x, hand_y = randint(0, TUK_WIDTH), randint(0, TUK_HEIGHT)
frame = 0
hide_cursor()
goal = 0

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    trace_hand()

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

    update_canvas()
    frame = (frame + 1) % 8

    delay(0.05)

close_canvas()