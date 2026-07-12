import pygame
import random
import sys
import os
import asyncio

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
pygame.mixer.init(44100, -16, 2, 2048)

def resource_path(path):
    if getattr(sys, "frozen", False):
        return os.path.join(os.path.dirname(sys.executable), "_internal", path)
    return path

MUSIC_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(MUSIC_END)

def play_music():
    """Start the music once (not looping via play(-1), which is unreliable
    in the browser). MUSIC_END fires when it finishes and is handled in
    each screen's event loop to restart it manually."""
    try:
        pygame.mixer.music.load(resource_path(MENU_MUSIC))
        pygame.mixer.music.play()
    except pygame.error:
        pass

def handle_music_end(event):
    if event.type == MUSIC_END:
        try:
            pygame.mixer.music.play()
        except pygame.error:
            pass

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH,HEIGHT), pygame.SCALED)
pygame.display.set_caption("The Number festival")

icon = pygame.image.load(resource_path('icon.png'))
pygame.display.set_icon(icon)

FONT_FILE = 'PixelOperator-Bold.ttf'
FONT_FILE2 = 'PixelOperator-Bold.ttf'

MENU_MUSIC = 'hot_spring_town.ogg'

MENU_BG= 'start_menu.png' 
LEVEL1_BG ='level_1.png' 
LEVEL2_BG = 'level_2.png'
LEVEL3_BG = 'level_3.png'

END_BG = 'end_menu.png'

PLAYER_IMG = 'player.png'

START_NORMAL = 'button.png'
START_HOVER = 'button_hover.png'

QUIT_NORMAL = 'button.png'
QUIT_HOVER = 'button_hover.png'

player_img = pygame.image.load(resource_path(PLAYER_IMG)).convert_alpha()
player_img = pygame.transform.scale(player_img, (100, 100))

menu_bg = pygame.image.load(resource_path(MENU_BG)).convert()
menu_bg = pygame.transform.scale(menu_bg, (WIDTH, HEIGHT))

end_bg = pygame.image.load(resource_path(END_BG)).convert()
level1_bg = pygame.image.load(resource_path(LEVEL1_BG)).convert()
level2_bg = pygame.image.load(resource_path(LEVEL2_BG)).convert()
level3_bg = pygame.image.load(resource_path(LEVEL3_BG)).convert()

start_normal = pygame.image.load(resource_path(START_NORMAL)).convert_alpha()
start_hover = pygame.image.load(resource_path(START_HOVER)).convert_alpha()

quit_normal = pygame.image.load(resource_path(QUIT_NORMAL)).convert_alpha()
quit_hover = pygame.image.load(resource_path(QUIT_HOVER)).convert_alpha()

end_bg = pygame.transform.scale(end_bg, (WIDTH, HEIGHT))
level1_bg = pygame.transform.scale(level1_bg, (WIDTH, HEIGHT))
level2_bg = pygame.transform.scale(level2_bg, (WIDTH, HEIGHT))
level3_bg = pygame.transform.scale(level3_bg, (WIDTH, HEIGHT))

TITLE_FONT = pygame.font.Font(resource_path(FONT_FILE), 72)
MENU_FONT = pygame.font.Font(resource_path(FONT_FILE), 36)
GAME_FONT = pygame.font.Font(resource_path(FONT_FILE), 30)
NUMBER_FONT= pygame.font.Font(resource_path(FONT_FILE), 42)

start_button = pygame.Rect(275,250,250,70)
quit_button = pygame.Rect(275,340,250,70)

WHITE = '#1D2128'
BLACK = '#000000'
GREEN = '#558467'
BLUE = '#215E61'
BLUE_1='#458393'
PINK ='#E22F80'
PURPLE='#792CA2'


clock = pygame.time.Clock()
FPS = 60

player_width = 100
player_height = 100

player_x=WIDTH//2 - player_width//2
player_y=HEIGHT - player_height - 40

player_speed = 6

object_width = 30
object_height = 30

