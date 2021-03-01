import turtle as t
import math


def point(x, y, r, g, b):
    t.goto(x, y)
    t.pencolor(r, g, b)
    t.pendown()
    t.goto(x, y)
    t.penup()


def draw_graph(x_map, y_map, r_map, g_map, b_map):
    for tx in range(150):
        for ty in range(150):
            x = x_map(tx, ty)
            y = y_map(tx, ty)
            r = r_map(tx, ty)
            g = g_map(tx, ty)
            b = b_map(tx, ty)
            point(x, y, r, g, b)


def stand_x_map(tx, ty):
    return tx * 5 - 500


def stand_y_map(tx, ty):
    return ty * 5 - 500


def stand_r_map(tx, ty):
    return tx / 150


def stand_g_map(tx, ty):
    return ty / 150


def stand_b_map(tx, ty):
    return 0


sina = math.sin(30 / 180 * math.pi)
cosa = math.cos(30 / 180 * math.pi)


def up_x_map(tx, ty):
    return -cosa * tx + cosa * ty;


def up_y_map(tx, ty):
    return sina * tx + sina * ty;


def up_r_map(tx, ty):
    return tx / 150


def up_g_map(tx, ty):
    return ty / 150


def up_b_map(tx, ty):
    return 0


def left_x_map(tx, ty):
    return -cosa * tx;


def left_y_map(tx, ty):
    return sina * tx - ty;


def left_r_map(tx, ty):
    return tx / 150


def left_g_map(tx, ty):
    return 0


def left_b_map(tx, ty):
    return ty / 150


def right_x_map(tx, ty):
    return cosa * tx


def right_y_map(tx, ty):
    return sina * tx - ty


def right_r_map(tx, ty):
    return 0


def right_g_map(tx, ty):
    return tx / 150


def right_b_map(tx, ty):
    return ty / 150


t.setup(1200, 1000)
t.speed(10)
t.delay(0)
t.tracer(False)
t.pensize(2)
t.penup()
# draw_graph(stand_x_map, stand_y_map, stand_r_map, stand_g_map, stand_b_map)
draw_graph(up_x_map, up_y_map, up_r_map, up_g_map, up_b_map)
draw_graph(left_x_map, left_y_map, left_r_map, left_g_map, left_b_map)
draw_graph(right_x_map, right_y_map, right_r_map, right_g_map, right_b_map)
# for b in range(150):
#     # t.goto(-500, b*7-400)
#     # t.pendown()
#     for r in range(150):
#         point(r * 5 - 500, b * 7 - 400, r / 150, b / 150, 0)iop0
#         # t.pencolor(r/150, b/150, 0)
#         # t.fd(5)

t.done()
