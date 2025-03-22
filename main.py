import pygame
import random

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Втеча з лабіринту")

background_color = (0, 0, 0)
cell_size = 40

player_img = pygame.image.load("player.png").convert_alpha()
player_img = pygame.transform.scale(player_img, (cell_size, cell_size))

sword_img = pygame.image.load("sword.png").convert_alpha()
sword_img = pygame.transform.scale(sword_img, (cell_size, cell_size))

chest_img = pygame.image.load("chest.png").convert_alpha()
chest_img = pygame.transform.scale(chest_img, (cell_size, cell_size))

key_img = pygame.image.load("key.png").convert_alpha()
key_img = pygame.transform.scale(key_img, (cell_size, cell_size))

wall_img = pygame.image.load("wall.png").convert_alpha()
wall_img = pygame.transform.scale(wall_img, (cell_size, cell_size))


def clear_area(maze, cx, cy, radius):
    for y in range(max(1, cy - radius), min(len(maze) - 1, cy + radius + 1)):
        for x in range(max(1, cx - radius), min(len(maze[0]) - 1, cx + radius + 1)):
            maze[y][x] = 0


def generate_random_maze(width, height):
    maze = [[1 if x == 0 or x == width - 1 or y == 0 or y == height - 1 else 0 for x in range(width)] for y in
            range(height)]

    for _ in range(width * height // 4):
        x, y = random.randint(1, width - 2), random.randint(1, height - 2)
        maze[y][x] = 1

    player_pos = [1, 1]
    sword_pos = [width - 3, 1]
    chest_pos = [width - 3, height - 3]
    key_pos = [random.randint(1, width - 2), random.randint(1, height - 2)]

    clear_area(maze, *player_pos, 3)
    clear_area(maze, *sword_pos, 3)
    clear_area(maze, *chest_pos, 3)
    clear_area(maze, *key_pos, 3)

    return maze, player_pos, sword_pos, chest_pos, key_pos

def main_menu():
    menu = True
    while menu:
        screen.fill((0, 0, 0))
        draw_button(screen, "Генерувати лабіринт випадково", 150, 200, 500, 100)
        draw_button(screen, "Обрати лабіринт за замовчуванням", 150, 350, 500, 100)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 150 <= x <= 650 and 200 <= y <= 300:
                    return generate_random_maze(20, 15)
                elif 150 <= x <= 650 and 350 <= y <= 450:
                    return default_maze, [1, 1], [17, 1], [17, 9], [5, 5]


def draw_button(screen, text, x, y, w, h):
    pygame.draw.rect(screen, (0, 128, 0), (x, y, w, h))
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, (255, 255, 255))
    screen.blit(text_surface, (x + (w - text_surface.get_width()) / 2, y + (h - text_surface.get_height()) / 2))


default_maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

inventory = []

maze, player_position, sword_position, chest_position, key_position = main_menu()
has_sword = False
chest_open = False

running = True
while running:

    screen.fill(background_color)

    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == 1:
                screen.blit(wall_img, (x * cell_size, y * cell_size))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and player_position[0] > 0 and maze[player_position[1]][
                player_position[0] - 1] == 0:
                player_position[0] -= 1
            if event.key == pygame.K_RIGHT and player_position[0] < len(maze[0]) - 1 and maze[player_position[1]][
                player_position[0] + 1] == 0:
                player_position[0] += 1
            if event.key == pygame.K_UP and player_position[1] > 0 and maze[player_position[1] - 1][
                player_position[0]] == 0:
                player_position[1] -= 1
            if event.key == pygame.K_DOWN and player_position[1] < len(maze) - 1 and maze[player_position[1] + 1][
                player_position[0]] == 0:
                player_position[1] += 1

            if player_position == chest_position and not chest_open:
                if "ключ" in inventory:
                    chest_open = True
                    inventory.append("меч")

            if player_position == key_position and "ключ" not in inventory:
                inventory.append("ключ")

            if player_position == sword_position and not has_sword:
                has_sword = True
                inventory.append("меч")

    if maze[player_position[1]][player_position[0]] == 0:
        screen.blit(player_img, (player_position[0] * cell_size, player_position[1] * cell_size))
    if maze[sword_position[1]][sword_position[0]] == 0 and not has_sword:
        screen.blit(sword_img, (sword_position[0] * cell_size, sword_position[1] * cell_size))
    if maze[chest_position[1]][chest_position[0]] == 0 and not chest_open:
        screen.blit(chest_img, (chest_position[0] * cell_size, chest_position[1] * cell_size))
    if maze[key_position[1]][key_position[0]] == 0 and "ключ" not in inventory:
        screen.blit(key_img, (key_position[0] * cell_size, key_position[1] * cell_size))

    if "ключ" in inventory and "меч" in inventory and chest_open:
        pygame.time.delay(500)
        running = False

    pygame.display.flip()
    pygame.time.wait(100)

pygame.quit()