object_x = random.randint(0, WIDTH - object_width)
object_y = random.randint(-150,-30)

new_range=random.randint(10,100)
current_number = random.randint(1, new_range)

object_speed = 5

score=0

WIN_SCORE= 10

async def menu():

    while True:
        screen.blit(menu_bg,(0,0))

        title = TITLE_FONT.render("The Number Festival", True, BLUE)
        screen.blit(title,title.get_rect(center=(WIDTH//2,120)))

        mouse = pygame.mouse.get_pos()

        if start_button.collidepoint(mouse):
            screen.blit(start_hover,start_button)
        else:
            screen.blit(start_normal,start_button)

        if quit_button.collidepoint(mouse):
            screen.blit(quit_hover,quit_button)

        else:
            screen.blit(quit_normal,quit_button)    

        start_text = MENU_FONT.render('START',True,WHITE)
        quit_text = MENU_FONT.render('QUIT',True,WHITE)

        screen.blit(start_text,start_text.get_rect(center=start_button.center))
        screen.blit(quit_text,quit_text.get_rect(center=quit_button.center))

        for event in pygame.event.get():
            handle_music_end(event)
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                 if start_button.collidepoint(event.pos):
                     play_music()
                     return True
                 if quit_button.collidepoint(event.pos):
                     return False
        pygame.display.flip()
        clock.tick(FPS)
        await asyncio.sleep(0)

async def level1():
    global player_x
    global object_x
    global object_y
    global object_speed
    global current_number
    global score
    global player_y
    score = 0
    player_x = WIDTH//2 - player_width//2
    player_y = HEIGHT - player_height - 40
    object_x = random.randint(0, WIDTH-object_width)
    object_y = random.randint(-150,-30)
    current_number = random.randint(1,new_range)

    waiting=True

    while waiting:
        screen.blit(level1_bg,(0,0))

        story=GAME_FONT.render('The Number Festival is on the way!.', True,(40,90,40))
        screen.blit(story, story.get_rect(center=(WIDTH//2,100)))

        story1=GAME_FONT.render('Fill the garden with numbers for the festival!.', True,(40,90,40))
        screen.blit(story1, story1.get_rect(center=(WIDTH//2,150)))

        level_text=GAME_FONT.render('LEVEL 1.', True,PINK)
        screen.blit(level_text, level_text.get_rect(center=(WIDTH//2,200)))

        info1=GAME_FONT.render('Collect only EVEN numbers to fill the garden!', True,BLACK)
        screen.blit(info1, info1.get_rect(center=(WIDTH//2,250)))

        info2=GAME_FONT.render(f'Reach {WIN_SCORE} points to complete the level!',True,BLACK)
        screen.blit(info2, info2.get_rect(center=(WIDTH//2,300)))

        info3=GAME_FONT.render('Press SPACE to start the level!',True,BLACK)
        screen.blit(info3, info3.get_rect(center=(WIDTH//2,400)))

        for event in pygame.event.get():
            handle_music_end(event)
            if event.type == pygame.QUIT:
                
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting=False
        pygame.display.flip()
        clock.tick(FPS)
        await asyncio.sleep(0)

    running=True
    while running:
        screen.blit(level1_bg,(0,0))
        for event in pygame.event.get():
            handle_music_end(event)
            if event.type == pygame.QUIT:
                
                return

        keys= pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and player_x>0:
            player_x -= player_speed

        if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
            player_x +=player_speed

        object_y += object_speed

        if (object_y + object_height > player_y
            and object_x + object_width>player_x
            and object_x <player_x + player_width
            ):

            if current_number %2 == 0:
                score +=1

            object_y = random.randint(-150,-30)
            object_x = random.randint(0,WIDTH - object_width)
            current_number = random.randint(1,new_range)

        if object_y >HEIGHT :
            object_y=random.randint(-150,-30)
            object_x =random.randint(0,WIDTH - object_width)
            current_number = random.randint(1,new_range)

        screen.blit(player_img,(player_x,player_y))

        number_text=NUMBER_FONT.render(str(current_number),True,PINK)
        screen.blit(number_text,(object_x,object_y))

        score_text = GAME_FONT.render(f'Score: {score}',True,WHITE)
        screen.blit(score_text,(20,20))

        pygame.display.flip()
        clock.tick(FPS)
        await asyncio.sleep(0)

        if score>=WIN_SCORE:
            running=False
    return
        


async def level2():
    global player_x
    global object_x
    global object_y
    global object_speed
    global current_number
    global score
    global player_y
    score=0
    player_x=WIDTH//2 - player_width//2
    player_y=HEIGHT - player_height - 40
    object_x = random.randint(0, WIDTH - object_width)
    object_y = random.randint(-150,-30)
    current_number = random.randint(1, new_range)

    waiting=True

    while waiting:
        screen.blit(level2_bg,(0,0))

        story=GAME_FONT.render('LEVEL 2', True,BLUE_1)
        screen.blit(story, story.get_rect(center=(WIDTH//2,100)))

        info1=GAME_FONT.render('Collect only ODD numbers to fill the garden!', True,BLACK)
        screen.blit(info1, info1.get_rect(center=(WIDTH//2,250)))

        info2=GAME_FONT.render(f'Reach {WIN_SCORE} points to complete the level!',True,BLACK)
        screen.blit(info2, info2.get_rect(center=(WIDTH//2,300)))

        info3=GAME_FONT.render('Press SPACE to start the level!',True,BLACK)
        screen.blit(info3, info3.get_rect(center=(WIDTH//2,400)))

        for event in pygame.event.get():
            handle_music_end(event)
            if event.type == pygame.QUIT:
                
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting=False
        pygame.display.flip()
        clock.tick(FPS)
        await asyncio.sleep(0)

    running=True
    while running:        
        screen.blit(level2_bg,(0,0))
        for event in pygame.event.get():
            handle_music_end(event)
            if event.type == pygame.QUIT:
                
                return
        keys= pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and player_x>0:
            player_x -= player_speed

        if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
            player_x +=player_speed

        object_y += object_speed

        if (object_y + object_height > player_y
            and object_x + object_width>player_x
            and object_x <player_x + player_width
            ):

            if current_number %2 != 0:
                score +=1

            object_y = random.randint(-150,-30)
            object_x = random.randint(0,WIDTH - object_width)
            current_number = random.randint(1,new_range)

        if object_y >HEIGHT :
            object_y=random.randint(-150,-30)
            object_x =random.randint(0,WIDTH - object_width)
            current_number = random.randint(1,new_range)

        screen.blit(player_img,(player_x,player_y))

        number_text=NUMBER_FONT.render(str(current_number),True,BLUE_1)
        screen.blit(number_text,(object_x,object_y))

        score_text = GAME_FONT.render(f'Score: {score}',True,WHITE)
        screen.blit(score_text,(20,20))

        pygame.display.flip()
        clock.tick(FPS)
        await asyncio.sleep(0)

        if score>=WIN_SCORE:
            running=False
    return
        

async def level3():
    global player_x
    global object_x
    global object_y
    global object_speed
    global current_number
    global score
    global player_y
    score=0
    player_x=WIDTH//2 - player_width//2
    player_y=HEIGHT - player_height - 40
    object_x = random.randint(0, WIDTH - object_width)
    object_y = random.randint(-150,-30)
    current_number = random.randint(1, new_range)

    waiting= True

    while waiting:
        screen.blit(level3_bg,(0,0))

        story=GAME_FONT.render('LEVEL 3', True,PURPLE)
        screen.blit(story, story.get_rect(center=(WIDTH//2,100)))

        info1=GAME_FONT.render('Collect only PRIME numbers to fill the garden!', True,BLACK)
        screen.blit(info1, info1.get_rect(center=(WIDTH//2,250)))

        info2=GAME_FONT.render(f'Reach {WIN_SCORE} points to complete the level!',True,BLACK)
        screen.blit(info2, info2.get_rect(center=(WIDTH//2,300)))

        info3=GAME_FONT.render('Press SPACE to start the level!',True,BLACK)
        screen.blit(info3, info3.get_rect(center=(WIDTH//2,400)))

        for event in pygame.event.get():
            handle_music_end(event)
            if event.type == pygame.QUIT:
                
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    
                    waiting=False
        pygame.display.flip()
        clock.tick(FPS)
        await asyncio.sleep(0)

    running=True
    while running:
        screen.blit(level3_bg,(0,0))
        for event in pygame.event.get():
            handle_music_end(event)
            if event.type == pygame.QUIT:
                
                return
        keys= pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and player_x>0:
            player_x -= player_speed

        if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
            player_x +=player_speed

        object_y += object_speed

        if (object_y + object_height > player_y
            and object_x + object_width>player_x
            and object_x <player_x + player_width
            ):
            is_prime = current_number > 1
            for i in range(2, int(current_number ** 0.5) + 1):
                if current_number % i == 0:
                    is_prime = False
                    break
            if is_prime:
                score +=1
            

            object_y = random.randint(-150,-30)
            object_x = random.randint(0,WIDTH - object_width)
            current_number = random.randint(1,new_range)

        if object_y >HEIGHT :
            object_y=random.randint(-150,-30)
            object_x =random.randint(0,WIDTH - object_width)
            current_number = random.randint(1,new_range)

        screen.blit(player_img,(player_x,player_y))

        number_text=NUMBER_FONT.render(str(current_number),True,PURPLE)
        screen.blit(number_text,(object_x,object_y))

        score_text = GAME_FONT.render(f'Score: {score}',True,WHITE)
        screen.blit(score_text,(20,20))

        pygame.display.flip()
        clock.tick(FPS)
        await asyncio.sleep(0)

        if score>=WIN_SCORE:
            running=False
    return
        

async def main():
    global player_x
    global object_x
    global object_y
    global object_speed
    global current_number
    global score

    while True:
        await level1()
        await level2()
        await level3()

        play_music()

        screen.blit(end_bg,(0,0))

        title=GAME_FONT.render('YOU WON!',True,WHITE)
        screen.blit(title,title.get_rect(center=(WIDTH//2,180)))

        subtitle=GAME_FONT.render('Press ENTER to play again',True,WHITE)
        screen.blit(subtitle,subtitle.get_rect(center=(WIDTH//2,240)))

        quit_text=GAME_FONT.render('Press ESC or Q to quit',True,WHITE)
        screen.blit(quit_text,quit_text.get_rect(center=(WIDTH//2,270)))

        story_text = GAME_FONT.render('Congratulations! You have completed all the levels.',True, WHITE)
        screen.blit(story_text,story_text.get_rect(center=(WIDTH //2,320)))

        story2 = GAME_FONT.render('The garden is now complete!',True,WHITE)
        screen.blit(story2,story2.get_rect(center=(WIDTH//2,370)))

        credit=GAME_FONT.render('The beautiful music is by Kistol<3',True, WHITE)
        screen.blit(credit,credit.get_rect(center=(WIDTH //2 , 420)))

        pygame.display.flip()

        waiting_for_input = True
        while waiting_for_input:
            for event in pygame.event.get():
                handle_music_end(event)
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        waiting_for_input = False
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                        return
            pygame.display.flip()
            clock.tick(FPS)
            await asyncio.sleep(0)

async def game():
    pygame.mixer.music.set_volume(0.5)

    start_clicked = await menu()
    if start_clicked:
        await main()

    try:
        pygame.mixer.music.stop()
    except pygame.error:
        pass

    screen.fill(WHITE)
    bye_text = TITLE_FONT.render('Thanks for playing!', True, PINK)
    screen.blit(bye_text, bye_text.get_rect(center=(WIDTH//2, HEIGHT//2)))
    pygame.display.flip()


asyncio.run(game())

        
        

