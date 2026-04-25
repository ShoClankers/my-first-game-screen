import pygame 
pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("First Game Screen")

image = pygame.image.load("mario.png")

image = pygame.transform.scale(image, (300, 300))
image_rect = image.get_rect(center=(250, 250))

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((128, 128, 128))  
    screen.blit(image, image_rect)

    pygame.display.flip()

pygame.quit()