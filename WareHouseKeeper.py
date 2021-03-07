#!/usr/bin/env python
""" pygame.examples.moveit
This is the full and final example from the Pygame Tutorial,
"How Do I Make It Move". It creates 10 objects and animates
them on the screen.
Note it's a bit scant on error checking, but it's easy to read. :]
Fortunately, this is python, and we needn't wrestle with a pile of
error codes.
"""
import os
import pygame as pg

main_dir = os.path.split(os.path.abspath(__file__))[0]
space_unit = 50
screen = None
background = None
# our game object class
class GameObject:
    def __init__(self, image, x, y):
        self.image = image
        self.pos = image.get_rect().move(x, y)



# quick function to load an image
def load_image(name):
    path = os.path.join(main_dir, "data", name)
    return pg.image.load(path).convert()


def move_player(playerobj, dx, dy, boxobj):
    next_pos = playerobj.pos.move(dx, dy)
    if boxobj.pos != next_pos:
        screen.blit(background, playerobj.pos, playerobj.pos)
        playerobj.pos = next_pos
        screen.blit(playerobj.image, playerobj.pos)

    else:
        next_box_pos = boxobj.pos.move(dx, dy)
        screen.blit(background, boxobj.pos, boxobj.pos)
        boxobj.pos = next_box_pos
        screen.blit(boxobj.image, boxobj.pos)
    # here's the full code


def main():
    global screen,background
    pg.init()
    screen = pg.display.set_mode((640, 480))

    player = load_image("player1.gif")
    background = load_image("liquid.bmp")
    box = load_image("box.jpeg")

    # scale the background image so that it fills the window and
    #   successfully overwrites the old sprite position.
    # background = pg.transform.scale2x(background)
    # background = pg.transform.scale2x(background)
    background = pg.transform.scale(background, [640, 480])
    player = pg.transform.scale(player, [space_unit, space_unit])
    box = pg.transform.scale(box, [space_unit, space_unit])
    screen.blit(background, (0, 0))
    playerobj = GameObject(player, 0, 0)
    boxobj = GameObject(box, 100, 100)
    # objects = []
    # for x in range(10):
    #     o = GameObject(player, x * 40, x)
    #     objects.append(o)
    screen.blit(boxobj.image, boxobj.pos)
    screen.blit(playerobj.image, playerobj.pos)
    while 1:

        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    move_player(playerobj, 0, -space_unit, boxobj)
                elif event.key == pg.K_RIGHT:
                    # 右方向键则加一
                    move_player(playerobj, space_unit, 0, boxobj)
                elif event.key == pg.K_LEFT:
                    move_player(playerobj, -space_unit, 0, boxobj)
                elif event.key == pg.K_DOWN:
                    move_player(playerobj, 0, space_unit, boxobj)

            if event.type == pg.QUIT:
                return
        # playerobj.move()

        # for o in objects:
        #     screen.blit(background, o.pos, o.pos)
        # for o in objects:
        #     o.move()
        #     screen.blit(o.image, o.pos)

        pg.display.update()


if __name__ == "__main__":
    main()
