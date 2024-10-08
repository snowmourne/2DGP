from random import randint

from pico2d import *

import random

# Game object class here
class Ball:
    def __init__(self):
        rand = random.randint(0, 1)
        if rand == 0:
            self.image = load_image('ball21x21.png')
        elif rand == 1:
            self.image = load_image('ball41x41.png')
        self.x, self.y = random.randint(0, 800), 599
    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.y -= random.randint(1,3)
        if self.y < 35:
           self. y = 35


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self):
        pass


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(0, 200), 90
        self.frame = randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1 ) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)



def reset_world():
    global running
    global grass
    global team
    global world
    global balls

    running = True
    #world = []


    grass = Grass()
    #world.append(grass)

    team = [Boy() for i in range(10)]
    #world += team

    balls = [Ball() for i in range(20)]
    #world += balls

def update_world():
    grass.update()
    for boy in team:
        boy.update()
    for ball in balls:
        ball.update()

def render_world():
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    for ball in balls:
        ball.draw()
    update_canvas()

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas()

# initialization code
running = True
grass = Grass()
team = [Boy() for i in range(10)]
world = []
balls = [Ball() for i in range(20)]

# game main loop code
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)


# finalization code

close_canvas()
