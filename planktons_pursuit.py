"""
Plankton's Pursuit for the Krabby Patty Formula
A Pygame-based arcade game where Plankton tries to steal the secret formula
while avoiding obstacles and projectiles from Mr. Krabs.
"""

import pygame
import random
from pygame.locals import *

# Color constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (102, 255, 51)
RED = (255, 0, 0)
LBLUE = (102, 204, 255)
LLBLUE = (0, 204, 255)
RRED = (255, 77, 77)
YELLOW = (255, 255, 0)
BROWN = (204, 136, 0)
GREY = (77, 77, 77)
BLUISH = (31, 143, 237)

# Initialize Pygame
pygame.init()

# Screen configuration
size = (700, 800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("PLANKTON'S PURSUIT BY JOSE AND TIMOTHY")


def draw_vertical_line(x0, y0, x1, y1):
    """Draw vertical train track lines."""
    pygame.draw.line(screen, BROWN, [x0, y0], [x1, y1], 14)


def draw_background(my_color, screen):
    """Draw the game background including roads, water, and lane markings."""
    # Draw lane separators
    y_offset = 117
    while y_offset < 1100:
        pygame.draw.line(screen, WHITE, [0, 100 + y_offset], [800, 100 + y_offset], 5)
        y_offset += 100
    
    # Draw water and top area
    pygame.draw.rect(screen, LLBLUE, [0, 520, 700, 95])
    pygame.draw.rect(screen, my_color, [0, 0, 700, 110])
    
    # Draw road signs
    for sign in road_sign:
        x = sign[0] - 5
        y = sign[1] - 5
        pygame.draw.rect(screen, WHITE, [x, y, 55, 10])
        pygame.draw.rect(screen, WHITE, [x, y - 500, 55, 10])
        pygame.draw.rect(screen, WHITE, [x, y - 400, 55, 10])
        pygame.draw.rect(screen, WHITE, [x, y - 200, 55, 10])


class Restaurant(pygame.sprite.Sprite):
    """Krusty Krab restaurant sprite that changes appearance at night."""
    
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/fullkrusty.PNG')
        self.rect = self.image.get_rect()
    
    def update(self):
        if my_color == BLACK:
            self.image = pygame.image.load('assets/nightcrustcrab.PNG')
        else:
            self.image = pygame.image.load('assets/fullkrusty.PNG')


class SecretFormula(pygame.sprite.Sprite):
    """The objective - Krabby Patty secret formula."""
    
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/secretformula.PNG')
        self.rect = self.image.get_rect()


class Train(pygame.sprite.Sprite):
    """Train obstacle that moves horizontally across tracks."""
    
    def __init__(self):
        super().__init__()
        self.original_pos_y = 0
        self.original_pos_x = 0
        self.image = pygame.image.load('assets/trainshutterstock.PNG').convert()
        self.image.set_colorkey(WHITE)
        self.train_change_x = 0
        self.rect = self.image.get_rect()
    
    def reset_pos(self):
        self.rect.x = -600
        self.rect.y = self.original_pos_y
    
    def update(self):
        # Train moves faster at night
        if my_color == BLACK:
            self.rect.x += 4
        else:
            self.rect.x += self.train_change_x
        
        if self.rect.x > 800:
            self.reset_pos()


class Police(pygame.sprite.Sprite):
    """Police car that chases the player."""
    
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/police.PNG').convert()
        self.popo_change_x = 0
        self.rect = self.image.get_rect()
    
    def reset_pos(self):
        x = 0
        y_positions = [620, 420, 220, 120, 720]
        rand = random.randrange(0, 4)
        self.rect.x = x
        self.rect.y = y_positions[rand]
    
    def update(self):
        self.rect.x += self.popo_change_x
        if self.rect.x > 700:
            self.reset_pos()
        # Police car moves vertically at night
        if my_color == BLACK:
            self.rect.y -= 1


class Boat(pygame.sprite.Sprite):
    """Boat obstacle that moves across the water."""
    
    def __init__(self):
        super().__init__()
        self.original_pos_y = 0
        self.original_pos_x = 0
        
        # Randomly select boat type
        x = random.randrange(0, 2)
        if x == 0:
            self.image = pygame.image.load('assets/boat1.PNG').convert()
        elif x == 1:
            self.image = pygame.image.load('assets/boat2.PNG').convert()
        elif x == 2:
            self.image = pygame.image.load('assets/boat3.PNG').convert()
        
        self.boat_change_x = 0
        self.rect = self.image.get_rect()
    
    def reset_pos(self):
        x = random.randrange(1, 3)
        if x == 1:
            self.image = pygame.image.load('assets/boat1.PNG').convert()
        elif x == 2:
            self.image = pygame.image.load('assets/boat2.PNG').convert()
        elif x == 3:
            self.image = pygame.image.load('assets/boat3.PNG').convert()
        
        self.rect.x = self.original_pos_x - 100
        self.rect.y = self.original_pos_y
    
    def update(self):
        if my_color == BLACK:
            self.rect.x += 3
        else:
            self.rect.x += self.boat_change_x
        
        if self.rect.x > 700:
            self.reset_pos()


class Car(pygame.sprite.Sprite):
    """Cars moving forward in traffic lanes."""
    
    def __init__(self):
        super().__init__()
        self.original_pos_y = 0
        self.original_pos_x = 0
        self.change_x = 0
        
        # Randomly select vehicle type
        x = random.randrange(1, 6)
        if x == 1:
            self.image = pygame.image.load('assets/car2.PNG')
        elif x == 2:
            self.image = pygame.image.load('assets/truck.PNG')
        elif x == 3:
            self.image = pygame.image.load('assets/car1.PNG')
        elif x == 4:
            self.image = pygame.image.load('assets/truck2.PNG')
        elif x == 5:
            self.image = pygame.image.load('assets/truck2.PNG')
        elif x == 6:
            self.image = pygame.image.load('assets/cement.PNG')
        
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
    
    def reset_pos(self):
        self.rect.y = self.original_pos_y
        self.rect.x = self.original_pos_x - 100
        
        randomize = [620, 420, 220, 120]
        for i in range(len(randomize)):
            if self.original_pos_y == randomize[i]:
                x = random.randrange(1, 6)
                if x == 1:
                    self.image = pygame.image.load('assets/car2.PNG')
                elif x == 2:
                    self.image = pygame.image.load('assets/truck.PNG')
                elif x == 3:
                    self.image = pygame.image.load('assets/car1.PNG')
                elif x == 4:
                    self.image = pygame.image.load('assets/truck2.PNG')
                elif x == 5:
                    self.image = pygame.image.load('assets/truck2.PNG')
                elif x == 6:
                    self.image = pygame.image.load('assets/cement.PNG')
    
    def update(self):
        if my_color == BLACK:
            self.rect.x += 3
        else:
            self.rect.x += self.change_x
        
        if self.rect.x > 700:
            self.reset_pos()


class Car2(pygame.sprite.Sprite):
    """Cars moving in opposite direction."""
    
    def __init__(self):
        super().__init__()
        self.original_pos_y = 0
        self.original_pos_x = 0
        self.change_x = 0
        
        x = random.randrange(1, 5)
        if x == 1:
            self.image = pygame.image.load('assets/reverseredcar.PNG')
        elif x == 2:
            self.image = pygame.image.load('assets/reversetruck1.PNG')
        elif x == 3:
            self.image = pygame.image.load('assets/reversecement.PNG')
        elif x == 4:
            self.image = pygame.image.load('assets/reversebluecar.PNG')
        elif x == 5:
            self.image = pygame.image.load('assets/reversetruck2.PNG')
        
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
    
    def reset_pos(self):
        self.rect.y = self.original_pos_y
        self.rect.x = self.original_pos_x
        
        randomize = [620, 420, 220, 120]
        for i in range(len(randomize)):
            if self.original_pos_y == randomize[i]:
                x = random.randrange(1, 5)
                if x == 1:
                    self.image = pygame.image.load('assets/reverseredcar.PNG')
                elif x == 2:
                    self.image = pygame.image.load('assets/reversetruck1.PNG')
                elif x == 3:
                    self.image = pygame.image.load('assets/reversecement.PNG')
                elif x == 4:
                    self.image = pygame.image.load('assets/reversebluecar.PNG')
                elif x == 5:
                    self.image = pygame.image.load('assets/reversetruck2.PNG')
    
    def update(self):
        if my_color == BLACK:
            self.rect.x -= 3
        else:
            self.rect.x += self.change_x
        
        if self.rect.x < -180:
            self.reset_pos()


class Player(pygame.sprite.Sprite):
    """Main player character - Plankton."""
    
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/plankton.PNG').convert()
        self.rect = self.image.get_rect()
    
    def update(self):
        self.rect.x += change_x
        self.rect.y += change_y
    
    def reset_pos(self):
        self.rect.y = 730
        self.rect.x = 400


class EPlayer(pygame.sprite.Sprite):
    """Enemy player - Mr. Krabs who shoots projectiles."""
    
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/MrKrabs.PNG').convert()
        self.image.set_colorkey(WHITE)
        self.krab_change_x = 0
        self.rect = self.image.get_rect()
    
    def update(self):
        self.rect.x += self.krab_change_x
        # Bounce off screen edges
        if self.rect.x > 700:
            self.krab_change_x *= -1
        if self.rect.x < 0:
            self.krab_change_x *= -1


class Bullet(pygame.sprite.Sprite):
    """Projectiles shot by Mr. Krabs - randomly shows different characters."""
    
    def __init__(self):
        super().__init__()
        
        x = random.randrange(1, 5)
        if x == 3:
            self.image = pygame.image.load('assets/patrick.PNG')
        elif x > 3:
            self.image = pygame.image.load('assets/spongebob.jpg').convert()
        elif x < 3:
            self.image = pygame.image.load('assets/images.jpg')
        
        self.rect = self.image.get_rect()
    
    def update(self):
        self.rect.y += random.randrange(5, 10)


# Initialize sprite groups
block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()
secret_list = pygame.sprite.Group()
forward_car_list = []
reverse_car_list = []
boat_list = []

# Create forward-moving cars
for i in range(6):
    if i not in [1, 2, 3, 5]:
        block = Car()
        block.rect.x = 0
        block.rect.y = 620 - 100 * i
        block.original_pos_x = block.rect.x
        block.original_pos_y = block.rect.y
        block.change_x = random.randrange(1, 3)
        block_list.add(block)
        all_sprites_list.add(block)
        forward_car_list.append(block)

# Create reverse-moving cars
for i in range(6):
    if i not in [0, 1, 3, 4]:
        block2 = Car2()
        block2.rect.x = 700
        block2.rect.y = 620 - 100 * i
        block2.original_pos_x = block2.rect.x
        block2.original_pos_y = block2.rect.y
        block2.change_x = random.randrange(-3, -1)
        block_list.add(block2)
        all_sprites_list.add(block2)
        reverse_car_list.append(block2)

# Create train
train = Train()
train.rect.x = 0
train.rect.y = 320
train.train_change_x = random.randrange(1, 3)
train.original_pos_x = train.rect.x
train.original_pos_y = train.rect.y
block_list.add(train)
all_sprites_list.add(train)

# Create boat
ship = Boat()
ship.rect.x = 0
ship.rect.y = 520
ship.boat_change_x = random.randrange(1, 3)
ship.original_pos_x = ship.rect.x
ship.original_pos_y = ship.rect.y
block_list.add(ship)
all_sprites_list.add(ship)
boat_list.append(ship)

# Create restaurant
breakfast = Restaurant()
breakfast.rect.x = 0
breakfast.rect.y = -40
all_sprites_list.add(breakfast)

# Create player
player = Player()
player.rect.x = 400
player.rect.y = 730
all_sprites_list.add(player)

# Create Mr. Krabs
player1 = EPlayer()
player1.rect.x = 0
player1.rect.y = 0
player1.krab_change_x = 2
all_sprites_list.add(player1)

# Create secret formula
krab_secret = SecretFormula()
krab_secret.rect.x = 380
krab_secret.rect.y = 20
all_sprites_list.add(krab_secret)
secret_list.add(krab_secret)

# Create police car
popo = Police()
popo.rect.x = 0
popo.rect.y = 220
popo.popo_change_x = 6
block_list.add(popo)
all_sprites_list.add(popo)

# Game variables
change_x = 0
change_y = 0
death = 0
level = 1
score = 0
bullet_speed = 0

# Load Chum Bucket image
chumbucket_pos = 0, 720
chumbucket = pygame.image.load('assets/chumbucket.PNG').convert()

# Load theme sound (optional)
try:
    theme_sound = pygame.mixer.Sound('assets/SpongeBob_Production_Music_Twelfth_Street_Rag.ogg')
except:
    theme_sound = None

# Create road sign positions
road_sign = []
for i in range(10):
    x = 0 + 100 * i
    y = 659
    road_sign.append([x, y])

done = False
clock = pygame.time.Clock()
my_color = LLBLUE

# Set timer for day/night cycle
pygame.time.set_timer(USEREVENT, 8000)

# Main game loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        # Day/night cycle timer
        elif event.type == USEREVENT:
            if my_color == LLBLUE:
                my_color = BLACK
            else:
                my_color = LLBLUE
        
        # Handle player movement
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_y = -7
            elif event.key == pygame.K_RIGHT:
                change_x = 7
            elif event.key == pygame.K_LEFT:
                change_x = -7
            elif event.key == pygame.K_DOWN:
                change_y = 7
        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                change_x = 0
            elif event.key == pygame.K_RIGHT:
                change_x = 0
            elif event.key == pygame.K_UP:
                change_y = 0
            elif event.key == pygame.K_DOWN:
                change_y = 0
    
    # Handle bullet spawning with variable fire rate
    bullet_speed += 20
    if my_color == BLACK:
        bullet_speed += 120  # Increased fire rate at night
    
    if bullet_speed % 600 == 0:
        bullet = Bullet()
        bullet.rect.x = player1.rect.x
        bullet.rect.y = player1.rect.y
        all_sprites_list.add(bullet)
        bullet_list.add(bullet)
    
    # Play theme music if available
    # if theme_sound:
    #     theme_sound.play()
    
    # Draw background
    screen.fill(GREY)
    draw_background(my_color, screen)
    screen.blit(chumbucket, chumbucket_pos)
    
    # Draw train tracks
    for i in range(30):
        x0 = 0 + 50 * i
        y0 = 320
        x1 = 0 + 50 * i
        y1 = 415
        draw_vertical_line(x0, y0, x1, y1)
    
    pygame.draw.line(screen, BROWN, [0, 330], [700, 330], 5)
    pygame.draw.line(screen, BROWN, [0, 405], [700, 405], 5)
    
    # Check collisions with obstacles
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, False)
    for block in blocks_hit_list:
        death += 1
        player.reset_pos()
    
    # Check collision with secret formula
    secrets_hit_list = pygame.sprite.spritecollide(player, secret_list, False)
    for secret in secrets_hit_list:
        level += 1
        score += 100
        player.reset_pos()
        krab_secret.rect.x = random.randrange(0, 650)
        krab_secret.rect.y = 20
        
        # Increase difficulty with each level
        for car in forward_car_list:
            car.change_x += 1
        for car in reverse_car_list:
            car.change_x -= 1
        for boat in boat_list:
            boat.boat_change_x += 1
        
        # Every 6 levels, increase police speed
        if level % 6 == 0:
            popo.popo_change_x += 2
    
    # Check collision with bullets
    bullet_hit_list = pygame.sprite.spritecollide(player, bullet_list, False)
    for bullet in bullet_hit_list:
        player.reset_pos()
    
    # Update and draw all sprites
    all_sprites_list.draw(screen)
    all_sprites_list.update()
    
    # Keep player within screen boundaries
    if player.rect.x < 0:
        change_x *= -1
    elif player.rect.x > 650:
        change_x *= -1
    elif player.rect.y < 0:
        change_y *= -1
    elif player.rect.y > 750:
        change_y *= -1
    
    # Display game stats
    font = pygame.font.SysFont('Arial', 30, True, False)
    
    text = font.render("DEATH:" + str(death), True, WHITE)
    screen.blit(text, [550, 760])
    
    text = font.render("LEVEL:" + str(level), True, WHITE)
    screen.blit(text, [0, 760])
    
    text = font.render("SCORE:" + str(score), True, WHITE)
    screen.blit(text, [550, 730])
    
    pygame.display.flip()
    clock.tick(60)  # 60 FPS

pygame.quit()