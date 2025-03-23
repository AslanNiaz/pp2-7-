import pygame
import sys

pygame.init()

# Настройки окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Paint Tool")
clock = pygame.time.Clock()

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Начальные параметры
screen.fill(WHITE)
drawing = False
last_pos = None
brush_size = 5
color = BLACK
mode = "brush"  # brush, rect, circle, eraser

# Функция рисования линии
def draw_line(screen, color, start, end, width):
    pygame.draw.line(screen, color, start, end, width)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                mode = "brush"
            elif event.key == pygame.K_r:
                mode = "rect"
            elif event.key == pygame.K_c:
                mode = "circle"
            elif event.key == pygame.K_e:
                mode = "eraser"
            elif event.key == pygame.K_1:
                color = BLACK
            elif event.key == pygame.K_2:
                color = RED
            elif event.key == pygame.K_3:
                color = GREEN
            elif event.key == pygame.K_4:
                color = BLUE
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            last_pos = event.pos
            start_pos = event.pos
        
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            if mode == "rect":
                end_pos = event.pos
                width = abs(end_pos[0] - start_pos[0])
                height = abs(end_pos[1] - start_pos[1])
                pygame.draw.rect(screen, color, (min(start_pos[0], end_pos[0]), min(start_pos[1], end_pos[1]), width, height), 2)
            elif mode == "circle":
                end_pos = event.pos
                radius = int(((end_pos[0] - start_pos[0])**2 + (end_pos[1] - start_pos[1])**2) ** 0.5)
                pygame.draw.circle(screen, color, start_pos, radius, 2)
        
        elif event.type == pygame.MOUSEMOTION:
            if drawing and mode == "brush":
                draw_line(screen, color, last_pos, event.pos, brush_size)
                last_pos = event.pos
            elif drawing and mode == "eraser":
                draw_line(screen, WHITE, last_pos, event.pos, brush_size * 2)
                last_pos = event.pos

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
