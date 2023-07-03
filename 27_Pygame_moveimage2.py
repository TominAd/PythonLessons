import pygame

max_x = 800
max_y = 600
IMG_SIZE = 200
game_over = False
bg_color = (0, 10, 0)

pygame.init()
screen = pygame.display.set_mode((max_x, max_y), pygame.FULLSCREEN)
pygame.display.set_caption("My First PyGame !:)")  # Наеменования окна

print(pygame.image.get_extended())  # выводит тру или фолс т.е. может прочитать картинку или нет. так как только в *.png

myimage = pygame.image.load("16975.png").convert()
myimage = pygame.transform.scale(myimage, (IMG_SIZE, IMG_SIZE))  # Если надо уменьшить картинку любых размеров
x = 500
y = 100

move_rigth = False
move_left = False
move_up = False
move_down = False

# ================main Game Loop
while game_over == False:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                game_over = True
            if event.key == pygame.K_LEFT:
                move_left = True
            if event.key == pygame.K_RIGHT:
                move_rigth = True
            if event.key == pygame.K_UP:
                move_up = True
            if event.key == pygame.K_DOWN:
                move_down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_left = False
            if event.key == pygame.K_RIGHT:
                move_rigth = False
            if event.key == pygame.K_UP:
                move_up = False
            if event.key == pygame.K_DOWN:
                move_down = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

    if move_left == True:
        x -= 1
        if x < 0:
            x = 0
    if move_rigth == True:
        x += 1
        if x > max_x - IMG_SIZE:
            x = max_x - IMG_SIZE
    if move_up == True:
        y -= 1
        if y < 0:
            Y = 0
    if move_down == True:
        y += 1
        if y > max_y - IMG_SIZE:
            y= max_y - IMG_SIZE



    screen.fill(bg_color)
    screen.blit(myimage, (x, y))
    pygame.display.flip()