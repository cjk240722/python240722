import pygame
import sys

# 게임 화면 크기
WIDTH, HEIGHT = 800, 600

# 색상 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# 캐릭터 클래스 정의
class Character(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

# pygame 초기화
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Battle Legends')

# 캐릭터 인스턴스 생성
all_sprites = pygame.sprite.Group()
player1 = Character(RED, WIDTH // 4, HEIGHT // 2)
player2 = Character(BLUE, 3 * WIDTH // 4, HEIGHT // 2)

all_sprites.add(player1)
all_sprites.add(player2)

clock = pygame.time.Clock()

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    all_sprites.update()

    screen.fill(BLACK)
    all_sprites.draw(screen)
    
    pygame.display.flip()
    clock.tick(30)
