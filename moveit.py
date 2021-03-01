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

# our game object class
class GameObject:
    def __init__(self, image, height, speed):
        self.speed = speed
        self.image = image
        self.pos = image.get_rect().move(0, height)

    def move(self):
        self.pos = self.pos.move(self.speed, 0)
        if self.pos.right > 600:
            self.pos.left = 0
    def move_up(self):
        self.pos = self.pos.move(0, self.speed)


# quick function to load an image
def load_image(name):
    path = os.path.join(main_dir, "data", name)
    return pg.image.load(path).convert()


# here's the full code
def main():
    pg.init()
    screen = pg.display.set_mode((640, 480))

    player = load_image("player1.gif")
    background = load_image("liquid.bmp")

    # scale the background image so that it fills the window and
    #   successfully overwrites the old sprite position.
    # background = pg.transform.scale2x(background)
    # background = pg.transform.scale2x(background)
    background = pg.transform.scale(background, [640,480])

    screen.blit(background, (0, 0))

    playerobj=GameObject(player, 20,20)
    # objects = []
    # for x in range(10):
    #     o = GameObject(player, x * 40, x)
    #     objects.append(o)

    while 1:
        screen.blit(background, playerobj.pos, playerobj.pos)
        k=pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    playerobj.pos = playerobj.pos.move(0, -playerobj.speed)
                elif event.key == pg.K_LEFT:
                #按下的是左方向键的话，把x坐标减一
                    playerobj.pos = playerobj.pos.move(-playerobj.speed,0)
                elif event.key == pg.K_RIGHT:
                #右方向键则加一
                    playerobj.pos = playerobj.pos.move(playerobj.speed,0)

                elif event.key == pg.K_DOWN:
                    playerobj.pos = playerobj.pos.move(0,playerobj.speed)


            if event.type == pg.QUIT:
                return
        # playerobj.move()
        screen.blit(playerobj.image,playerobj.pos)
        # for o in objects:
        #     screen.blit(background, o.pos, o.pos)
        # for o in objects:
        #     o.move()
        #     screen.blit(o.image, o.pos)

        pg.display.update()


if __name__ == "__main__":
    main()