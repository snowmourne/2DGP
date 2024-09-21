import turtle as t

def t_Rmove():
    t.setheading(0)
    t.forward(50)
    t.stamp()

def t_Lmove():
    t.setheading(180)
    t.forward(50)
    t.stamp()

def t_Umove():
    t.setheading(90)
    t.forward(50)
    t.stamp()

def t_Dmove():
    t.setheading(270)
    t.forward(50)
    t.stamp()

def t_reset():
    t.reset()
    t.shape('turtle')
    t.stamp()

t.shape('turtle')
t.stamp()

t.onkey(t_Umove, 'w')
t.onkey(t_Lmove, 'a')
t.onkey(t_Dmove, 's')
t.onkey(t_Rmove, 'd')
t.onkey(t_reset, 'Escape')
t.listen()

t.mainloop()


