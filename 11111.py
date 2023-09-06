import pygame
import random

# 初始化pygame
pygame.init()

# 设置窗口大小
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("流星划过")

# 定义流星类
class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("meteor.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, width)
        self.rect.y = random.randint(-100, -50)
        self.speed = random.randint(5, 10)

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > height:
            self.rect.x = random.randint(0, width)
            self.rect.y = random.randint(-100, -50)
            self.speed = random.randint(5, 10)

# 加载背景图像
background = pygame.image.load("background.jpg").convert()

# 创建流星精灵组
meteors = pygame.sprite.Group()
for _ in range(20):
    meteor = Meteor()
    meteors.add(meteor)


# 退出游戏
pygame.quit()