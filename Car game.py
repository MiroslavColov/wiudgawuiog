import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 1200 , 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the blocks")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load player image (make sure to use the correct path to the image file)
player_image = pygame.image.load('Porsche.jpeg')  # Replace with your player image
player_image = pygame.transform.scale(player_image, (100, 50))  # Resize player image to fit

# Load block image (replace with the correct path to your block image)
block1_image = pygame.image.load('Konus.jpeg')  # Replace with your block image
block1_image = pygame.transform.scale(block1_image, (50, 70))  # Resize block image to fit

block1_size = 50
block1_pos = [random.randint(0, WIDTH - block1_size), 0]
block1_speed = 5

score = 0
font = pygame.font.SysFont("Lato", 30)

# Player position
player_size = 50
player_pos = [WIDTH // 2, HEIGHT - player_size]
player_speed = 4

clock = pygame.time.Clock()
FPS = 60

def detect_collision1(player_pos, block_pos):
    px, py = player_pos
    bx, by = block_pos
    return (
        px < bx + block1_size and
        px + player_size > bx and
        py < by + block1_size and
        py + player_size > by
    )

def draw_objects():
    screen.fill(BLACK)
    screen.blit(player_image, player_pos)  # Draw the player image
    screen.blit(block1_image, block1_pos)  # Draw the block image
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    pygame.display.flip()

game_over = False
while not game_over:
    clock.tick(FPS)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= 7
    if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - player_size:
        player_pos[0] += 7

    # Move block
    block1_pos[1] += block1_speed
    if block1_pos[1] > HEIGHT:
        block1_pos = [random.randint(0, WIDTH - block1_size), 0]
        score += 1
        block1_speed += 2
        player_speed += 1

        if block1_speed > 20:
            block1_speed = 20

        if player_speed > 15:
            player_speed = 15

    # Check for collision
    if detect_collision1(player_pos, block1_pos):
        game_over = True

    # Draw objects
    draw_objects()

# Once game over, show score and exit
screen.fill(BLACK)
game_over_text = font.render("GAME OVER !!!", True, WHITE)
final_score_text = font.render(f"FINAL SCORE: {score}", True, WHITE)
screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 40))
screen.blit(final_score_text, (WIDTH // 2 - final_score_text.get_width() // 2, HEIGHT // 2))
pygame.display.flip()

pygame.time.wait(3000)
pygame.quit()



