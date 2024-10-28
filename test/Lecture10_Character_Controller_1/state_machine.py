#event ( 종류 문자열, 실제 값)
from sdl2 import SDL_KEYDOWN, SDLK_SPACE


def space_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE

def time_out(e):
    return e[0] == 'TIME_OUT'

# 상태 머신을 처리 관리해주는 클래스
class StateMachine:

    def __init__(self, o):
        self.o = o
        self.event_que = []

    def start(self, state):
        self.cur_state = state #현재 상태를 시작상태로 만듬
        self.cur_state.enter(self.o, ('START', 0))
        pass

    def add_event(self, e):
        self.event_que.append(e)

    def set_transitions(self, transitions):
        self.transitions = transitions

    def update(self):
        self.cur_state.do(self.o)
        if self.event_que:
            event = self.event_que.pop(0)
            for check_event, next_state in self.transitions[self.cur_state].items():
                if check_event(event):
                    self.cur_state.exit(self.o)
                    self.cur_state = next_state
                    self.cur_state.enter(self.o)
                    return

    def draw(self):
        self.cur_state.draw(self.o)

    def handle_event(self, e):
        pass