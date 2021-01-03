import random
import turtle

t = turtle.Pen()

turtle.speed(9)
turtle.tracer(0,0)
t.up()

str_len = 500

gen_0_list = [0] * str_len
initial_mem = 250
gen_0_list[initial_mem] = 1



# This is Rule 30
def rules(left, me, right):
    if left == 1 and me == 1 and right == 1:
        return 0
    elif left == 1 and me == 1 and right == 0:
        return 0
    elif left == 1 and me == 0 and right == 1:
        return 0
    elif left == 1 and me == 0 and right == 0:
        return 1
    elif left == 0 and me == 1 and right == 1:
        return 1
    elif left == 0 and me == 1 and right == 0:
        return 1
    elif left == 0 and me == 0 and right == 1:
        return 1
    elif left == 0 and me == 0 and right == 0:
        return 0


# This is Rule 110
"""def rules(left, me, right):
    if left == 1 and me == 1 and right == 1:
        return 0
    elif left == 1 and me == 1 and right == 0:
        return 1
    elif left == 1 and me == 0 and right == 1:
        return 1
    elif left == 1 and me == 0 and right == 0:
        return 0
    elif left == 0 and me == 1 and right == 1:
        return 1
    elif left == 0 and me == 1 and right == 0:
        return 1
    elif left == 0 and me == 0 and right == 1:
        return 1
    elif left == 0 and me == 0 and right == 0:
        return 0"""

def next_gen(looked_at):
    next_list = [0] * str_len
    for i in range(1, str_len - 1):
        left = looked_at[(i - 1)]
        me = looked_at[i]
        right = looked_at[(i + 1)]
        next_list[i] = rules(left, me, right)
    for j in next_list:
        if j == 0:
            t.forward(1)
        if j == 1:
            t.down()
            t.forward(1)
            t.up()
    t.back(str_len)
    t.right(90)
    t.forward(1)
    t.left(90)
    return next_list


first_gen = gen_0_list

for i in range(0, 200):
    second_gen = next_gen(first_gen)
    first_gen = second_gen

t.forward(250)
turtle.update()
turtle.Screen().exitonclick()