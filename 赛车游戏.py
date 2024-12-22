import pygame
import random

# 初始化pygame
pygame.init()

# 屏幕设置
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("赛车小游戏")

# 颜色定义
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# 玩家车辆
class Car(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def move_left(self, pixels):
        self.rect.x -= pixels
        if self.rect.x < 0:
            self.rect.x = 0

    def move_right(self, pixels):
        self.rect.x += pixels
        if self.rect.x > screen_width - self.rect.width:
            self.rect.x = screen_width - self.rect.width

# 障碍物
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += 5
        if self.rect.y > screen_height:
            self.rect.y = -self.rect.height
            self.rect.x = random.randrange(screen_width - self.rect.width)

# 游戏初始化
all_sprites_list = pygame.sprite.Group()
car = Car(RED, 50, 50)
car.rect.x = screen_width // 2 - 25
car.rect.y = screen_height - 100

obstacle = Obstacle(YELLOW, 50, 50)
obstacle.rect.x = random.randrange(screen_width - obstacle.rect.width)
obstacle.rect.y = -obstacle.rect.height

all_sprites_list.add(car)
all_sprites_list.add(obstacle)

# 游戏循环
clock = pygame.time.Clock()
game_over = False
score = 0

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        car.move_left(5)
    if keys[pygame.K_RIGHT]:
        car.move_right(5)

    all_sprites_list.update()
    
    # 检测碰撞
    if pygame.sprite.collide_rect(car, obstacle):
        game_over = True

    # 绘制
    screen.fill(BLACK)
    all_sprites_list.draw(screen)
    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(score), 1, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.flip()

    clock.tick(60)
    score += 1

pygame.quit()
