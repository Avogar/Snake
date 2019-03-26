import pygame, random, os, sys
pygame.init()

def draw_snake():
    for i in range(len(x)-1, -1,-1):
        if i == 0:
            if dx[i] == a:
                screen.blit(snake_head_right,[x[i],y[i]-1])
            elif dx[i] == -a:
                screen.blit(snake_head_left, [x[i], y[i]-1])
            elif dy[i] == a:
                screen.blit(snake_head_down, [x[i]-1, y[i]])
            elif dy[i] == -a:
                screen.blit(snake_head_up, [x[i]-1, y[i]])
        elif i == len(x) - 1:
            if dx[i-1] == a:
                screen.blit(snake_tail_right,[x[i],y[i]])
            elif dx[i-1] == -a:
                screen.blit(snake_tail_left, [x[i], y[i]])
            elif dy[i-1] == a:
                screen.blit(snake_tail_down, [x[i], y[i]])
            elif dy[i-1] == -a:
                screen.blit(snake_tail_up, [x[i], y[i]])
        else:
            if angle[i][0] == 1:
                screen.blit(snake_body_upleft, [x[i], y[i]])
            elif angle[i][1] == 1:
                screen.blit(snake_body_upright, [x[i], y[i]])
            elif angle[i][2] == 1:
                screen.blit(snake_body_downleft, [x[i], y[i]])
            elif angle[i][3] == 1:
                screen.blit(snake_body_downright, [x[i], y[i]])
            else:
                if dx[i] != 0:
                    screen.blit(snake_body_h,[x[i],y[i]])
                elif dy[i] != 0:
                    screen.blit(snake_body_v,[x[i],y[i]])


def shortening():
    for i in range(2,len(x)-1):
        if x[0] == x[i] and y[0] == y[i]:
            k = len(x)
            for j in range(i,k):
                x.pop()
                y.pop()
                dx.pop()
                dy.pop()
                angle.pop()
                snake_portal.pop()
            break

def borders():
    for i in range(len(x)):
        if x[i] >= size[0]:
            x[i] = 0
        if x[i] <= -a:
            x[i] = size[0] - a
        if y[i] >= size[0]:
            y[i] = 0
        if y[i] <= -a:
            y[i] = size[0] - a

def teleport():
    portal_open = []
    portal = []
    portal_open = open_portal(portal_open)
    for line in portal_open:
        list = line.split()
        for i in range(len(list)):
            list[i] = int(list[i])
        portal.append(list)
    if portal != []:
        for i in range(len(x)):
            for j in range(len(portal)):
                if j % 2 == 0:
                    xp = portal[j+1][0]
                    yp = portal[j+1][1]
                else:
                    xp = portal[j-1][0]
                    yp = portal[j-1][1]
                if x[i] == portal[j][0] and y[i] == portal[j][1] and snake_portal[i] == [0]:
                    x[i] = xp
                    y[i] = yp
                    snake_portal[i] = [1,j]
                else:
                    if snake_portal[i] == [1,j]:
                        snake_portal[i] = [0]
                        for j in range(len(portal)):
                            if j % 2 == 0:
                                xp = portal[j + 1][0]
                                yp = portal[j + 1][1]
                            else:
                                xp = portal[j - 1][0]
                                yp = portal[j - 1][1]
                            if x[i] == portal[j][0] and y[i] == portal[j][1] and snake_portal[i] == [0]:
                                x[i] = xp
                                y[i] = yp
                                snake_portal[i] = [1, j]
    if portal_open != []: portal_open.close()

def move():
    for i in range(len(down)-1,-1,-1):
        if down[i] >= len(x):
            down.pop(i)

    for i in range(len(down)):
        angle[down[i]][2] = angle[down[i]][3] = 0
        if down[i] + 1 < len(x):
            if dx[down[i]] == a:
                angle[down[i]+1][2] = 1
            elif dx[down[i]] == -a:
                angle[down[i]+1][3] = 1
        dx[down[i]] = 0
        dy[down[i]] = a
        down[i] += 1

    for i in range(len(up)-1,-1,-1):
        if up[i] >= len(x):
            up.pop(i)

    for i in range(len(up)):
        angle[up[i]][0] = angle[up[i]][1] = 0
        if up[i] + 1 < len(x):
            if dx[up[i]] == a:
                angle[up[i]+1][0] = 1
            elif dx[up[i]] == -a:
                angle[up[i]+1][1] = 1
        dx[up[i]] = 0
        dy[up[i]] = -a
        up[i] += 1

    for i in range(len(right)-1,-1,-1):
        if right[i] >= len(x):
            right.pop(i)

    for i in range(len(right)):
        angle[right[i]][1] = angle[right[i]][3] = 0
        if right[i] + 1 < len(x):
            if dy[right[i]] == a:
                angle[right[i]+1][1] = 1
            elif dy[right[i]] == -a:
                angle[right[i]+1][3] = 1
        dx[right[i]] = a
        dy[right[i]] = 0
        right[i] += 1

    for i in range(len(left)-1,-1,-1):
        if left[i] >= len(x):
            left.pop(i)

    for i in range(len(left)):
        angle[left[i]][0] = angle[left[i]][2] = 0
        if left[i] + 1 < len(x):
            if dy[left[i]] == a:
                angle[left[i]+1][0] = 1
            elif dy[left[i]] == -a:
                angle[left[i]+1][2] = 1
        dx[left[i]] = -a
        dy[left[i]] = 0
        left[i] += 1

    for i in range(len(x)):
        x[i] += dx[i]
        y[i] += dy[i]

