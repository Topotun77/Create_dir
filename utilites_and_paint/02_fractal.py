# -*- coding: utf-8 -*-

import simple_draw as sd
import random as rnd

sd.resolution = (1000, 1000)
print(help(sd))

# нарисовать ветку дерева из точки (300, 5) вертикально вверх длиной 100

point_0 = sd.get_point(500, 5)
r = 255
g = 255
b = 255


# сделать функцию рисования ветки из заданной точки,
# заданной длины, с заданным наклоном
# def branch(point, angle, length):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#     v1.draw()
#     return v1.end_point

# angle_0 = 90
# length_0 = 200
# next_point = branch(point=point_0, angle=angle_0, length=length_0)
# next_angle = angle_0 - 30
# next_length = length_0 * .75
# next_point = branch(point=next_point, angle=next_angle, length=next_length)
# next_angle = next_angle - 30
# next_length = next_length * .75
# next_point = branch(point=next_point, angle=next_angle, length=next_length)

# написать цикл рисования ветвей с постоянным уменьшением длины на 25% и отклонением на 30 градусов
# angle_0 = 90
# length_0 = 200
#
# next_angle = angle_0
# next_length = length_0
# next_point = point_0
#
# while next_length > 1:
#     next_point = branch(point=next_point, angle=next_angle, length=next_length)
#     next_angle = next_angle - 30
#     next_length = next_length * .75

# сделать функцию branch рекурсивной

def branch(point, angle, length, delta):
    if length < 2:
        return
    global r, g, b
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw(color=tuple([r, g, b]))

    # r = int(rnd.random()*255)
    # g = int(rnd.random()*255)
    # b = int(rnd.random()*255)

    if b>10:
        b -= 10
    elif g>10:
        g -= 10
    elif r>10:
        r -= 10
    else:
        r = 255
        g = 255
        b = 255

    next_point = v1.end_point
    next_angle = angle - delta
    next_length = length * .5
    if delta == 0:
        branch(point=next_point, angle=next_angle, length=next_length, delta=delta)
    else:
        for delta_2 in range(0, 61, 30):
            branch(point=next_point, angle=next_angle, length=next_length, delta=delta_2)
        for delta_2 in range(0, -61, -30):
            branch(point=next_point, angle=next_angle, length=next_length, delta=delta_2)


for delta in range(0, 61, 30):
    branch(point=point_0, angle=90, length=300, delta=delta)
for delta in range(-60, 1, 30):
    branch(point=point_0, angle=90, length=300, delta=delta)


sd.pause()

