from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk = load_image('TUK_GROUND.png')
character = load_image('pngegg.png')

status = 0

def handle_events():
    global running, x_dir, y_dir, status

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                status = 1
                x_dir += 1
                update_canvas()
            elif event.key == SDLK_LEFT:
                status = 1
                x_dir -= 1
            elif event.key == SDLK_UP:
                status = 2
                y_dir += 1
            elif event.key == SDLK_DOWN:
                status = 2
                y_dir -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                status = 0
                x_dir -= 1
            elif event.key == SDLK_LEFT:
                status = 0
                x_dir += 1
            elif event.key == SDLK_UP:
                status = 0
                y_dir -= 1
            elif event.key == SDLK_DOWN:
                status = 0
                y_dir += 1


running = True
x = TUK_WIDTH // 2
y = TUK_HEIGHT // 2
frame = 0
x_dir = 0
y_dir = 0

while running:
    clear_canvas()
    tuk.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    if status == 0:
        character.clip_draw(frame * 47, 450 , 45, 50, x, y, 150, 150)
        frame = (frame + 1) % 2
        pass
    elif status == 1:
        character.clip_draw(frame * 60, 360 , 45, 45, x, y, 150, 150)
        frame = (frame + 1) % 10
        pass
    elif status == 2:
        character.clip_draw(frame * 70, 165, 60, 60, x, y, 150, 150)
        frame = (frame + 1) % 10
        pass
    update_canvas()
    handle_events()

    x += x_dir * 10
    y += y_dir * 10
    if x < 30:
        x = 30
    elif x > TUK_WIDTH - 30:
        x = TUK_WIDTH - 30
    if y < 30:
        y = 30
    elif y > TUK_HEIGHT - 30:
        y = TUK_HEIGHT - 30


    delay(0.05)

close_canvas()

