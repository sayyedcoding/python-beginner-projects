import pygame
import sys

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 400
MAZE = [
    "####################",
    "#S#      #         #",
    "# #### #   #########",
    "# #    #      #    #",
    "# #### ########## # #",
    "#    # #        # # #",
    "#### # ######## # # #",
    "#  # #     # # #   #",
    "# ######### # # ####",
    "#       #   #   #  E",
    "####################"
]
BLOCK_SIZE = WIDTH // len(MAZE[0])

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Game")

# Load images
player_image = pygame.image.load("player.png")
player_image = pygame.transform.scale(player_image, (BLOCK_SIZE, BLOCK_SIZE))

# Load fonts
font = pygame.font.Font(None, 36)

# Find the start and end positions
start_pos = (0, 1)
end_pos = (len(MAZE[0]) - 1, len(MAZE) - 2)

# Player position
player_x, player_y = start_pos

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and MAZE[player_y - 1][player_x] != '#':
        player_y -= 1
    if keys[pygame.K_DOWN] and MAZE[player_y + 1][player_x] != '#':
        player_y += 1
    if keys[pygame.K_LEFT] and MAZE[player_y][player_x - 1] != '#':
        player_x -= 1
    if keys[pygame.K_RIGHT] and MAZE[player_y][player_x + 1] != '#':
        player_x += 1

    # Check if the player reached the end
    if (player_x, player_y) == end_pos:
        text = font.render("You Win!", True, WHITE)
        screen.blit(text, (WIDTH // 2 - 80, HEIGHT // 2))
        pygame.display.flip()
        pygame.time.delay(2000)
        running = False

    # Draw the maze
    screen.fill(BLACK)
    for y, row in enumerate(MAZE):
        for x, cell in enumerate(row):
            if cell == '#':
                pygame.draw.rect(screen, WHITE, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
    screen.blit(player_image, (player_x * BLOCK_SIZE, player_y * BLOCK_SIZE))
    pygame.display.flip()

# Quit the game
pygame.quit()
sys.exit()
