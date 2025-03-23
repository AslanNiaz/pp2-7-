import pygame
import random
import sys

pygame.init()

# --- Настройки окна ---
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Game with Blocks")
clock = pygame.time.Clock()

# --- Цвета ---
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)  # Игрок
RED = (255, 0, 0)  # Враги
YELLOW = (255, 255, 0)  # Монеты

# --- Игровые переменные ---
player_x = WIDTH // 2 - 25
player_y = HEIGHT - 100
player_speed = 5
player_size = 50

# --- Монеты ---
coins = []
coin_spawn_time = 100
coin_timer = 0
collected_coins = 0

# --- Враги ---
enemies = []
enemy_spawn_time = 120
enemy_timer = 0
enemy_speed = 5
enemy_size = 50

# --- Шрифт ---
font = pygame.font.Font(None, 36)

game_over = False

running = True
while running:
    screen.fill(WHITE)
    
    # --- Обработка событий ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
    
    if not game_over:
        # --- Управление ---
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
            player_x += player_speed
        
        # --- Спавн монет ---
        coin_timer += 1
        if coin_timer >= coin_spawn_time:
            coin_x = random.randint(50, WIDTH - 50)
            coin_y = 0
            coins.append([coin_x, coin_y])
            coin_timer = 0
        
        # --- Движение монет ---
        for coin in coins[:]:
            coin[1] += 3
            if player_x < coin[0] < player_x + player_size and player_y < coin[1] < player_y + player_size:
                coins.remove(coin)
                collected_coins += 1
            if coin[1] > HEIGHT:
                coins.remove(coin)
        
        # --- Спавн врагов ---
        enemy_timer += 1
        if enemy_timer >= enemy_spawn_time:
            enemy_x = random.randint(50, WIDTH - 50)
            enemy_y = 0
            enemies.append([enemy_x, enemy_y])
            enemy_timer = 0
        
        # --- Движение врагов ---
        for enemy in enemies[:]:
            enemy[1] += enemy_speed
            if player_x < enemy[0] < player_x + player_size and player_y < enemy[1] < player_y + player_size:
                game_over = True
            if enemy[1] > HEIGHT:
                enemies.remove(enemy)
        
        # --- Отрисовка ---
        pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))
        for coin in coins:
            pygame.draw.rect(screen, YELLOW, (coin[0], coin[1], 20, 20))
        for enemy in enemies:
            pygame.draw.rect(screen, RED, (enemy[0], enemy[1], enemy_size, enemy_size))
        
        # --- Отображение счета ---
        score_text = font.render(f"Coins: {collected_coins}", True, (0, 0, 0))
        screen.blit(score_text, (WIDTH - 150, 20))
    else:
        # --- Экран окончания игры ---
        game_over_text = font.render("GAME OVER", True, (255, 0, 0))
        screen.blit(game_over_text, (WIDTH // 2 - 50, HEIGHT // 2))
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()
