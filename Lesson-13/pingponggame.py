import pygame as py

# khai bao cua so tro choi
py.init()
py.display.set_caption('Ping Ponggggg')
size = (600, 600)
canvas = py.display.set_mode(size)
bg_color = (186, 194, 227)
clock = py.time.Clock()


# chen tai nguyen
ball_img = py.image.load('Lesson-13/assets/ball.png')
paddle_img = py.image.load('Lesson-13/assets/paddle.png')


# setup toa do
paddle_1_x = 0
paddle_1_y = 250
paddle_2_x = 570
paddle_2_y = 250
ball_x = 285
ball_y = 300

# setup bien danh cho nut bam
w_pressed = False
s_pressed = False
up_pressed = False
down_pressed = False

# speed
speed_x = 3
speed_y = 2



loop = True
while loop: # play game
    events = py.event.get() # bat su kien
    for e in events:
        # quit
        if e.type == py.QUIT:
            loop = False
        # keyboard check
        elif e.type == py. KEYDOWN:
            if e.key == py.K_w:
                w_pressed = True
            elif e.key == py.K_s:
                s_pressed = True
            elif e.key == py.K_UP:
                up_pressed = True
            elif e.key == py.K_DOWN:
                down_pressed = True


        elif e.type == py.KEYUP:
            if e.key == py.K_w:
                w_pressed = False
            elif e.key == py.K_s:
                s_pressed = False
            elif e.key == py.K_UP:
                up_pressed = False
            elif e.key == py.K_DOWN:
                down_pressed = False
    # ball move
    ball_x += speed_x
    ball_y += speed_y

    # check collision with paddles and edges
    # >< paddles
    if ball_x <= (paddle_1_x + 30) and paddle_1_y <= ball_y <= (paddle_1_y + 120):
        speed_x = -speed_x
    if ball_x >= (paddle_2_x - 20) and paddle_2_y <= ball_y <= (paddle_2_y + 120):
        speed_x = -speed_x
    
    # >< edges
    if ball_x <= 0 or ball_x >= 570:
        speed_x = -speed_x
    if ball_y <= 0 or ball_y >= 570:
        speed_y = -speed_y

    # paddle >< edges
    if paddle_1_y <= 0:
        w_pressed = False
    if paddle_2_y <= 0:
        up_pressed = False
    if paddle_1_y >= 480:
        s_pressed = False
    if paddle_2_y >= 480:
        down_pressed = False

    # paddles move
    if w_pressed:
        paddle_1_y -= 5
    elif s_pressed:
        paddle_1_y += 5
    if up_pressed:
        paddle_2_y -= 5
    elif down_pressed:
        paddle_2_y += 5

    canvas.fill(bg_color)
    canvas.blit(ball_img, (ball_x, ball_y))
    canvas.blit(paddle_img, (paddle_1_x, paddle_1_y))
    canvas.blit(paddle_img, (paddle_2_x, paddle_2_y))


    clock.tick(60)

    py.display.flip()