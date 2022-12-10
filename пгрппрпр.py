import pygame

WIDTH = 640
HEIGHT = 420
FPS = 60
WHITE_COLOR = (255, 255, 255)
RED_COLOR =   (255, 0,   0)
GREEN_COLOR = (0,   255, 0)
BLUE_COLOR =  (0,   0,   255)
YELLOW_COLOR =  (255, 255, 51)
BLACK_COLOR = (0, 0, 0)

pygame.init()
surface = pygame.display.set_mode((WIDTH, HEIGHT))
surface.fill(WHITE_COLOR)
pygame.display.set_caption("Первая программа на PyGame")
pygame.display.set_icon(pygame.image.load("icon.jpeg.jpg"))
background_image = pygame.image.load("cringe.jpg")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
surface.blit(background_image, (0,0))
pygame.display.update()

size = 75


pygame.draw.ellipse(surface, WHITE_COLOR, (270, 50, 100, 100),  50)
pygame.draw.ellipse(surface, WHITE_COLOR, (270, 150, 100, 150),  50)
pygame.draw.ellipse(surface, WHITE_COLOR, (270, 300, 100, 100),  50)

pygame.draw.rect(surface, BLUE_COLOR, (WIDTH//2-3, HEIGHT//2-3, 6, 6))
pygame.draw.rect(surface, BLUE_COLOR, (WIDTH//2-3, HEIGHT//2.5, 6, 6))

pygame.draw.rect(surface, BLACK_COLOR, (WIDTH//1.9, HEIGHT//4.8, 14, 6))
pygame.draw.rect(surface, BLACK_COLOR, (WIDTH//2.1, HEIGHT//4.8, 14, 6))
pygame.draw.rect(surface, BLACK_COLOR, (WIDTH//2-3, HEIGHT//3.6, 6, 6))


pygame.display.update()

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    clock.tick(FPS)