import pygame as pg
from pygame.locals import QUIT, K_RIGHT, K_DOWN
from pathlib import Path
import sys

images_root = Path(__file__).parent / 'images'

images_rigth = images_root / 'run_right'
images_stand = images_root / 'stand'

pg.init()
run_right = [pg.image.load(str(image)) for image in images_rigth.iterdir()]
stand_img = [pg.image.load(str(image)) for image in images_stand.iterdir()]
screen = pg.display.set_mode((300,300))
clock = pg.time.Clock()

rigth_count = 0

stand_up = True
stand_count = 0

while True:

    clock.tick(20)
    screen.fill((255,255,255))

    keys = pg.key.get_pressed()

    if keys[K_RIGHT]:
        screen.blit(run_right[rigth_count], (60,90))
        rigth_count += 1
        rigth_count = rigth_count % len(run_right)

        stand_count = 0

    else:
        screen.blit(stand_img[stand_count], (60,90))

        if stand_up:
            stand_count += 1
        else:
            stand_count -= 1

        if stand_count >= len(stand_img):
            stand_count -= 1
            stand_up = not stand_up
        elif stand_count < 0:
            stand_count += 1
            stand_up = not stand_up

        rigth_count = 0


    for event in pg.event.get():

        if event.type == QUIT:
            pg.quit()
            sys.exit()

    pg.display.flip()