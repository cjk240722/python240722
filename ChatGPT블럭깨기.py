import pygame
import random

# 게임 초기화
pygame.init()

# 화면 크기 설정
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Block Breaker")

# 색상 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# 공 클래스
class Ball:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.radius = 10
        self.dx = 4
        self.dy = -4
        self.color = WHITE
    
    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
    
    def move(self):
        self.x += self.dx
        self.y += self.dy
        
        # 벽 충돌 검사
        if self.x - self.radius < 0 or self.x + self.radius > WIDTH:
            self.dx *= -1
        if self.y - self.radius < 0:
            self.dy *= -1
        if self.y + self.radius > HEIGHT:
            return False
        return True

# 패들 클래스
class Paddle:
    def __init__(self):
        self.width = 400
        self.height = 10
        self.x = (WIDTH - self.width) // 2
        self.y = HEIGHT - self.height - 20
        self.color = BLUE
        self.speed = 10
    
    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
    
    def move(self, dx):
        self.x += dx
        if self.x < 0:
            self.x = 0
        if self.x > WIDTH - self.width:
            self.x = WIDTH - self.width

# 블록 클래스
class Block:
    def __init__(self, x, y):
        self.width = 60
        self.height = 20
        self.x = x
        self.y = y
        self.color = RED
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)

# 게임 설정
ball = Ball()
paddle = Paddle()
blocks = [Block(x * 70 + 20, y * 30 + 20) for x in range(10) for y in range(5)]
clock = pygame.time.Clock()
running = True

while running:
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # 키보드 입력 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.move(-paddle.speed)
    if keys[pygame.K_RIGHT]:
        paddle.move(paddle.speed)
    
    # 공 이동
    if not ball.move():
        print("Game Over!")
        running = False
    
    # 충돌 처리
    ball_rect = pygame.Rect(ball.x - ball.radius, ball.y - ball.radius, ball.radius * 2, ball.radius * 2)
    if ball_rect.colliderect(paddle.x, paddle.y, paddle.width, paddle.height):
        ball.dy *= -1
    
    for block in blocks[:]:
        if ball_rect.colliderect(block.rect):
            ball.dy *= -1
            blocks.remove(block)
    
    # 화면 업데이트
    screen.fill(BLACK)
    ball.draw()
    paddle.draw()
    for block in blocks:
        block.draw()
    pygame.display.flip()
    
    # 프레임 속도 조절
    clock.tick(60)

pygame.quit()
