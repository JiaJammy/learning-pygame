import pygame,sys
from pygame.locals import *

SCREENWIDTH, SCREENHEIGHT = 900,700
FPS = 60
score = 0
count=0

game_active = False
pygame.init()
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('quiz game')
font_50 = pygame.font.Font(r'D:\jia\coding and hackathons\python\learning pygame\text\Pixeltype.ttf', 50)
font_100 = pygame.font.Font(r'D:\jia\coding and hackathons\python\learning pygame\text\Pixeltype.ttf', 100)

bg = pygame.image.load(r'D:\jia\coding and hackathons\python\learning pygame\images\quiz game temp bg.png').convert()

char = pygame.image.load(r'D:\jia\coding and hackathons\python\learning pygame\images\player_stand.png').convert_alpha()
char = pygame.transform.scale2x(char)
char_rect =char.get_rect(center = (150,500))

index = 0
correct_ans = []

quiz_list = ['What is the capital city of Australia?','Which planet is known as the "Red Planet"','What is the smallest country in the world?','What is the name of the longest river in the world?']
option_A_list = ['A) Sydney','A) Venus' ,'A) Monaco' ,'A) Amazon']
option_B_list = ['B) Melbourne','B)Mars' ,'B) Nauru' ,'B) Yamuna' ]
option_C_list = ['C) Canberra','C) Jupiter' ,'C) Tuvalu' ,'C) Nile']
option_D_list = ['D) Brisbane','D) Uranus','D) Vatican City','D) Yangtze']

def ques_x(index):
    global score, game_active,correct_ans
    ques_surf = font_50.render(quiz_list[index], False, '#C6C9CB')
    ques_rect = ques_surf.get_rect(topleft = (150,100))
    pygame.draw.rect(screen, '#172F43', ques_rect,0,10)
    screen.blit(ques_surf, ques_rect)

    A_surf = font_50.render(option_A_list[index], False, '#C6C9CB')
    A_rect = A_surf.get_rect(topleft = (600,200))
    pygame.draw.rect(screen, '#172F43', A_rect,0,10)
    screen.blit(A_surf, A_rect)
    

    B_surf = font_50.render(option_B_list[index], False, '#C6C9CB')
    B_rect = B_surf.get_rect(topleft = (600,300))
    pygame.draw.rect(screen, '#172F43', B_rect,0,10)
    screen.blit(B_surf, B_rect)
    

    C_surf = font_50.render(option_C_list[index], False, '#C6C9CB')
    C_rect = C_surf.get_rect(topleft = (600,400))
    pygame.draw.rect(screen, '#172F43', C_rect,0,10)
    screen.blit(C_surf, C_rect)
    

    D_surf = font_50.render(option_D_list[index], False, '#C6C9CB')
    D_rect = D_surf.get_rect(topleft = (600,500))
    pygame.draw.rect(screen, '#172F43', D_rect,0,10)
    screen.blit(D_surf, D_rect)
    

    correct_ans = [C_rect,B_rect,D_rect,C_rect]
              
def game_screen():  
    screen.fill((94,129,162))
    play = font_100.render(' PRESS ENTER TO PLAY!', False, '#C6C9CB')
    play_rect = play.get_rect(center = (450,400))
    pygame.draw.rect(screen, '#172F43', play_rect,0,5)
    screen.blit(play, play_rect)

game_screen()   
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if len(correct_ans) > 0:
                print(correct_ans[index].collidepoint(event.pos))
            if len(correct_ans) > 0 and correct_ans[index].collidepoint(event.pos):
                screen.blit(bg, (0,0))
                screen.blit(char, char_rect)
                index += 1
                ques_x(index)
            if len(correct_ans) == 0 and pygame.mouse.get_pressed()[0] == True:
                print(pygame.mouse.get_pressed())
                screen.blit(bg, (0,0))
                screen.blit(char, char_rect)
                ques_x(index)

    pygame.display.update()
    clock.tick(FPS)

            

                    
            


        
