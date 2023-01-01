import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, width, height, pos_x, pos_y, color):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

    def changeColor(self, color):
        self.image.fill(color)


class Player1(pygame.sprite.Sprite):
    def __init__(self, path, height, width):
        super().__init__()
        self.image = pygame.image.load(path)
        self.image = pygame.transform.scale(self.image, (height, width))
        self.rect = self.image.get_rect()

        if self.rect.x <= 25:
            self.rect.x = 25

    def border(self):
        if self.rect.x <= 0:
            self.rect.x = 0
        if self.rect.x >= 550:
            self.rect.x = 550
        if self.rect.y <= 0:
            self.rect.y = 0
        if self.rect.y >= 550:
            self.rect.y = 550

    def moveRight(self, dist):
        self.rect.x += dist

    def moveLeft(self, dist):
        self.rect.x -= dist

    def moveDown(self, dist):
        self.rect.y += dist

    def moveUp(self, dist):
        self.rect.y -= dist


# General setup
pygame.init()

# Main window
screen_width = 600
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Panel Party')

# Variables
dist = 1
p1_points = 0
p2_points = 0

# Game Objects
all_group = pygame.sprite.Group()
tile_group = pygame.sprite.Group()
for row in range(40, screen_width, 65):
    for col in range(40, screen_width, 65):
        tile = Tile(50, 50, row, col, (128, 128, 128))
        tile_group.add(tile)
        tile_group.draw(screen)
        all_group.add(tile)

player_group = pygame.sprite.Group()
player1 = Player1('ghost.png', 50, 50)
player1.rect.x = 25
player1.rect.y = 25
player_group.add(player1)
all_group.add(player1)

player2 = Player1('super-mario.png', 50, 50)
player2.rect.x = screen_width - 25
player2.rect.y = screen_height - 25
player_group.add(player2)
all_group.add(player2)


# Game Loop
while True:
    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    # No more tiles
    if p1_points+p2_points == 81:
        pygame.time.wait(4000)
        pygame.quit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(0, 0, 600, 600),  2)

    # keys to control movements
    keys = pygame.key.get_pressed()
    # Player 1 movements
    player1.border()
    if keys[pygame.K_LEFT]:
        player1.moveLeft(dist)
    if keys[pygame.K_RIGHT]:
        player1.moveRight(dist)
    if keys[pygame.K_DOWN]:
        player1.moveDown(dist)
    if keys[pygame.K_UP]:
        player1.moveUp(dist)
    # Player 2 movements
    player2.border()
    if keys[pygame.K_a]:
        player2.moveLeft(dist)
    if keys[pygame.K_d]:
        player2.moveRight(dist)
    if keys[pygame.K_s]:
        player2.moveDown(dist)
    if keys[pygame.K_w]:
        player2.moveUp(dist)

    # Collision detection
    p1_hit_list = pygame.sprite.spritecollide(player1, tile_group, False)
    p2_hit_list = pygame.sprite.spritecollide(player2, tile_group, False)
    # for i in tile_group:
    print("P1: {}".format(p1_hit_list))
    print("P2: {}".format(p2_hit_list))
    for i in p1_hit_list:
        i.changeColor((255, 0, 0))
    for i in p2_hit_list:
        i.changeColor((0, 0, 255))

    # Calculate score
    # for i in p1_hit_list:
    #     p1_points += 1
    # for i in p2_hit_list:
    #     p2_points += 1

    # Display score
    # text_surface = my_font.render("Ghost: "+str(p1_points), False, (0, 255, 0))
    # screen.blit(text_surface, (100, 600))
    # text_surface = my_font.render("Mario: "+str(p2_points), False, (0, 255, 0))
    # screen.blit(text_surface, (400, 600))

    all_group.draw(screen)
    all_group.update()
    pygame.display.update()
