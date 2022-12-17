import pygame

# Initialize pygame
pygame.init()

# Create screen
screen = pygame.display.set_mode((800, 600))

# Caption
pygame.display.set_caption("Panel Party")

# Player 1
player1Image = pygame.image.load('ghost.png')
player1Image = pygame.transform.scale(player1Image, (64, 64))
p1x, p1y = 0, 0
p1xChange, p1yChange = 0, 0


def player1(x1, y1):
    screen.blit(player1Image, (x1, y1))  # blit means draw


# Player 2
player2Image = pygame.image.load('super-mario.png')
player2Image = pygame.transform.scale(player2Image, (64, 64))
p2x, p2y = 370, 50
p2xChange, p2yChange = 0, 0


def player2(x2, y2):
    screen.blit(player2Image, (x2, y2))


# Speed
speed = 0.1

# Game Loop
running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # keys to control movements
        if event.type == pygame.KEYDOWN:
            # Player 1 movements
            if event.key == pygame.K_LEFT:
                p1xChange = -speed
            if event.key == pygame.K_RIGHT:
                p1xChange = speed
            if event.key == pygame.K_DOWN:
                p1yChange = speed
            if event.key == pygame.K_UP:
                p1yChange = -speed
            # Player 2 movements
            if event.key == pygame.K_a:
                p2xChange = -speed
            if event.key == pygame.K_d:
                p2xChange = speed
            if event.key == pygame.K_s:
                p2yChange = speed
            if event.key == pygame.K_w:
                p2yChange = -speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                p1xChange = 0
                p1yChange = 0
            if event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_s or event.key == pygame.K_w:
                p2xChange = 0
                p2yChange = 0

    p1x += p1xChange
    p1y += p1yChange
    p2x += p2xChange
    p2y += p2yChange

    # Player 1 does not exit border
    if p1x <= 0:
        p1x = 0
    if p1x >= 736:
        p1x = 736
    if p1y <= 0:
        p1y = 0
    if p1y >= 536:
        p1y = 536
    player1(p1x, p1y)

    # Player 2 does not exit border
    if p2x <= 0:
        p2x = 0
    if p2x >= 736:
        p2x = 736
    if p2y <= 0:
        p2y = 0
    if p2y >= 536:
        p2y = 536
    player2(p2x, p2y)

    pygame.display.update()
