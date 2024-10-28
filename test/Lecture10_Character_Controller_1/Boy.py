from pico2d import load_image
from state_machine import *

class Idle:
    @staticmethod
    def enter(boy):
        pass

    @staticmethod
    def exit(boy):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8

    @staticmethod
    def draw(boy):
        boy.image.clip_draw(boy.frame * 100, boy.action * 100, 100, 100, boy.x, boy.y)

class Sleep:
    @staticmethod
    def enter(boy):
        pass

    @staticmethod
    def exit(boy):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        pass

    @staticmethod
    def draw(boy):
        boy.image.clip_composite_draw(boy.frame * 100, 300, 100, 100, 3.141592/2,'',  boy.x-25, boy.y-25, 100, 100)
        pass


class Boy:
    def __init__(self):
        self.x, self.y = 400, 90
        self.frame = 0
        self.dir = 0
        self.action = 3
        self.image = load_image('animation_sheet.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start(Idle) #객체를 생성한것이 아닌 직접 Idle이라는 함수 사용
        self.state_machine.set_transitions(
                {
                    Idle: {time_out: Sleep},
                    Sleep: {space_down: Idle}
                }

            )
    def update(self):
        self.state_machine.update()


    def handle_event(self, event):
        pass

    def draw(self):
        self.state_machine.draw()
