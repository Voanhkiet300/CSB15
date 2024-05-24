import pygame as py


# khai bao cua so tro choi
py.init()
py.display.set_caption('Ping Pong')
size = (600, 600)
canvas = py.display.set_mode(size)
bg_color = (186, 194, 227)
clock = py.time.Clock()


ball_img = py.image.load('/Lesson-13/assets/ball.png')
