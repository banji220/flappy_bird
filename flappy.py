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
    top_pipe = pipe_surface.get_rect(midbottom=(700, random_pipe_height - 200))
    return bottom_pipe, top_pipe


# Moving Pipe to the left in x = -5 Postion"
def move_pipe(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes

# Draw Pipe 
def draw_pipe(pipes):
    for pipe in pipes:
        if pipe.bottom >= 800:
            screen.blit(pipe_surface, pipe)
        else:
            flap_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flap_pipe, pipe)
    
# Check Collisions (Birds and Pipes)
def check_collision(pipes):
    for pipe in pipes:
        if bird_rectangle.colliderect(pipe):
            return False
        
    if bird_rectangle.top <= -100 or bird_rectangle.bottom >= 740:
        return False
    
    return True
        

def rotate_bird(bird):
    new_bird = pygame.transform.rotozoom(bird, bird_movement * -3, 1)
    return new_bird
    

def bird_animation():
    new_bird = bird_frames[bird_index]
    new_bird_rectangle = new_bird.get_rect(center=(100, bird_rectangle.centery))
    return new_bird, new_bird_rectangle


def score_display(game_state):
    if game_state == "main_game":
        score_surface = game_font.render(str(int(score)), True, (255, 255, 255))
        score_rectangle = score_surface.get_rect(center=(288, 60))
        screen.blit(score_surface, score_rectangle)
    elif game_state == "game_over":
        score_surface = game_font.render(f"Score: {int(score)}", True, (255, 255, 255))
        score_rectangle = score_surface.get_rect(center=(288, 60))
        screen.blit(score_surface, score_rectangle)
        
        # High Score
        high_score_surface = game_font.render(f"High score: {int(high_score)}", True, (255, 255, 255))
        high_score_rectangle = high_score_surface.get_rect(center=(288, 300))
        screen.blit(high_score_surface, high_score_rectangle)
        

def update_score(score, high_score):
    if score > high_score:
        high_score = score
    return high_score

# Display width and height
pygame.init()
screen = pygame.display.set_mode((576, 950))
clock = pygame.time.Clock()
game_font = pygame.font.Font("04B_19__.TTF", 40)



#! Game Variables
gravity = 0.15
bird_movement = 0
game_active = True
score = 0
high_score = 0

# Background-Day surface
background_surface = pygame.image.load("assets/background-day3.png").convert()
background_surface = pygame.transform.scale2x(background_surface)

# Floor Surface
floor_surface = pygame.image.load("assets/base.png").convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_position = 0


# Bird Red
bird_downflap = pygame.transform.scale2x(pygame.image.load("assets/redbird-downflap.png")).convert_alpha()
bird_midflap = pygame.transform.scale2x(pygame.image.load("assets/redbird-midflap.png")).convert_alpha()
bird_upflap = pygame.transform.scale2x(pygame.image.load("assets/redbird-upflap.png")).convert_alpha()
bird_frames = [bird_downflap, bird_midflap, bird_upflap]
bird_index = 0
bird_surface = bird_frames[bird_index]
bird_rectangle = bird_surface.get_rect(center=(100, 475))
BIRD_FLAP = pygame.USEREVENT + 1
pygame.time.set_timer(BIRD_FLAP, 200)


# Pip Surface
pipe_surface = pygame.image.load("assets/pipe-red.png").convert()
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)
pipe_height = [575, 595, 400, 475, 300, 350, 600, 250]





while True:
    
    for event in pygame.event.get():
        
        # Logic: When user hit the exit button, the windows will be close without any error
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        # Logic: When user press Space key, birds will go up -8 in the Y direction"
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_SPACE and game_active == True:
                bird_movement = 0
                bird_movement -= 6
            
            # This if statement will be run and Tru if User press "Space Key" and the game_active == False (Game_over)
            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True
                pipe_list.clear()
                bird_rectangle.center = (100, 475)
                bird_movement = 0
                score = 0
                
                
        # Logic:  Making new pipes
        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())
            

        if event.type == BIRD_FLAP:
            if bird_index < 2:
                bird_index += 1
            else:
                bird_index = 0
                
            bird_surface, bird_rectangle = bird_animation()
                          
    # BACKGROUND   
    screen.blit(background_surface, (0, 0))
    if game_active:
        # Calling Collision Function
        game_active = check_collision(pipe_list)
        
        # BIRD
        bird_movement += gravity
        rotated_bird = rotate_bird(bird_surface)
        bird_rectangle.centery += bird_movement
        screen.blit(rotated_bird , bird_rectangle)
        
        
        # PIPE
        pipe_list = move_pipe(pipe_list)
        draw_pipe(pipe_list)
        
        # Score Display
        score += 0.01 
        score_display("main_game")
    else:
        high_score = update_score(score, high_score)
        score_display("game_over")
    
    # FLOOR
    # floor_speed
    floor_x_position -=2.5
    infinity_floor()
    # In this if statement when left floor is at the zero x position will restart again
    if floor_x_position <= -576:
        floor_x_position = 0
        
    pygame.display.update()
    clock.tick(120)
    