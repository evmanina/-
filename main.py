import os
import sys

import pygame

# Елизавета Манина
pygame.init()

inJump = False
running = False
Moving_right = False
Moving_left = False
Jump_up = False
Jump_down = False
walking_on_right = [pygame.image.load("sprites/R_R1.png"), pygame.image.load("sprites/R_R2.png"),
                    pygame.image.load("sprites/R_R3.png"), pygame.image.load("sprites/R_R4.png")]
walking_on_left = [pygame.image.load("sprites/R_L1.png"), pygame.image.load("sprites/R_L2.png"),
                   pygame.image.load("sprites/R_L3.png"), pygame.image.load("sprites/R_L4.png")]
hero_stand = pygame.image.load('sprites/Stand.png')
hero_jump_up = pygame.image.load("sprites/J_UL.png")
hero_jump_down = pygame.image.load("sprites/J_DL.png")
hero_jump_up_right = pygame.image.load("sprites/J_UR.png")
hero_jump_down_right = pygame.image.load("sprites/J_DR.png")

fon1 = pygame.image.load('sprites/start_screen_bg.jpg')

game_over_bg = pygame.image.load("sprites/game_over_screen.jpg")

all_sprites = pygame.sprite.Group()
hero = pygame.sprite.Sprite(all_sprites)
hero.image = hero_stand
hero.rect = hero.image.get_rect()

ground = pygame.sprite.Sprite(all_sprites)
ground.image = pygame.image.load('data/ground.png')
ground.rect = ground.image.get_rect()

wall1 = pygame.sprite.Sprite(all_sprites)
wall1.image = pygame.image.load('data/wall1.png')
wall1.rect = ground.image.get_rect()

wall2 = pygame.sprite.Sprite(all_sprites)
wall2.image = pygame.image.load('data/wall2.png')
wall2.rect = ground.image.get_rect()

wall3 = pygame.sprite.Sprite(all_sprites)
wall3.image = pygame.image.load('data/wall3.png')
wall3.rect = ground.image.get_rect()


def start_game():
    """
    данная функция задает изначальное положение героя, вводит переменные и константы и включает музыку
    global running - отвечает за состояние героя - бежит он или нет (тип bool)
    global wallspeed - скорость изменения заднего фона
    global i - счетчик
    global slower - коэффициент замедления скорости
    global grdelta -  скорость перемещения персонажа
    global wallstart - задний фон 1
    global wallstart2 - задний фон 2
    global animation - отвечает за анимацию
    global score - очки
    global gravity - высота прыжка
    global delta - скорость
    global fps - количество сменяемых кадров

    """
    global running
    global wallspeed
    global i
    global slower
    global grdelta
    global wallstart
    global wallstart2
    global animation
    global score
    global gravity
    global delta
    global fps
    running = True
    wallspeed = 20
    i = 1
    slower = 0.5
    grdelta = 20
    wallstart = 2000
    wallstart2 = 1800
    animation = 0
    score = 0
    gravity = 9
    delta = 10
    fps = 16
    hero.rect.bottomright = 200, 535
    ground.rect.bottomleft = -50, 485
    wall1.rect.bottomleft = wallstart, 375
    wall2.rect.bottomleft = wallstart2, 425
    wall3.rect.bottomleft = 12900, 275
    pygame.mixer.music.stop()
    pygame.mixer.music.load("music/bg_music.mp3")
    pygame.mixer.music.set_volume(0.01)
    pygame.mixer.music.play(-1)


# Азалия Хабибуллина
def print_text(message, x, y, color=(198, 207, 207), letter_type="sprites/shrift.ttf", letter_size=30):
    """
      данная функция создает текст для стартовой страницы
    :param message:сам текст
    :param x: координата "message"
    :param y: координата "message"
    :param color: цвет текста
    :param letter_type: стиль текста
    :param letter_size: размер символов
    """
    letter_type = pygame.font.Font(letter_type, letter_size)
    text = letter_type.render(message, True, color)
    screen.blit(text, (x, y))


def start_screen():
    """
     данная функция импортирует текст из функции "print_text" и форматирует его. запускает музыку, начинает игру.
    """
    fon = pygame.transform.scale(fon1, (1000, 600))
    screen.blit(fon, (0, 0))
    print_text('Controlling the character:', 100, 50)
    print_text('A - left', 100, 100)
    print_text('D - right', 100, 150)
    print_text('SPACE - jump', 100, 200)
    print_text('Press mouse button to start', 370, 510, letter_size=20)
    pygame.mixer.music.load("music/strat_screen_music_bg.mp3")
    pygame.mixer.music.set_volume(0.01)
    pygame.mixer.music.play(-1)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                start_game()
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(fps)


