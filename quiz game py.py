import pygame,sys
from pygame.locals import *

SCREENWIDTH, SCREENHEIGHT = 900,700
FPS = 60
score = 0
count=0

game_active = True
pygame.init()
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('quiz game')

bg = pygame.image.load(r'D:\jia\coding and hackathons\purestream\better game main bg.png').convert()

char = pygame.image.load(r'D:\jia\coding and hackathons\python\learning pygame\images\player_stand.png').convert_alpha()
char = pygame.transform.scale2x(char)
char_rect =char.get_rect(center = (150,500))

test_font = pygame.font.Font(r'D:\jia\coding and hackathons\python\learning pygame\text\Pixeltype.ttf', 50) 

quiz_list = ['What is the capital city of Australia?','Which planet is known as the "Red Planet"','What is the smallest country in the world?','What is the name of the longest river in the world?']
option_A_list = ['A) Sydney','A) Venus' ,'A) Monaco' ,'A) Amazon']
option_B_list = ['B) Melbourne','B)Mars' ,'B) Nauru' ,'B) Yamuna' ]
option_C_list = ['C) Canberra','C) Jupiter' ,'C) Tuvalu' ,'C) Nile']
option_D_list = ['D) Brisbane','D) Uranus','D) Vatican City','D) Yangtze']

def ques_x():
    global count, score
    count+=1
    ques_surf = test_font.render(quiz_list[0], False, (64,64,64))
    ques_rect = ques_surf.get_rect(topleft = (100,100))
    pygame.draw.rect(screen, '#c0e8ec', ques_rect,0,10)
    screen.blit(ques_surf, ques_rect)

    A_surf = test_font.render(option_A_list[0], False, (64,64,64))
    A_rect = A_surf.get_rect(topleft = (600,200))
    pygame.draw.rect(screen, '#c0e8ec', A_rect,0,10)
    screen.blit(A_surf, A_rect)
    

    B_surf = test_font.render(option_B_list[0], False, (64,64,64))
    B_rect = B_surf.get_rect(topleft = (600,300))
    pygame.draw.rect(screen, '#c0e8ec', B_rect,0,10)
    screen.blit(B_surf, B_rect)
    

    C_surf = test_font.render(option_C_list[0], False, (64,64,64))
    C_rect = C_surf.get_rect(topleft = (600,400))
    pygame.draw.rect(screen, '#c0e8ec', C_rect,0,10)
    screen.blit(C_surf, C_rect)
    

    D_surf = test_font.render(option_D_list[0], False, (64,64,64))
    D_rect = D_surf.get_rect(topleft = (600,500))
    pygame.draw.rect(screen, '#c0e8ec', D_rect,0,10)
    screen.blit(D_surf, D_rect)
    

    correct_ans = [C_rect,B_rect,D_rect,C_rect]
    
    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if correct_ans[0].collidepoint(event.pos):
                print(event)
                score +=4
                print(score)
                screen.fill('Black')
                quiz_list.pop(0)
                correct_ans.pop(0)
                option_B_list.pop(0)
                option_C_list.pop(0)
                option_D_list.pop(0)
                option_A_list.pop(0)
                ques_x()
                



while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    if game_active:
        screen.blit(bg, (0,0))
        screen.blit(char, char_rect)
        ques_x()
    #else:

    pygame.display.update()
    clock.tick(FPS)

