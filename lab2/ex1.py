import random as rd
import turtle as t

t.shape('turtle')
t.speed(0)

for i in range(1000):
    alpha = rd.random()*720
    step_lenth = rd.randint(10, 30)
    t.forward(step_lenth)
    t.left(alpha)
