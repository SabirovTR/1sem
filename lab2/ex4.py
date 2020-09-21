from random import randint
import turtle as t

t.shape('circle')

t.penup()
t.goto(200, 200)
t.pendown()
t.goto(200,-200)
t.goto(-200, -200)
t.goto(-200, 200)
t.goto(200, 200)
t.penup

number_of_turtles = 5
steps_of_time_number = 100


pool = [t.Turtle(shape='turtle') for i in range(number_of_turtles)]
for unit in pool:
    unit.shape('circle')
    unit.penup()
    unit.speed(0)

x = [randint(-200, 200) for unit in pool]
y = [randint(-200, 200) for unit in pool]
vx = [randint(-20, 20) for unit in pool]
vy = [randint(-20, 20) for unit in pool]
dt = 1

while True:
    for unit in pool:
        i = pool.index(unit)
        if (abs(x[i]) <= 200)and(abs(y[i]) <= 200):
            unit.goto(x[i], y[i])
            x[i] += vx[i]*dt
            y[i] += vy[i]*dt
        elif (abs(x[i]) <= 200)and(abs(y[i]) > 200):
            if y[i] > 200: y[i] = 200;
            else: y[i] = -200
            unit.goto(x[i], y[i])
            vy[i] = - vy[i]
            x[i] += vx[i]*dt
            y[i] += vy[i]*dt
        elif (abs(x[i]) > 200)and(abs(y[i]) <= 200):
            if x[i] > 200: x[i] = 200;
            else: x[i] = -200
            unit.goto(x[i], y[i])
            vx[i] = - vx[i]
            x[i] += vx[i]*dt
            y[i] += vy[i]*dt
        else:
            if y[i] > 200: y[i] = 200;
            else: y[i] = -200
            if x[i] > 200: x[i] = 200;
            else: x[i] = -200
            unit.goto(x[i], y[i])
            vx[i] = - vx[i]
            vy[i] = - vy[i]
            x[i] += vx[i]*dt
            y[i] += vy[i]*dt
