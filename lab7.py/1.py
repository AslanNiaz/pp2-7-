import pygame
import time
import math

# Initialize Pygame
pygame.init()

# Load the Mickey clock face
clock_face = pygame.image.load(r'mickeyclock.jpeg')
width, height = clock_face.get_size()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mickey Clock")

# Center of the clock
center_x, center_y = width // 2, height // 2

# Lengths of Mickey's hands
minute_hand_length = 230
second_hand_length = 300

def draw_hand(angle, length, color, thickness):
    end_x = center_x + length * math.cos(math.radians(angle))
    end_y = center_y - length * math.sin(math.radians(angle))
    pygame.draw.line(screen, color, (center_x, center_y), (end_x, end_y), thickness)

def main():
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Get current time
        current_time = time.localtime()
        seconds = current_time.tm_sec
        minutes = current_time.tm_min

        # Calculate angles (12 o'clock is 90 degrees)
        second_angle = 90 - (seconds * 6)
        minute_angle = 90 - (minutes * 6)

        # Draw clock
        screen.blit(clock_face, (0, 0))

        # Draw Mickey's hands
        draw_hand(minute_angle, minute_hand_length, (0, 0, 0), 8)  # Right hand (minutes)
        draw_hand(second_angle, second_hand_length, (255, 0, 0), 4)  # Left hand (seconds)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__== "__main__":
    main()