import pygame

max_x = 800
max_y = 600
game_over = False
bg_color = (0, 10, 0)

pygame.init()
screen = pygame.display.set_mode((max_x, max_y), pygame.FULLSCREEN)
pygame.display.set_caption("My First PyGame !:)")  # Наеменования окна

print(pygame.image.get_extended())  # выводит тру или фолс т.е. может прочитать картинку или нет. так как только в *.png

myimage = pygame.image.load("16975.png").convert()
myimage = pygame.transform.scale(myimage, (250, 250))  # Если надо уменьшить картинку любых размеров
x = 500
y = 100
# ================main Game Loop
while game_over == False:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over = True
            if event.key == pygame.K_LEFT:
                x -= 20
            if event.key == pygame.K_RIGHT:
                x += 20
            if event.key == pygame.K_UP:
                y -= 20
            if event.key == pygame.K_DOWN:
                y += 20
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

    screen.fill(bg_color)
    screen.blit(myimage, (x, y))
    pygame.display.flip()