def eating(eatxy, e, event):
    if x[0] == eatxy[0] and y[0] == eatxy[1]:
        if dx[len(x)-1] == a:
            x.append(x[len(x)-1] - a)
            y.append(y[len(y)-1])
            dx.append(a)
            dy.append(0)
        elif dx[len(x)-1] == -a:
            x.append(x[len(x)-1] + a)
            y.append(y[len(y)-1])
            dx.append(-a)
            dy.append(0)
        elif dy[len(x)-1] == a:
            x.append(x[len(x)-1])
            y.append(y[len(y)-1] - a)
            dx.append(0)
            dy.append(a)
        elif dy[len(x)-1] == -a:
            x.append(x[len(x)-1])
            y.append(y[len(y)-1] + a)
            dx.append(0)
            dy.append(-a)
        snake_portal.append(snake_portal[len(x)-2])
        angle.append([0, 0, 0, 0])
        eatxy = eat_location(eatxy)
        e = random.randint(0, 9)
        event = 1
    return eatxy, e, event

def boom(bomb,life,event):
    if x[0] == bomb[0] and y[0] == bomb[1]:
        life -= 1
        bomb = eat_location(bomb)
        event = 1
    return bomb, life, event


def eat_location(eatxy):
    lvl_open = []
    portal_open = []
    portal = []
    portal_open = open_portal(portal_open)
    for line in portal_open:
        list = line.split()
        for i in range(len(list)):
            list[i] = int(list[i])
        portal.append(list)
    eatxy = [int(a * random.randint(a, size[0] // a - 1 - a)), int(a * random.randint(a, size[0] // a - 1 - a))]
    for i in range(len(x)):
        if x[i] == eatxy[0] and y[i] == eatxy[1]:
            eatxy = eat_location(eatxy)
    for i in range(len(portal)):
        if eatxy[0] == portal[i][0] and eatxy[1] == portal[i][1]:
            eatxy = eat_location(eatxy)
    if lvl != 1:
        lvl_open = open_lvl(lvl_open)
        for line in lvl_open:
            list = line.split()
            for i in range(len(list)):
                list[i] = int(list[i])
            if len(list) == 4 and 0 <= eatxy[0] - list[0] < list[2] and 0 <= eatxy[1] - list[1] < list[3]:
                eatxy = eat_location(eatxy)
        lvl_open.close()
    if portal_open != []: portal_open.close()
    return eatxy

def prise_collect(prisexy):
    for i in range(len(prisexy)):
        if x[0] == prisexy[i][0] and y[0] == prisexy[i][1]:
            prisexy.pop(i)
            break
    return prisexy

def draw_pause():
    pygame.draw.rect(screen, cyan, [129, 124, 150, 130], 0)
    pygame.draw.rect(screen, black, [129, 124, 150, 130], 1)
    text = font.render('ПАУЗА', True, black)
    screen.blit(text, [174,138])

    pygame.draw.rect(screen, continue_color, continue_l, 0)
    pygame.draw.rect(screen, black, continue_l, 1)
    text = font.render('Продолжить', True, black)
    screen.blit(text, [continue_l[0] + 9, continue_l[1] + 8])

    pygame.draw.rect(screen, menu_color, menu_l, 0)
    pygame.draw.rect(screen, black, menu_l, 1)
    text = font.render('Меню', True, black)
    screen.blit(text, [menu_l[0] + 40, menu_l[1] + 9])

def draw_menu():
    pygame.draw.rect(screen,black,[0,0,size[0],size[1]],1)
    pygame.draw.rect(screen, begin_color,begin_l, 0)
    pygame.draw.rect(screen, black, begin_l, 1)
    text = font.render('Начать!', True, black)
    screen.blit(text, [begin_l[0]+22, begin_l[1]+10])
    text = font.render('Уровни:', True,black)
    screen.blit(text, [172, 274])
    pygame.draw.rect(screen, constructor_color, constructor, 0)
    pygame.draw.rect(screen, black, constructor, 1)
    text = font.render('Конструктор', True, black)
    screen.blit(text, [constructor[0] + 10, constructor[1] + 10])
    if count_lvl//(16*page) > 0:
        n = page*16
    else:
        n = count_lvl
    for i in range((page-1)*16, n):
        pygame.draw.rect(screen,lvl_color[i],lvl_l[i%16],0)
        pygame.draw.rect(screen,black,lvl_l[i%16],1)
        font1 = pygame.font.Font(None, 40)
        text = font1.render(str(i+1),True,black)
        ddx = 12
        if i >= 9:
            ddx = 5
        screen.blit(text, [lvl_l[i%16][0]+ddx, lvl_l[i%16][1]+7])
    arl = arr = 1
    if page == 1:
        arl = 0
    if page*16 >= count_lvl:
        arr = 0
    if arl == 1:
        pygame.draw.rect(screen, arrowl_color, arrow_left, 0)
        pygame.draw.rect(screen, black, arrow_left, 1)
        pygame.draw.rect(screen, black, [arrow_left[0] + 9, arrow_left[1] + 4, arrow_left[2] - 14, arrow_left[3] - 8], 0)
        pygame.draw.polygon(screen, black, [(arrow_left[0] + 4, arrow_left[1] + 6), (arrow_left[0] + 8, arrow_left[1] + 2), (arrow_left[0] + 8, arrow_left[1] + 10), 0])
    if arr == 1:
        pygame.draw.rect(screen, arrowr_color, arrow_right, 0)
        pygame.draw.rect(screen, black, arrow_right, 1)
        pygame.draw.rect(screen, black, [arrow_right[0] + 5, arrow_right[1] + 4, arrow_right[2] - 14, arrow_right[3] - 8], 0)
        pygame.draw.polygon(screen, black, [(arrow_right[0] + arrow_right[2] - 5, arrow_right[1] + 6), (arrow_right[0] + arrow_right[2] - 9, arrow_right[1] + 2), (arrow_right[0] + arrow_right[2] - 9, arrow_right[1] + 10), 0])


def draw_inf():
    pygame.draw.rect(screen,white,[0,408,408,20],0)
    pygame.draw.rect(screen,black,[0,408,408,20],1)
    font1 = pygame.font.Font(None,20)
    if lvl_type == 1:
        text = font1.render('Длина: ' + str(len(x)) + '/' + str(maxlen), True, black)
    elif lvl_type == 2:
        text = font1.render('Нужно пройти лабиринт.', True, black)
    elif lvl_type == 3:
        text = font1.render('Призов собрано: ' + str(count_prise - len(prisexy)) + '/' + str(count_prise), True, black)
    screen.blit(text, [2,411])
    text = font1.render(str(life), True, black)
    screen.blit(life_p,[391,411])
    if life >= 10:
        lifexy = [373, 411]
    else:
        lifexy = [380, 411]
    screen.blit(text,lifexy)


def draw_lvl():
    lvl_open = []
    lvl_open = open_lvl(lvl_open)
    for line in lvl_open:
        list = line.split()
        for i in range(len(list)):
            list[i] = int(list[i])
        if len(list) == 4:
            pygame.draw.rect(screen,black,list,0)
    if lvl_open != []:
        lvl_open.close()
    j = 0
    portal_open = []
    portal_open = open_portal(portal_open)
    for line in portal_open:
        list = line.split()
        for i in range(len(list)):
            list[i] = int(list[i])
        screen.blit(portal_image[int(j)], [list[0], list[1]])
        j += 0.5
    if portal_open != []: portal_open.close()

def draw_gameover():
    screen.fill(red)
    pygame.draw.rect(screen, black, [0, 0, size[0], size[1]], 1)
    font_go = pygame.font.Font(None,40)
    text = font_go.render('Вы проиграли!', True, black)
    screen.blit(text, [104, 104])

    pygame.draw.rect(screen, continue_color, [continue_l[0], continue_l[1], continue_l[2], continue_l[3]], 0)
    pygame.draw.rect(screen, black, [continue_l[0], continue_l[1], continue_l[2], continue_l[3]], 1)
    text = font.render('Заново', True, black)
    screen.blit(text, [continue_l[0] + 35, continue_l[1] + 8])

    pygame.draw.rect(screen, menu_color, [menu_l[0], menu_l[1], menu_l[2], menu_l[3]], 0)
    pygame.draw.rect(screen, black, [menu_l[0], menu_l[1], menu_l[2], menu_l[3]], 1)
    text = font.render('Меню', True, black)
    screen.blit(text, [menu_l[0] + 40, menu_l[1] + 9])

def draw_win():
    screen.fill(green)
    pygame.draw.rect(screen, black, [0, 0, size[0], size[1]], 1)
    font_go = pygame.font.Font(None, 40)
    text = font_go.render('Уровень пройден!', True, black)
    screen.blit(text, [80, 104])

    pygame.draw.rect(screen, menu_color, [menu_l[0], menu_l[1], menu_l[2], menu_l[3]], 0)
    pygame.draw.rect(screen, black, [menu_l[0], menu_l[1], menu_l[2], menu_l[3]], 1)
    text = font.render('Меню', True, black)
    screen.blit(text, [menu_l[0] + 40, menu_l[1] + 9])

def tupik():
    t = 0
    l = len(x)
    for c in range(3, l):
        x.pop()
        y.pop()
        dx.pop()
        dy.pop()
        angle.pop()
        snake_portal.pop()
    x.reverse()
    y.reverse()
    dx.reverse()
    dy.reverse()
    if snake_portal[1] != [0] or snake_portal[2] != 0:
        teleport()
        t = 1
    for q in range(3):
        dx[q] *= -1
        dy[q] *= -1
        angle[q] = [0, 0, 0, 0]
        snake_portal[q] = [0]
    dx[0] = dx[1]
    dy[0] = dy[1]
    if t == 1:
        teleport()

def snake_death(death):
    death = 0
    lvl_open = []
    lvl_open = open_lvl(lvl_open)
    for line in lvl_open:
        list = line.split()
        for i in range(len(list)):
            list[i] = int(list[i])
        if len(list) == 4 and 0 <= x[0] - list[0] < list[2] and 0 <= y[0] - list[1] < list[3]:
            if life != 1:
                if dx[0] == -a:
                    if angle[1] == [0,0,0,0]:
                        d1 = y[0]
                        d2 = size[0] - y[0] + 8
                        lvl_open2 = []
                        lvl_open2 = open_lvl(lvl_open2)
                        for line2 in lvl_open2:
                            list2 = line2.split()
                            for j in range(len(list2)):
                                list2[j] = int(list2[j])
                            if len(list2) == 4:
                                if list2[0] <= x[0] + a < list2[0] + list2[2]:
                                    if list2[1] >= y[0] and list2[1] - y[0] < d2:
                                        d2 = list2[1] - y[0]
                                    elif list2[1] + list2[3] <= y[0] and y[0] - list2[1] - list2[3] < d1:
                                        d1 =  y[0] - list2[1] - list2[3]
                        if d1 == 0 and d2 == 8:
                            tupik()
                            if left != []:
                                left.pop()
                            move()
                            death = snake_death(death)
                        elif d2 > d1:
                            x[0] += a
                            y[0] += a
                            dx[0] = 0
                            dy[0] = a
                            angle[1] = [0,0,0,1]
                            down.append(1)

                        else:
                            x[0] += a
                            y[0] -= a
                            dx[0] = 0
                            dy[0] = -a
                            angle[1] = [0,1,0,0]
                            up.append(1)

                    elif angle[1] == [1,0,0,0]:
                        x[0] += a
                        y[0] += a
                        dx[0] = 0
                        dy[0] = a
                        angle[1] = [0,0,0,0]
                        left.pop()
                        death = snake_death(death)
                    elif angle[1] == [0,0,1,0]:
                        x[0] += a
                        y[0] -= a
                        dx[0] = 0
                        dy[0] = -a
                        angle[1] = [0,0,0,0]
                        left.pop()
                        death = snake_death(death)
                elif dx[0] == a:
                    if angle[1] == [0,0,0,0]:
                        d1 = y[0]
                        d2 = size[0] - y[0] + 8
                        lvl_open2 = []
                        lvl_open2 = open_lvl(lvl_open2)
                        for line2 in lvl_open2:
                            list2 = line2.split()
                            for j in range(len(list2)):
                                list2[j] = int(list2[j])
                            if len(list2) == 4:
                                if list2[0] <= x[0] - a < list2[0] + list2[2]:
                                    if list2[1] >= y[0] and list2[1] - y[0] < d2:
                                        d2 = list2[1] - y[0]
                                    elif list2[1] + list2[3] <= y[0] and y[0] - list2[1] - list2[3] < d1:
                                        d1 = y[0] - list2[1] - list2[3]
                        if d1 == 0 and d2 == 8:
                            tupik()
                            if right != []:
                                right.pop()
                            move()
                            death = snake_death(death)
                        elif d2 > d1:
                            x[0] -= a
                            y[0] += a
                            dx[0] = 0
                            dy[0] = a
                            angle[1] = [0,0,1,0]
                            down.append(1)
                        else:
                            x[0] -= a
                            y[0] -= a
                            dx[0] = 0
                            dy[0] = -a
                            angle[1] = [1,0,0,0]
                            up.append(1)
                    elif angle[1] == [0,1,0,0]:
                        x[0] -= a
                        y[0] += a
                        dx[0] = 0
                        dy[0] = a
                        angle[1] = [0,0,0,0]
                        right.pop()
                        death = snake_death(death)
                    elif angle[1] == [0,0,0,1]:
                        x[0] -= a
                        y[0] -= a
                        dx[0] = 0
                        dy[0] = -a
                        angle[1] = [0,0,0,0]
                        right.pop()
                        death = snake_death(death)
                elif dy[0] == a:
                    if angle[1] == [0,0,0,0]:
                        d1 = x[0]
                        d2 = size[0] - x[0] + 8
                        lvl_open2 = []
                        lvl_open2 = open_lvl(lvl_open2)
                        for line2 in lvl_open2:
                            list2 = line2.split()
                            for j in range(len(list2)):
                                list2[j] = int(list2[j])
                            if len(list2) == 4:
                                if list2[1] <= y[0] - a < list2[1] + list2[3]:
                                    if list2[0] >= x[0] and list2[0] - x[0] < d2:
                                        d2 = list2[0] - x[0]
                                    elif list2[0] + list2[2] <= x[0] and x[0] - list2[0] - list2[2] < d1:
                                        d1 = x[0] - list2[0] - list2[2]
                        if d1 == 0 and d2 == 8:
                            tupik()
                            if down != []:
                                down.pop()
                            move()
                            death = snake_death(death)
                        elif d2 > d1:
                            x[0] += a
                            y[0] -= a
                            dx[0] = a
                            dy[0] = 0
                            angle[1] = [0,1,0,0]
                            right.append(1)
                        else:
                            x[0] -= a
                            y[0] -= a
                            dx[0] = -a
                            dy[0] = 0
                            angle[1] = [1,0,0,0]
                            left.append(1)
                    elif angle[1] == [0,0,0,1]:
                        x[0] -= a
                        y[0] -= a
                        dx[0] = -a
                        dy[0] = 0
                        angle[1] = [0,0,0,0]
                        down.pop()
                        death = snake_death(death)
                    elif angle[1] == [0,0,1,0]:
                        x[0] += a
                        y[0] -= a
                        dx[0] = a
                        dy[0] = 0
                        angle[1] = [0,0,0,0]
                        down.pop()
                        death = snake_death(death)
                elif dy[0] == -a:
                    if angle[1] == [0,0,0,0]:
                        d1 = x[0]
                        d2 = size[0] - x[0] + 8
                        lvl_open2 = []
                        lvl_open2 = open_lvl(lvl_open2)
                        for line2 in lvl_open2:
                            list2 = line2.split()
                            for j in range(len(list2)):
                                list2[j] = int(list2[j])
                            if len(list2) == 4:
                                if list2[1] <= y[0] + a < list2[1] + list2[3]:
                                    if list2[0] >= x[0] and list2[0] - x[0] < d2:
                                        d2 = list2[0] - x[0]
                                    elif list2[0] + list2[2] <= x[0] and x[0] - list2[0] - list2[2] < d1:
                                        d1 = x[0] - list2[0] - list2[2]
                        if d1 == 0 and d2 == 8:
                            tupik()
                            if up != []:
                                up.pop()
                            move()
                            death = snake_death(death)
                        elif d2 > d1:
                            x[0] += a
                            y[0] += a
                            dx[0] = a
                            dy[0] = 0
                            angle[1] = [0,0,0,1]
                            right.append(1)
                        else:
                            x[0] -= a
                            y[0] += a
                            dx[0] =  -a
                            dy[0] = 0
                            angle[1] = [0,0,1,0]
                            left.append(1)
                    elif angle[1] == [1,0,0,0]:
                        x[0] += a
                        y[0] += a
                        dx[0] = a
                        dy[0] = 0
                        angle[1] = [0,0,0,0]
                        up.pop()
                        death = snake_death(death)
                    elif angle[1] == [0,1,0,0]:
                        x[0] -= a
                        y[0] += a
                        dx[0] = -a
                        dy[0] = 0
                        angle[1] = [0, 0, 0, 0]
                        up.pop()
                        death = snake_death(death)
            death = 1
    if lvl_open != []: lvl_open.close()
    return death

def open_lvl(lvl_open):
    if lvl >= 2:
        lvl_open = open(trip + '/data/lvl/lvl' + str(lvl) + '.txt', 'r')
    return lvl_open

def open_portal(portal_open):
    if portal == 1:
        portal_open = open(trip + '/data/portal/portal' + str(lvl) + '.txt', 'r')
    return portal_open

def eat_check(eatxy,bomb,k):
    list = eatxy + bomb
    for i in range(len(list)):
        if (list[i][0] == list[k][0] or list[i][1] == list[k][1]) and i != k:
            list[k] = eat_location(list[k])
            list[k] = eat_check(list[0:len(eatxy)], bomb, k)
    return list[k]

black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)
yellow = (255,255,0)
cyan = (0,255,255)
grey = (150,150,150)
orange = (255,165,0)
brown = (139,69,19)
purple = (160,32,240)
Green2 = (180,255,140)
continue_color = menu_color = grey2 = begin_color = constructor_color =  (220,220,220)
size = [408,428]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()
font = pygame.font.Font(None,25)

done = True

trip = sys.path[0]

snake_head_right = pygame.image.load(trip + "/data/Image/Headright.png").convert()
snake_head_right.set_colorkey(white)

snake_head_left = pygame.image.load(trip + "/data/Image/Headleft.png").convert()
snake_head_left.set_colorkey(white)

snake_head_up = pygame.image.load(trip + "/data/Image/Headup.png").convert()
snake_head_up.set_colorkey(white)

snake_head_down = pygame.image.load(trip + "/data/Image/Headdown.png").convert()
snake_head_down.set_colorkey(white)

snake_tail_right = pygame.image.load(trip + "/data/Image/Tailright.png").convert()
snake_tail_right.set_colorkey(white)

snake_tail_left = pygame.image.load(trip + "/data/Image/Tailleft.png").convert()
snake_tail_left.set_colorkey(white)

snake_tail_up = pygame.image.load(trip + "/data/Image/Tailup.png").convert()
snake_tail_up.set_colorkey(white)

snake_tail_down = pygame.image.load(trip + "/data/Image/Taildown.png").convert()
snake_tail_down.set_colorkey(white)

snake_body_h = pygame.image.load(trip + "/data/Image/Horizontal.png").convert()
snake_body_v = pygame.image.load(trip + "/data/Image/Vertical.png").convert()

portal_image = []
color = white
for i in range(6):
    portal_image.append(pygame.image.load(trip + '/data/Image/portal' + str(i+1) + '.png').convert())
    if i == 3 or i == 5:
        color = black
    else:
        color = white
    portal_image[i].set_colorkey(color)

door = pygame.image.load(trip + '/data/Image/door.png').convert()
door.set_colorkey(white)
prise = pygame.image.load(trip + '/data/Image/prise.png').convert()
prise.set_colorkey(white)

snake_body_upleft = pygame.image.load(trip + "/data/Image/sUpleft.png").convert()
snake_body_upright = pygame.image.load(trip + "/data/Image/sUpright.png").convert()
snake_body_downleft = pygame.image.load(trip + "/data/Image/Downleft.png").convert()
snake_body_downright = pygame.image.load(trip + "/data/Image/Downright.png").convert()

life_p = pygame.image.load(trip + "/data/Image/life.png").convert()

eat = []
for i in range(10):
    eat.append(pygame.image.load(trip + "/data/Image/Eat" + str(i+1) + ".png").convert())
    eat[i].set_colorkey(white)

bomb_p = pygame.image.load(trip + "/data/Image/sbomb.png").convert()
bomb_p.set_colorkey(white)

a = 8
n = 3
pause = 0
menu = 1
x_lvl = 9
y_lvl = 300
dx_lvl = 40
dy_lvl = 40
event_eat = 0
lvl_l = [[x_lvl, y_lvl, dx_lvl, dy_lvl]]
for i in range(15):
    lvl_l.append([x_lvl + dx_lvl + 10,y_lvl,dx_lvl,dy_lvl])
    x_lvl += dx_lvl + 10
    if i == 6:
        x_lvl = 9 - dx_lvl - 10
        y_lvl += dy_lvl + 10
continue_l = [140, 166, 128, 36]
menu_l = [140, 208, 128, 36]
begin_l = [150, 146, 108, 36]
constructor = [140,195,128,36]
arrow_left = [16, 278, 26, 13]
arrow_right = [366, 278, 26, 13]
arrowl_color = arrowr_color = grey2
maxlvl_open = open(trip + '/data/lvl/maxlvl.txt', 'r')
maxlvl = int(maxlvl_open.read())
lvl = maxlvl
maxlvl_open.close()
count_lvl_open = open(trip + '/data/lvl/count_lvl.txt', 'r')
count_lvl = int(count_lvl_open.read())
lvl_color = [grey for i in range(count_lvl)]
for i in range(lvl):
    lvl_color[i] = grey2
if count_lvl%16 == 0:
    page = count_lvl/16
else:
    page = count_lvl//16 + 1
life = 3
count_bomb = 9
count_eat = 8
count_prise = 10
death = 0
win = 0
constr = 0
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
            maxlvl_open = open(trip + '/data/lvl/maxlvl.txt', 'w')
            maxlvl_open.write(str(maxlvl))
            maxlvl_open.close()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if (pause == 1 or life == 0) and continue_l[0] <= x_mouse <= continue_l[0] + continue_l[2] and continue_l[1] <= y_mouse <= continue_l[1] + continue_l[3] :
                continue_color = grey
            if menu == 1 and begin_l[0] <= x_mouse <= begin_l[0] + begin_l[2] and begin_l[1] <= y_mouse <= begin_l[1] + begin_l[3]:
                begin_color = grey
            if (pause == 1 or life == 0 or win == 1) and menu_l[0] <= x_mouse <= menu_l[0] + menu_l[2] and menu_l[1] <= y_mouse <= menu_l[1] + menu_l[3]:
                menu_color = grey
            elif menu == 1:
                if maxlvl//(page*16) > 0:
                    k = 16*page
                else:
                    k = maxlvl
                for i in range((page-1)*16,maxlvl):
                    if lvl_l[i%16][0] <= x_mouse <= lvl_l[i%16][0] + lvl_l[i%16][2] and lvl_l[i%16][1] <= y_mouse <= lvl_l[i%16][1] + lvl_l[i%16][3]:
                        lvl_color[i] = red
                        for j in range(maxlvl):
                            if j != i:
                                lvl_color[j] = grey2
                        break
                if page > 1 and arrow_left[0] <= x_mouse <= arrow_left[0] + arrow_left[2] and arrow_left[1] <= y_mouse <= arrow_left[1] + arrow_left[3]:
                    arrowl_color = grey
                if page*16 < count_lvl and arrow_right[0] <= x_mouse <= arrow_right[0] + arrow_right[2] and arrow_right[1] <= y_mouse <= arrow_right[1] + arrow_right[3]:
                    arrowr_color = grey
                if 0 <= x_mouse - constructor[0] <= constructor[2] and 0 <= y_mouse - constructor[1] <= constructor[3]:
                    constructor_color = grey

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1 :
            if (menu == 1 and begin_l[0] <= x_mouse <= begin_l[0] + begin_l[2] and begin_l[1] <= y_mouse <= begin_l[1] + begin_l[3] and
                    begin_color == grey or life == 0 and x_mouse >= continue_l[0] and x_mouse <= continue_l[0] + continue_l[2] and y_mouse >= continue_l[1] and
                    y_mouse <= continue_l[1] + continue_l[3] and continue_color == grey):
                if menu == 1:
                    begin_color = grey2
                    draw_menu()
                    pygame.display.flip()
                else:
                    continue_color = grey2
                    draw_gameover()
                    pygame.display.flip()
                clock.tick(10)
                menu = 0
                lvl_open = []
                lvl_open = open_lvl(lvl_open)
                if lvl_open == []:
                    lvl_type = 1
                    portal = 0
                else:
                    lvl_type = int(lvl_open.read(1))
                    portal = int(lvl_open.read(2))
                if lvl_type == 1:
                    life = 3
                elif 2 <= lvl_type <= 3:
                    life = 20
                bomb = [[] for i in range(count_bomb)]
                eatxy = [[] for i in range(count_eat)]
                prisexy = [[] for i in range(count_prise)]
                e = [random.randint(0, 9) for i in range(count_eat)]
                maxlen = 20
                if lvl_type == 1:
                    n = 3
                elif 2 <= lvl_type <= 3:
                    n = 8
                for i in range(maxlvl):
                    if lvl_color[i] == red:
                        lvl_color[i] = grey2
                x = []
                y = []
                dx = []
                dy = []
                up = []
                snake_portal = []
                down = []
                left = []
                right = []
                p = a * n
                angle = []
                for i in range(n):
                    x.append(p)
                    p -= a
                    y.append(a)
                    dx.append(a)
                    dy.append(0)
                    snake_portal.append([0])
                    angle.append([0,0,0,0])
                    # [0,0,0,0] - upleft, upright, downleft, downright
                if lvl_type == 1:
                    for i in range(len(eatxy)):
                        eatxy[i] = eat_location(eatxy[i])
                    for i in range(len(bomb)):
                        bomb[i] = eat_location(bomb[i])
                    for i in range(len(eatxy)):
                        eatxy[i] = eat_check(eatxy,bomb,i)
                    for i in range(len(bomb)):
                        bomb[i] = eat_check(bomb,eatxy,i)
                elif lvl_type == 2:
                    door_open = []
                    door_open = open_lvl(door_open)
                    for line in door_open:
                        list = line.split()
                        if len(list) == 2:
                            doorxy = [int(list[0]), int(list[1])]
                elif lvl_type == 3:
                    for i in range(len(prisexy)):
                        prisexy[i] = eat_location(prisexy[i])
                    for i in range(len(prisexy)):
                        prisexy[i] = eat_check(prisexy,[],i)

            else:   begin_color = grey2
            if pause == 1 and life != 0 and x_mouse >= continue_l[0] and x_mouse <= continue_l[0] + continue_l[2] and y_mouse >= continue_l[1] and y_mouse <= continue_l[1] + continue_l[3] and continue_color == grey:
                continue_color = grey2
                pause = -1
            else: continue_color = grey2
            if (pause == 1 or life == 0 or win == 1) and menu_l[0] <= x_mouse <= menu_l[0] + menu_l[2] and menu_l[1] <= y_mouse <= menu_l[1] + menu_l[3] and menu_color == grey:
                menu_color = grey2
                continue_color = grey2
                menu = 1
                pause = 0
                win = 0
                lvl = maxlvl
            elif menu == 1:
                if maxlvl//(page*16) > 0:
                    k = 16*page
                else:
                    k = maxlvl
                for i in range((page-1)*16, k):
                    if lvl_l[i%16][0] <= x_mouse <= lvl_l[i%16][0] + lvl_l[i%16][2] and lvl_l[i%16][1] <= y_mouse <= lvl_l[i%16][1] + lvl_l[i%16][3] and lvl_color[i] == red:
                        lvl = i + 1
                        break
                    else:
                        lvl_color[i] = grey2
                        lvl = maxlvl
                if page > 1 and arrow_left[0] <= x_mouse <= arrow_left[0] + arrow_left[2] and arrow_left[1] <= y_mouse <= arrow_left[1] + arrow_left[3] and arrowl_color == grey:
                    arrowl_color = grey2
                    page -= 1
                else:
                    arrowl_color = grey2
                if page*16 < count_lvl and arrow_right[0] <= x_mouse <= arrow_right[0] + arrow_right[2] and arrow_right[1] <= y_mouse <= arrow_right[1] + arrow_right[3] and arrowr_color == grey:
                    arrowr_color = grey2
                    page += 1
                else:
                    arrowr_color = grey2
                if 0 <= x_mouse - constructor[0] <= constructor[2] and 0 <= y_mouse - constructor[1] <= constructor[3] and constructor_color == grey:
                    constructor_color = grey2
                    draw_menu()
                    pygame.display.flip()
                    clock.tick(10)
                    done = False
                    constr = 1
                else:
                    constructor_color = grey2
            else: menu_color = grey2
        if event.type == pygame.KEYDOWN and pause != 1 and menu != 1:
            if event.key == pygame.K_ESCAPE and menu != 1:
                pause = 1
            if (event.key == pygame.K_UP or event.key == pygame.K_w) and dy[0] == 0:
                up.append(0)
                break
            if (event.key == pygame.K_DOWN or event.key == pygame.K_s) and dy[0] == 0:
                down.append(0)
                break
            if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and dx[0] == 0:
                left.append(0)
                break
            if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and dx[0] == 0:
                right.append(0)
                break

    pos = pygame.mouse.get_pos()
    x_mouse = pos[0]
    y_mouse = pos[1]
    if menu == 0 and life != 0:

        if pause == 0 and life != 0:
            move()
            death = snake_death(death)
            if death == 1:
                life -= 1
            if lvl_type == 1:
                for i in range(len(eatxy)):
                    eatxy[i], e[i], event_eat = eating(eatxy[i],e[i],event_eat)
                    if event_eat == 1:
                        eatxy[i] = eat_check(eatxy,bomb,i)
                        event_eat = 0
                for i in range(len(bomb)):
                    bomb[i], life, event_eat = boom(bomb[i],life,event_eat)
                    if event_eat == 1:
                        bomb[i] = eat_check(bomb,eatxy,i)
                        event_eat = 0
            elif lvl_type == 3:
                prisexy = prise_collect(prisexy)
            borders()

            teleport()
            shortening()

        screen.fill(Green2)

        draw_lvl()

        if lvl_type == 1:
            if len(x) >= maxlen:
                menu = 1
                win = 1
                if maxlvl == lvl and lvl < count_lvl:
                    maxlvl += 1
                    lvl += 1
                    lvl_color[lvl-1] = grey2
            else:
                for i in range(len(eatxy)):
                    screen.blit(eat[e[i]], eatxy[i])
                for i in range(len(bomb)):
                    screen.blit(bomb_p, bomb[i])
        elif lvl_type == 2:
            screen.blit(door,doorxy)
            if 0 <= x[0] - doorxy[0] < 16 and 0 <= y[0] - doorxy[1] < 16:
                menu = 1
                win = 1
                if maxlvl == lvl and lvl < count_lvl:
                    maxlvl += 1
                    lvl += 1
                    lvl_color[lvl - 1] = grey2
        elif lvl_type == 3:
            for i in range(len(prisexy)):
                screen.blit(prise,prisexy[i])
            if len(prisexy) == 0:
                menu = 1
                win = 1
                if maxlvl == lvl and lvl < count_lvl:
                    maxlvl += 1
                    lvl += 1
                    lvl_color[lvl - 1] = grey2

        if death != 1 or life != 0: draw_snake()
        draw_inf()

        if death == 1 and life != 0:
            pygame.draw.rect(screen,red,[0,0,408,428],16)
            pygame.display.flip()
            clock.tick()
            death = 0

        if abs(pause) == 1:
            draw_pause()
            if pause == -1:
                pause = 0
    else:
        screen.fill(cyan)
        if life == 0 and menu != 1:
            draw_gameover()
        else:
            if win == 1:
                draw_win()
            else:
                draw_menu()

    pygame.display.flip()

    clock.tick(10)

pygame.quit ()
if constr == 1:
    os.system(trip + '/data/Constructor.py')
