import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 700
BACKGROUND_COLOR = (31, 31, 31)
WHITE = (255, 255, 255)
FPS = 30

# Card settings
CARD_SIZE = (80, 60)
CARD_PADDING = 10
GRID_SIZE = 4

# Setup the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Memory Puzzle Game")
clock = pygame.time.Clock()

# Load images or use simple colors
def load_images():
    images = []
    for i in range(1, 9):  # Assuming 8 pairs of cards
        image = pygame.Surface(CARD_SIZE)
        image.fill((random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)))
        images.append(image)
    return images * 2  # Duplicate for pairs

class Card:
    def __init__(self, image, pos):
        self.image = image
        self.rect = pygame.Rect(pos, CARD_SIZE)
        self.is_open = False
        self.is_matched = False

    def draw(self, surface):
        if self.is_open or self.is_matched:
            surface.blit(self.image, self.rect.topleft)
        else:
            pygame.draw.rect(surface, WHITE, self.rect)

    def handle_click(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            return True
        return False

def setup_cards():
    images = load_images()
    random.shuffle(images)
    cards = []
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            pos = (i * (CARD_SIZE[0] + CARD_PADDING) + 100, j * (CARD_SIZE[1] + CARD_PADDING) + 100)
            cards.append(Card(images.pop(), pos))
    return cards

def game_loop():
    cards = setup_cards()
    running = True
    open_cards = []

    start_time = time.time()
    game_time = 60  # seconds

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for card in cards:
                    if card.handle_click() and not card.is_open and not card.is_matched:
                        card.is_open = True
                        open_cards.append(card)
                        if len(open_cards) == 2:
                            pygame.time.wait(500)  # Wait half a second
                            if open_cards[0].image == open_cards[1].image:
                                open_cards[0].is_matched = True
                                open_cards[1].is_matched = True
                            else:
                                open_cards[0].is_open = False
                                open_cards[1].is_open = False
                            open_cards = []

        # Check for game time
        if time.time() - start_time > game_time:
            print("Time's up!")
            running = False

        screen.fill(BACKGROUND_COLOR)
        for card in cards:
            card.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    game_loop()
