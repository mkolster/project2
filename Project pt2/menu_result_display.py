import pygame

import control_fires
import user_fires_logic
import sys
from pygame import mixer

import place_ships

pygame.init()
mixer.init()
clock = pygame.time.Clock()
mixer.music.load('epic-action-113888.mp3')
mixer.music.set_volume(0.2)


def welcome_screen():
    mixer.music.play()
    color = 'white'
    position = (0,0)

    input_text = ''
    input_rect = pygame.Rect(300 // 2, 425, 200, 35)
    input_rect.center = (500 // 2, 900//2)
    active = False
    text_font = pygame.font.Font(None, 32)


    screen = pygame.display.set_mode((500, 500))

    pygame.display.set_caption('Menu')

    image = pygame.image.load('battleship3.jpg')
    image = pygame.transform.scale(image, (500,500))

    font = pygame.font.Font('freesansbold.ttf', 65)
    text = font.render('BATTLESHIP', True, 'white', (55, 55, 55))
    text_rect = text.get_rect()
    text_rect.center = (500 // 2, 100 // 2)



    font2 = pygame.font.Font('freesansbold.ttf', 35)
    # text2 = font2.render(' player name', True, 'black', 'gray')
    # text2_rect = text2.get_rect()
    # text2_rect.center = (500 // 2, 600 // 2)

    text3 = font2.render('Press ENTER to begin',True, 'white')
    text3_rect = text3.get_rect()
    text3_rect.center = (500//2, 750//2)

    font3 = pygame.font.Font('freesansbold.ttf', 20)
    text_username = font3.render('Player Name:', True, 'black','gray')
    text_username_rect = text_username.get_rect()
    text_username_rect.center = (500 // 2, 825//2)

    quitter = False
    letter_count = 0
    while not quitter:
        screen.fill('black')
        screen.blit(image, (0,0))
        screen.blit(text, text_rect)
        # screen.blit(text2, text2_rect)
        screen.blit(text3, text3_rect)
        screen.blit(text_username, text_username_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mixer.music.stop()
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    mixer.music.stop()
                    control_fires.gridsquare(input_text)
                if active:
                    if event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                        letter_count -= 1
                    elif letter_count <= 12 and event.key != pygame.KMOD_SHIFT:
                        input_text += event.unicode
                        letter_count += 1


            elif event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False

        if active:
            color = (255, 255, 255)
        else:
            color = (200, 200, 200)

        pygame.draw.rect(screen, color, input_rect)
        text_surface = text_font.render(input_text, True, 'black')
        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
        # input_rect.w = max(200, text_surface.get_width() + 20)

        pygame.display.flip()
        clock.tick(60)

        pygame.display.update()


def ending_screen(value, player_name, outcome):
    mixer.music.play()
    color = 'white'
    position = (0, 0)

    screen = pygame.display.set_mode((500, 500))

    pygame.display.set_caption('Game Over')

    image = pygame.image.load('battleship3.jpg')
    image = pygame.transform.scale(image, (500, 500))

    font = pygame.font.Font('freesansbold.ttf', 35)
    text = font.render(f'Patrol boat: {value[0]} hits {value[5][0]}', True, 'black', 'gray')
    text_rect = text.get_rect()
    text_rect.center = (500 // 2, 100 // 2)

    font = pygame.font.Font('freesansbold.ttf', 35)
    text1 = font.render(f'Submarine: {value[1]} hits {value[5][1]}', True, 'black', 'gray')
    text1_rect = text1.get_rect()
    text1_rect.center = (500 // 2, 200 // 2)

    font = pygame.font.Font('freesansbold.ttf', 35)
    text2 = font.render(f'Destroyer: {value[2]} hits {value[5][2]}', True, 'black', 'gray')
    text2_rect = text2.get_rect()
    text2_rect.center = (500 // 2, 300 // 2)

    font = pygame.font.Font('freesansbold.ttf', 35)
    text3 = font.render(f'Battleship: {value[3]} hits {value[5][3]}', True, 'black', 'gray')
    text3_rect = text3.get_rect()
    text3_rect.center = (500 // 2, 400 // 2)

    font = pygame.font.Font('freesansbold.ttf', 35)
    text4 = font.render(f'Carrier: {value[4]} hits {value[5][4]}', True, 'black', 'gray')
    text4_rect = text4.get_rect()
    text4_rect.center = (500 // 2, 500 // 2)

    font = pygame.font.Font('freesansbold.ttf', 35)
    text5 = font.render(f'{player_name} you {outcome}!', True, 'black', 'gray')
    text5_rect = text5.get_rect()
    text5_rect.center = (500 // 2, 600 // 2)

    quitter = False

    while not quitter:
        screen.fill('black')
        screen.blit(image, (0, 0))
        screen.blit(text, text_rect)
        screen.blit(text1, text1_rect)
        screen.blit(text2, text2_rect)
        screen.blit(text3, text3_rect)
        screen.blit(text4, text4_rect)
        screen.blit(text5, text5_rect)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mixer.music.stop()
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mixer.music.stop()
                quitter = True

        pygame.display.update()