# Елизавета Манина
def draw():
    """
    данная функция задает переменные для самого процесса игры, анимацию, музыку. регламентирует длину прыжков и описывает
    положение персонажа в пространтсве.
    пояснение к глобальным переменным представлен выше в ф-ии "start_game"
    """
    global wallspeed, wallstart, grdelta, wallstart2
    global animation
    global i
    global slower
    if i + 1 >= 340:
        i = 1
    if 230 < i < 330:
        slower = 1
    else:
        slower = 0.5
    bg = pygame.image.load(f'captures/{int(i // 1)}.png')
    screen.blit(bg, (0, 0))
    i += slower

    if ground.rect.right < 1000:
        ground.rect.left = -50
    screen.blit(ground.image, (ground.rect.left, ground.rect.bottom))
    ground.rect.left -= grdelta

    if wall1.rect.left < -300:
        wall1.rect.left = wallstart
    if wall2.rect.left < -300:
        wall2.rect.left = wallstart2
    grdelta, wallspeed = change_speed(score, grdelta, wallspeed)

    screen.blit(wall1.image, (wall1.rect.left, wall1.rect.bottom))
    screen.blit(wall2.image, (wall2.rect.left, wall2.rect.bottom))
    screen.blit(wall3.image, (wall3.rect.left, wall3.rect.bottom))
    wall1.rect.left -= wallspeed
    wallstart = 1300
    wall2.rect.left -= wallspeed
    wallstart2 = 1200
    wall3.rect.left -= wallspeed

    if animation + 1 >= 16:
        animation = 0
    if Moving_left and not Jump_up and not Jump_down:
        screen.blit(walking_on_left[animation // 4], (hero.rect.left, hero.rect.top))
        animation += 1
    elif Moving_right and not Jump_up and not Jump_down:
        screen.blit(walking_on_right[animation // 4], (hero.rect.left, hero.rect.top))
        animation += 1
    elif Moving_left and Jump_up and not Jump_down:
        screen.blit(hero_jump_up, (hero.rect.left, hero.rect.top))
    elif Moving_left and not Jump_up and Jump_down:
        screen.blit(hero_jump_down, (hero.rect.left, hero.rect.top))
    elif Moving_right and Jump_up and not Jump_down:
        screen.blit(hero_jump_up_right, (hero.rect.left, hero.rect.top))
    elif Moving_right and not Jump_up and Jump_down:
        screen.blit(hero_jump_down_right, (hero.rect.left, hero.rect.top))
    elif Jump_up:
        screen.blit(hero_jump_up_right, (hero.rect.left, hero.rect.top))
    elif Jump_down:
        screen.blit(hero_jump_down_right, (hero.rect.left, hero.rect.top))
    else:
        screen.blit(walking_on_right[animation // 4], (hero.rect.left, hero.rect.top))
        animation += 1
    print_text("Score:" + str(score), 560, 20)
    pygame.display.flip()


# Азалия Хабибуллина
def lose_game():
    """
    данная функция отвечает за "проигрыш". Т.е окно возобновления игры
    аналогично пояснение к глобальным переменным представлен выше в ф-ии "start_game"

    """
    global running
    running = False
    losing = True
    while losing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.mixer.music.stop()
        g_o_sc = pygame.transform.scale(game_over_bg, (784, 544))
        screen.blit(g_o_sc, (0, 0))
        print_text("Press 'R' to restart the game", 120, 470)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_r]:
            start_game()
            losing = False
        pygame.display.flip()
        clock.tick(20)


def check_lose():
    """
    данная функция проверяет проиграл ли герой
    """
    if (wall1.rect.left + 75 < hero.rect.right < wall1.rect.left + 170 and hero.rect.bottom > 445) or \
            (wall2.rect.left + 75 < hero.rect.right < wall2.rect.left + 160 and hero.rect.bottom > 470) or \
            (wall3.rect.left + 100 < hero.rect.right < wall3.rect.left + 210 and hero.rect.bottom > 345):
        return True
    return False


# Елизавета Манина
def change_speed(score, grdelta, wallspeed):
    """
функция отвечает за изменение скорости
    :param score - очки
    :param grdelta - скорость персонажа
    :param wallspeed - скорость изменения заднего фона
    """
    if score > 400:
        wallspeed = 30
        grdelta = 30
    if score > 700:
        wallspeed = 40
        grdelta = 40
    if score > 1000:
        wallspeed = 45
        grdelta = 45
    if score > 1100:
        wallspeed = 50
        grdelta = 50
    return grdelta, wallspeed


if __name__ == '__main__':
    size = width, height = 784, 544
    pygame.display.set_caption("Revolver")
    screen = pygame.display.set_mode(size)
    fps = 16

    clock = pygame.time.Clock()
    start_screen()

    running = True

    while running:
        clock.tick(fps)
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if keys[pygame.K_a] and hero.rect.left > 0:
                hero.rect.left -= delta
                Moving_left = True
                Moving_right = False
            elif keys[pygame.K_d] and hero.rect.right < 780:
                hero.rect.left += delta
                Moving_left = False
                Moving_right = True
            else:
                Moving_left = False
                Moving_right = False
                animation = 0
            if not inJump:
                if keys[pygame.K_SPACE]:
                    inJump = True
                    Jump_up = True

        # заимствованная часть кода, идея взята с интернет ресурсов:
        # https://www.cyberforum.ru/python-graphics/thread2343538.html
        # https://www.programmersforum.rocks/t/kak-sdelat-pryzhok-na-pygame/1260
        # https://pythonspot.com/jump-and-run-in-pygame/

        if inJump:
            if gravity >= -9:
                if gravity == -9:
                    hero.rect.top += ((gravity + 5) ** 2)
                if gravity < 0:
                    hero.rect.top += (gravity ** 2)
                    Jump_up = False
                    Jump_down = True
                else:
                    hero.rect.top -= (gravity ** 2)
                gravity -= 1
            else:
                inJump = False
                gravity = 9
                Jump_up = False
                Jump_down = False
        # заимствованная часть кода закончилась
        if hero.rect.bottom > 535:
            hero.rect.bottom = 535
        if check_lose():
            lose_game()

        draw()
        score += 1
    pygame.quit()