import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# --- Configuration & Constants ---
WIDTH, HEIGHT = 800, 600
BLOCK_SIZE = 20
FPS = 2# Game speed

# --- Modern Color Palette ---
BG_COLOR = (30, 30, 40)          # Dark grey/blue background
GRID_COLOR = (40, 40, 50)        # Subtle grid lines
SNAKE_HEAD_COLOR = (0, 255, 100) # Bright neon green
SNAKE_BODY_COLOR = (0, 200, 80)  # Slightly darker green
FOOD_COLOR = (255, 60, 60)       # Bright red
TEXT_COLOR = (240, 240, 240)

# --- Setup Display ---
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Modern Python Snake")
clock = pygame.time.Clock()
font = pygame.font.SysFont("bahnschrift", 28)

def draw_grid():
    """Draws a subtle background grid for a modern look."""
    for x in range(0, WIDTH, BLOCK_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, BLOCK_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (WIDTH, y))

def main():
    # Snake initial state: starts in the middle
    snake = [(WIDTH // 2, HEIGHT // 2)]
    dx, dy = BLOCK_SIZE, 0  # Starts moving right
    score = 0

    def spawn_food():
        """Spawns food in a random location not occupied by the snake."""
        while True:
            x = random.randrange(0, WIDTH, BLOCK_SIZE)
            y = random.randrange(0, HEIGHT, BLOCK_SIZE)
            if (x, y) not in snake:
                return (x, y)
                
    food = spawn_food()
    running = True
    game_over = False

    while running:
        # 1. Handle Events (Keyboard Input)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if not game_over:
                    # No restrictions - instantly change to any direction!
                    if event.key == pygame.K_w:
                        dx, dy = 0, -BLOCK_SIZE
                    elif event.key == pygame.K_s:
                        dx, dy = 0, BLOCK_SIZE
                    elif event.key == pygame.K_a:
                        dx, dy = -BLOCK_SIZE, 0
                    elif event.key == pygame.K_d:
                        dx, dy = BLOCK_SIZE, 0
                else:
                    # Restart game on SPACE
                    if event.key == pygame.K_SPACE:
                        main()
                        return

        if not game_over:
            # 2. Update Game Logic
            new_head = (snake[0][0] + dx, snake[0][1] + dy)

            # Check for collisions with walls or self
            if (new_head[0] < 0 or new_head[0] >= WIDTH or
                new_head[1] < 0 or new_head[1] >= HEIGHT or
                new_head in snake):
                game_over = True
            else:
                snake.insert(0, new_head) # Move head forward
                
                # Check if food is eaten
                if new_head == food:
                    score += 1
                    food = spawn_food()
                else:
                    snake.pop() # Remove tail if no food eaten

        # 3. Render Graphics
        screen.fill(BG_COLOR)
        draw_grid()

        # Draw Food (Shiny Circle)
        food_rect = pygame.Rect(food[0], food[1], BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.circle(screen, FOOD_COLOR, food_rect.center, BLOCK_SIZE // 2 - 2)

        # Draw Snake (Rounded Rectangles)
        for i, segment in enumerate(snake):
            color = SNAKE_HEAD_COLOR if i == 0 else SNAKE_BODY_COLOR
            rect = pygame.Rect(segment[0] + 1, segment[1] + 1, BLOCK_SIZE - 2, BLOCK_SIZE - 2)
            pygame.draw.rect(screen, color, rect, border_radius=5)

        # Draw Score
        score_text = font.render(f"Score: {score}", True, TEXT_COLOR)
        screen.blit(score_text, [15, 15])

        # Draw Game Over Screen
        if game_over:
            # Create a dark semi-transparent overlay
            overlay = pygame.Surface((WIDTH, HEIGHT))
            overlay.set_alpha(150)
            overlay.fill((0, 0, 0))
            screen.blit(overlay, (0, 0))
            
            over_text = font.render("GAME OVER - Press SPACE to Restart", True, (255, 100, 100))
            text_rect = over_text.get_rect(center=(WIDTH/2, HEIGHT/2))
            screen.blit(over_text, text_rect)

        # Update display and control frame rate
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()