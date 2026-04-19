import pygame
import math
pygame.init()

pygame.display.set_caption("Testing Chamber")
SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 800
WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
BACKGROUND = "white"
clock = pygame.time.Clock()

bulletSound = pygame.mixer.Sound("single-pistol-gunshot-42-40781.wav")

class Player(object):
    def __init__(self, x, y, vel, enemy=False):
        self.radius = 27
        self.x = x
        self.y = y
        self.vel = vel
        self.enemy = enemy
        self.gun_width = 20
        self.gun_height = 72
    
    def draw(self, WINDOW, BACKGROUND):
        WINDOW.fill(BACKGROUND)
        gun = pygame.Rect(self.x - self.gun_width // 2, self.y - self.gun_height, self.gun_width, self.gun_height)
        pygame.draw.rect(WINDOW, "gray", gun)
        pygame.draw.circle(WINDOW, "black", (self.x, self.y), self.radius)
        pygame.draw.circle(WINDOW, "red", (self.x, self.y), self.radius - 2)
        pygame.display.update()

class Projectile(object):
    def __init__(self, x, y, vel=20, width=14, height=20):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.vel = vel
    
    def draw(self, WINDOW):
        bullet = pygame.Rect(self.x - self.width // 2, self.y - main_player.gun_height - self.height, self.width, self.height)
        pygame.draw.rect(WINDOW, "orange", bullet)
        pygame.display.update()

class Rotation(object):
    def __init__(self, image, angle=0):
        self.image = image
        self.angle = angle
    
    def draw(self, WINDOW):
        global SCREEN_WIDTH
        global SCREEN_HEIGHT
        global BACKGROUND

        picture = pygame.image.load(self.image)
        rotated = pygame.transform.rotate(picture, self.angle)
        WINDOW.fill(BACKGROUND)
        WINDOW.blit(rotated, (200, 100))
        pygame.draw.circle(WINDOW, "red", (200, 100), 5)
        self.angle += 90
        pygame.display.flip()


# Variables
main_player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 10)
bullets = []
spaceHold = False

# wheel = Rotation("wheel.jpg")
# shrek = Rotation("shrek.jpg")
# plane = Rotation("coordinateplane.jpg") # 713 x 500

# Methods
def shoot():
    global spaceHold
    global bullets

    if keys[pygame.K_SPACE]:
        if not spaceHold:
            bullets.append(Projectile(main_player.x, main_player.y))
            spaceHold = True
            # bulletSound.play()
    else:
        spaceHold = False

# Main Loop
run = True
FPS = 30
while run:
    clock.tick(FPS)

    # Boundaries
    upper_boundary = main_player.y - main_player.radius > 5
    lower_boundary = main_player.y + main_player.radius < SCREEN_HEIGHT - 5
    left_boundary = main_player.x - main_player.radius > 5
    right_boundary = main_player.x + main_player.radius < SCREEN_WIDTH - 5

    # Closes when application is terminated
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    

    # wheel.draw(WINDOW)
    # shrek.draw(WINDOW)
    # plane.draw(WINDOW)


    for bullet in bullets:
        if bullet.y > 0:
            bullet.y -= bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
    
    keys = pygame.key.get_pressed()
    # Multi-Directional Movement
    if keys[pygame.K_w] and keys[pygame.K_d] and upper_boundary and right_boundary:
        main_player.x += main_player.vel
        main_player.y -= main_player.vel
        shoot()
    elif keys[pygame.K_s] and keys[pygame.K_d] and lower_boundary and right_boundary:
        main_player.x += main_player.vel
        main_player.y += main_player.vel
        shoot()
    elif keys[pygame.K_w] and keys[pygame.K_a] and upper_boundary and left_boundary:
        main_player.x -= main_player.vel
        main_player.y -= main_player.vel
        shoot()
    elif keys[pygame.K_s] and keys[pygame.K_a] and lower_boundary and left_boundary:
        main_player.x -= main_player.vel
        main_player.y += main_player.vel
        shoot()
    # Cardinal Movement
    elif keys[pygame.K_w] and upper_boundary:
        main_player.y -= main_player.vel
        shoot()
    elif keys[pygame.K_s] and lower_boundary:
        main_player.y += main_player.vel
        shoot()
    elif keys[pygame.K_a] and left_boundary:
        main_player.x -= main_player.vel
        shoot()
    elif keys[pygame.K_d] and right_boundary:
        main_player.x += main_player.vel
        shoot()
    # Standing Shooting
    shoot()
    
    main_player.draw(WINDOW, BACKGROUND)
    for bullet in bullets:
        bullet.draw(WINDOW)

    # Bullet Checker
    if len(bullets) > 60:
        pygame.quit()

pygame.quit()