import pygame,sys
from pygame.locals import *
from random import randint
pygame.init()


def display_score():
    current_time = int(pygame.time.get_ticks()/1000) - start_time
    score_surf = test_font.render(f'Score: {current_time}', False, (64,64,64))
    score_rect = score_surf.get_rect(center= (400,50))
    pygame.draw.rect(screen, '#c0e8ec', score_rect,0,10)
    pygame.draw.rect(screen, 'Gray', score_rect, 1,10)
    screen.blit(score_surf,score_rect)

    return current_time 

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5
            if obstacle_rect.bottom == 300:
                screen.blit(snail_surface, obstacle_rect)
            else:
                screen.blit(fly_surf, obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]   #obstacle is not copied to the list when it leaves the screen
        return obstacle_list
    else:
        return []

def collisions(player,obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True

screen = pygame.display.set_mode((800,400))  #tuple(width,hight)
pygame.display.set_caption('game')

clock = pygame.time.Clock() #clock object
start_time = 0
player_gravity = 0
game_active = False
score = 0    #initialise score as 0

test_font = pygame.font.Font(r'D:\jia\coding and hackathons\python\learning pygame\text\Pixeltype.ttf', 50)             #tuple(font type, size)
sky_surface = pygame.image.load(r'D:\jia\coding and hackathons\python\learning pygame\images\Sky.png').convert()    #use r'' and make it a raw string to avoid escape sequences. or use double backslashh (\\)
ground_surface = pygame.image.load(r'D:\jia\coding and hackathons\python\learning pygame\images\ground.png').convert()  #convert makes it so that pygame can use it better or smth

#obstacles
snail_surface = pygame.image.load(r'D:\jia\coding and hackathons\python\learning pygame\images\snail1.png').convert_alpha()   #convert_alpha makes it so that the transparent values stay transparent

fly_surf = pygame.image.load(r'D:\jia\coding and hackathons\python\learning pygame\images\Fly1.png').convert_alpha()

obstacle_rect_list = []


#player variables
player_surf = pygame.image.load(r'D:\jia\coding and hackathons\python\learning pygame\images\player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))    #draws a rectangle around the surface
                                                            #creates a position variable tuple


#intro screen
player_stand = pygame.image.load(r'D:\jia\coding and hackathons\python\learning pygame\images\player_stand.png').convert_alpha()
player_stand = pygame.transform.scale2x(player_stand)       #(image object(width, height))
player_stand_rect = player_stand.get_rect(center = (400,200))
#text1
player_text_1 = test_font.render('Pixel Runner', False, (111,196,169))
playertxt1_rect = player_text_1.get_rect(center = (400,100))

#text2
game_message = test_font.render('Press space to run', False, (111,196,169))
game_message_rect = game_message.get_rect(center = (400,320))

#timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 700)     




while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos):
                    if player_rect.bottom >= 300:
                        player_gravity = -20    
                    
            if event.type == KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if player_rect.bottom >= 300:
                        player_gravity = -20
        else:
            if event.type == KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                
                start_time = int(pygame.time.get_ticks()/1000)
        
        if event.type == obstacle_timer and game_active:    #this block can be placed in if game_active 
            if randint(0,2):   #randomly assigns 0/1 i.e t/f
                obstacle_rect_list.append(snail_surface.get_rect(midbottom = (randint(900,11000), 300)))
            else:
                obstacle_rect_list.append(fly_surf.get_rect(midbottom = (randint(900,11000), 210)))

    if game_active:                                    
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0,300))

        #pygame.draw.rect(screen, '#c0e8ec', score_rect,0,10)
        #pygame.draw.rect(screen, '#c0e8ec', score_rect, 2,10)
        
        score = display_score()

       
        

        #obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)


        #PLAYER 
        player_gravity += 1
        player_rect.y += player_gravity
        #player_rect.x +=4
        #if player_rect.x > 900:
        #    player_rect.x = 0
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surf, player_rect)

        #collisions
        game_active = collisions(player_rect, obstacle_rect_list)
        
    else:
        screen.fill((94,129,162))
        screen.blit(player_stand, player_stand_rect)
        #resseting everything
        obstacle_rect_list.clear()    #clears the list so the position of the collided obstacle changes
        player_rect.midbottom = (80,300)   
        player_gravity = 0

        #score variables are created here since score keeps changing
        score_message = test_font.render(f'Your Score: {score}', False,(111,196,169) )
        score_message_rect = score_message.get_rect(center = (400,320) )
        screen.blit(player_text_1, playertxt1_rect)

        if score == 0:
            screen.blit(game_message, game_message_rect)
        else:
            screen.blit(score_message, score_message_rect)

    pygame.display.update()
    clock.tick(60) #frame rate

  


