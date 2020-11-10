import pygame, sys, random


#! Game Functions
# Putting two floor_surface next to each other
def infinity_floor():
    screen.blit(floor_surface, (floor_x_position, 740))
    screen.blit(floor_surface, (floor_x_position + 576, 740))


# Creating Pipe at the x=288 and y=475 in the middle top of the surface
def create_pipe():
    random_pipe_height = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop=(700, random_pipe_height))
    top_pipe = pipe_surface.get_rect(midbottom=(700, random_pipe_height - 250))
    return bottom_pipe, top_pipe


# Moving Pipe to the left in x = -5 Postion"
def move_pipe(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes

# Draw Pipe 
def draw_pipe(pipes):
    for pipe in pipes:
        screen.blit(pipe_surface, pipe)
    
        
# Display width and height
pygame.init()
screen = pygame.display.set_mode((576, 950))
clock = pygame.time.Clock()




#! Game Variables
gravity = 0.15
bird_movement = 0

# Background-Day surface
background_surface = pygame.image.load("assets/background-day3.png").convert()
background_surface = pygame.transform.scale2x(background_surface)

# Floor Surface
floor_surface = pygame.image.load("assets/base.png").convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_position = 0

# Pip Surface
pipe_surface = pygame.image.load("assets/pipe-red.png").convert()
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)
pipe_height = [575, 400, 475, 300, 600, 200]

# Bird Red
bird_surface = pygame.image.load("assets/redbird-upflap.png").convert()
bird_surface = pygame.transform.scale2x(bird_surface)
bird_rectangle = bird_surface.get_rect(center=(100, 475))



while True:
    
    for event in pygame.event.get():
        
        # Logic: When user hit the exit button, the windows will be close without any error
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        # Logic: When user press Space key, birds will go up -8 in the Y direction"
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement -= 8
                
        # Logic:  Making new pipes
        if event.type == SPAWNPIPE:
            pipe_list.append(create_pipe())
            
              
    # BACKGROUND   
    screen.blit(background_surface, (0, 0))
    
    # BIRD
    bird_movement += gravity
    bird_rectangle.centery += bird_movement
    screen.blit(bird_surface, bird_rectangle)
    
    # PIPE
    pipe_list = move_pipe(pipe_list)
    draw_pipe(pipe_list)
    
    # FLOOR
    floor_x_position -=1
    infinity_floor()
    # In this if statement when left floor is at the zero x position will restart again
    if floor_x_position < -576:
        floor_x_position = 0
        
    pygame.display.update()
    clock.tick(120)
    