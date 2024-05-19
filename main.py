import pygame as pg

pg.init()

hight = 500
wight = 500
x_rec = 100
y_rec = 50
x_rec1 = 50
y_rec1 = 50
x_rec2 = 50
y_rec2 = 450
rec_size = 100
circle_radius = 50
dir_circle = 1
dir_rect = 1
win = pg.display.set_mode((wight, hight))
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
    x_rec = x_rec + dir_rect
    if x_rec + rec_size >= wight:
        dir_rect = -1
    if x_rec == 0:
        dir_rect = 1

    y_rec = y_rec + dir_circle
    if y_rec + circle_radius >= wight:
        dir_circle = -1
    if y_rec - circle_radius == 0:
        dir_circle = 1

    x_rec1 = x_rec1 + dir_circle
    y_rec1 = y_rec1 + dir_circle
    if x_rec1 + circle_radius >= wight and y_rec1 + circle_radius >= wight:
        dir_circle = -1
    if x_rec1 - circle_radius == 0 and y_rec1 - circle_radius == 0:
        dir_circle = 1

    x_rec2 = x_rec2 + dir_circle
    y_rec2 = y_rec2 - dir_circle
    if x_rec2 + circle_radius >= wight and y_rec1 + circle_radius >= wight:
         dir_circle = -1
    if x_rec2 - circle_radius == 0 and y_rec1 - circle_radius == 0:
        dir_circle = 1

    win.fill((255, 255, 255))
    pg.draw.rect(win, (255, 255, 0), (x_rec, 300, rec_size, rec_size))
    pg.draw.circle(win, 'red', (200, y_rec), circle_radius)
    pg.draw.circle(win, 'blue', (x_rec1, y_rec1), circle_radius)
    pg.draw.circle(win, 'black', (x_rec2, y_rec2), circle_radius)
    pg.display.update()

    pg.time.delay(10)
