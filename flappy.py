import pygame, sys

pygame.init()
def infinity_floor():
    screen.blit(floor_surface, (floor_x_position, 740))
    screen.blit(floor_surface, (floor_x_position + 576, 740))



screen = pygame.display.set_mode((576, 950))
clock = pygame.time.Clock()

#! Game variables
gravity = 0.15
bird_movement = 0



background_surface = pygame.image.load("assets/background-day3.png").convert()
background_surface = pygame.transform.scale2x(background_surface)




floor_surface = pygame.image.load("assets/base.png").convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_position = 0



bird_surface = pygame.image.load("assets/redbird-upflap.png").convert()
bird_surface = pygame.transform.scale2x(bird_surface)
bird_rectangle = bird_surface.get_rect(center=(100, 475))



while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement -= 8
        
        
        
    screen.blit(background_surface, (0, 0))
    
    bird_movement += gravity
    bird_rectangle.centery += bird_movement
    screen.blit(bird_surface, bird_rectangle)
    floor_x_position -=1
    infinity_floor()
    if floor_x_position < -576:
        floor_x_position = 0
    pygame.display.update()
    clock.tick(120)
    