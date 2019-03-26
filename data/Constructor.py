import pygame, os, sys
pygame.init()

def check_naezd(event_naezd, naezdxy):
    min = 409
    for i in range(len(rectxy) - 1):
        if direction == [1, 0, 0, 0] and x_mouse >= rectxy[i][0] and 0 <= dop[1] - rectxy[i][1] < rectxy[i][3] and dop[
            0] < rectxy[i][0] and rectxy[i][0] - dop[0] < min:
            min = rectxy[i][0] - dop[0]
            event_naezd = 1
            rectxy[len(rectxy) - 1][2] = rectxy[i][0] - rectxy[len(rectxy) - 1][0]
            naezdxy = rectxy[i][0:2]
        elif direction == [0, 1, 0, 0] and x_mouse < rectxy[i][0] + rectxy[i][2] and 0 <= dop[1] - rectxy[i][1] < rectxy[i][3] and \
                dop[0] > rectxy[i][0] and dop[0] - rectxy[i][0] < min:
            min = dop[0] - rectxy[i][0]
            event_naezd = 1
            rectxy[len(rectxy) - 1][0] = rectxy[i][0] + rectxy[i][2]
            rectxy[len(rectxy) - 1][2] = dop[0] - rectxy[i][0] - rectxy[i][2] + 8
            naezdxy = rectxy[i][0:2]
        elif direction == [0, 0, 1, 0] and y_mouse >= rectxy[i][1] and 0 <= dop[0] - rectxy[i][0] < rectxy[i][2] and \
                dop[1] < rectxy[i][1] and rectxy[i][1] - dop[1] < min:
            min = rectxy[i][1] - dop[1]
            event_naezd = 1
            rectxy[len(rectxy) - 1][3] = rectxy[i][1] - rectxy[len(rectxy) - 1][1]
            naezdxy = rectxy[i][0:2]
        elif direction == [0, 0, 0, 1] and y_mouse < rectxy[i][1] + rectxy[i][3] and 0 <= dop[0] - rectxy[i][0] < rectxy[i][2] and \
                dop[1] > rectxy[i][1] and dop[1] - rectxy[i][1] < min:
            min = dop[1] - rectxy[i][1]
            event_naezd = 1
            rectxy[len(rectxy) - 1][1] = rectxy[i][1] + rectxy[i][3]
            rectxy[len(rectxy) - 1][3] = dop[1] - rectxy[i][1] - rectxy[i][3] + 8
            naezdxy = rectxy[i][0:2]
    return event_naezd, naezdxy

def check_end(rectxy):
    list = rectxy
    event = 0
    for i in range(len(rectxy)):
        for j in range(len(rectxy)):
            if j != i:
                if rectxy[i][3] == rectxy[j][3] == 8 and rectxy[j][1] == rectxy[i][1] and (rectxy[j][0] + rectxy[j][2] == rectxy[i][0] or rectxy[j][0] == rectxy[i][0] + rectxy[i][2]):
                    list[i][0] = min(rectxy[i][0], rectxy[j][0])
                    list[i][2] = rectxy[i][2] + rectxy[j][2]
                    list.pop(j)
                    event = 1
                    break
                elif rectxy[i][2] == rectxy[j][2] == 8 and rectxy[j][0] == rectxy[i][0] and (rectxy[j][1] + rectxy[j][3] == rectxy[i][1] or rectxy[j][1] == rectxy[i][1] + rectxy[i][3]):
                    list[i][1] = min(rectxy[i][1], rectxy[j][1])
                    list[i][3] = rectxy[i][3] + rectxy[j][3]
                    list.pop(j)
                    event = 1
                    break
        if event == 1:
            break
    if event == 1:
        list = check_end(list)
    else:
        list2 = list
        k = len(list2)
        for i in range(k):
            if list[i][0] == 0:
                list.append([408,list[i][1],8,list[i][3]])
            if list[i][1] == 0:
                list.append([list[i][0],408,list[i][2],8])
            if list[i][0] == 400 or list[i][0] + list[i][2] == 408:
                list.append([-8,list[i][1],8,list[i][3]])
            if list[i][1] == 400 or list[i][1] + list[i][3] == 408:
                list.append([list[i][0],-8,list[i][2],8])

    return  list

def draw_page1():
    screen.fill(cyan)
    font = pygame.font.Font(None, 33)
    text = font.render('Вы хотите создать новый уровень', True, black)
    screen.blit(text,[22,120])
    text = font.render('или изменить уже имеющийся?', True, black)
    screen.blit(text,[38,160])

    font = pygame.font.Font(None, 25)
    pygame.draw.rect(screen,button_changelvl_color,button_changelvl,0)
    pygame.draw.rect(screen,black,button_changelvl,1)
    text = font.render('Изменить уровень', True, black)
    screen.blit(text,[button_changelvl[0]+4,button_changelvl[1]+5])
    
    pygame.draw.rect(screen, button_createlvl_color, button_createlvl, 0)
    pygame.draw.rect(screen, black, button_createlvl, 1)
    text = font.render('Создать новый', True, black)
    screen.blit(text, [button_createlvl[0]+13,button_createlvl[1]+5])

def draw_select_lvl():
    pygame.draw.rect(screen,green,[50,120,308,140],0)
    pygame.draw.rect(screen,black,[50,120,308,140],1)
    font = pygame.font.Font(None,25)
    text = font.render('Введите номер уровня, который', True, black)
    screen.blit(text,[73,140])
    text = font.render('хотите изменить, и нажмите Enter.', True, black)
    screen.blit(text,[70,170])
    #select_lvl = [180,200,48,24]

    pygame.draw.rect(screen,white,select_lvl,0)
    pygame.draw.rect(screen,black,select_lvl,1)
    text = font.render(lvl_str,True,black)
    screen.blit(text,[select_lvl[0] + 20 - (len(lvl_str)-1)*5, select_lvl[1] + 4])
    if er != 1:
        font = pygame.font.Font(None,17)
        if er == 0:
            text = font.render('К сожелению,  уровни с 1 по 16 нельзя изменить.', True, red)
        else:
            text = font.render('Такого уровня не существует. Повторите попытку.', True, red)
        screen.blit(text,[53,230])
    pygame.draw.rect(screen,back_color,back,0)
    pygame.draw.rect(screen,black,back,1)
    pygame.draw.line(screen,black,[back[0] + 3,back[1] + 3],[back[0] + back[2] - 4, back[1] + back[3] - 4])
    pygame.draw.line(screen,black,[back[0] + 3,back[1] + back[3] - 4],[back[0] + back[2] - 4, back[1] + 3])


def draw_page2():
    screen.fill(cyan)
    font = pygame.font.Font(None, 33)
    text = font.render('Выберете тип вашего уровня.', True, black)
    screen.blit(text, [45,80])
    font = pygame.font.Font(None, 21)
    text = font.render('(Для выбора нажмите соответствующую клавишу)', True, black)
    screen.blit(text, [15,110])
    font = pygame.font.Font(None, 26)
    text = font.render('1 тип: Цель - достичь необходимой длины.', True, black)
    screen.blit(text, [25,170])
    text = font.render('2 тип: Цель - найти выход из лабиринта.', True, black)
    screen.blit(text, [25, 210])
    text = font.render('3 тип: Цель - собрать десять призов.', True, black)
    screen.blit(text, [25, 250])



def draw_snake(list):
    x = list[0]
    for i in range(list[2]//8):
        if i == 0:
            screen.blit(snake_tail_right,[x,list[1]])
        elif i == list[2]//8-1:
            screen.blit(snake_head_right,[x,list[1]-1])
        else:
            screen.blit(snake_body_h, [x,list[1]])
        x += 8

def draw_page3():
    screen.fill(Green2)
    for i in range(len(rectxy)):
        if i == 0:
            draw_snake(rectxy[i])
        elif door == 2 and i == 1:
            screen.blit(door_p, [rectxy[i][0],rectxy[i][1]])
        else:
            if not(door == 1 and i == 1):
                pygame.draw.rect(screen, black, rectxy[i], 0)

    j = 0
    for i in range(len(portalxy)):
        screen.blit(portal_image[int(j)], [portalxy[i][0], portalxy[i][1]])
        j += 0.5

    if portal == 0 and len(portalxy) < 12 and y_mouse0 <= 408:
        screen.blit(portal_image[int(number_portal)], [x_mouse, y_mouse])
    if door == 1:
        screen.blit(door_p, [x_mouse, y_mouse])

    pygame.draw.rect(screen, white, [0,408,408,20], 0)
    pygame.draw.rect(screen, black, [0,408,408,20], 1)

    pygame.draw.rect(screen,button_clear_color,button_clear,0)
    pygame.draw.rect(screen,black,button_clear,1)
    font = pygame.font.Font(None,17)
    text = font.render('Очистить', True, black)
    screen.blit(text, [button_clear[0] + 2, button_clear[1] + 2])

    if portal == 1:
        pygame.draw.rect(screen, button_continue_color, button_continue, 0)
        pygame.draw.rect(screen, black, button_continue, 1)
        text = font.render('Далее', True, black)
        screen.blit(text, [button_continue[0] + 3, button_continue[1] + 2])

        pygame.draw.rect(screen, button_delete_color, button_delete, 0)
        pygame.draw.rect(screen, black, button_delete, 1)
        text = font.render('Режим удаления', True, black)
        screen.blit(text, [button_delete[0] + 2, button_delete[1] + 2])
    else:
        pygame.draw.rect(screen, button_save_color, button_save, 0)
        pygame.draw.rect(screen, black, button_save, 1)
        text = font.render('Сохранить', True, black)
        screen.blit(text, [button_save[0] + 3, button_save[1] + 2])

        pygame.draw.rect(screen, button_addportal_color, button_addportal,0)
        pygame.draw.rect(screen, black, button_addportal,1)
        text = font.render('Добавить порталы', True, black)
        screen.blit(text, [button_addportal[0] + 2, button_addportal[1] + 2])
    pygame.draw.rect(screen, button_return_color, button_return, 0)
    screen.blit(return_p,[button_return[0]+2,button_return[1]])
    pygame.draw.rect(screen, black, button_return,1)

def save(lvl):
    draw_page3()
    pygame.display.flip()
    clock.tick(20)
    lvl_write = open(trip + '/lvl/lvl' + str(lvl) + '.txt', 'w')
    lvl_write.write(str(lvl_type) + '\n')
    if door != 0:
        lvl_write.write(str(rectxy[1][0]) + ' ' + str(rectxy[1][1]) + '\n')
        rectxy.pop(1)
    rectxy[1:] = check_end(rectxy[1:])
    for i in range(1, len(rectxy)):
        for j in range(len(rectxy[i])):
            lvl_write.write(str(rectxy[i][j]) + ' ')
        if i != len(rectxy) - 1:
            lvl_write.write('\n')
    lvl_write.close()
    if portalxy != []:
        if len(portalxy) % 2 != 0:
            portalxy.pop()
        portal_write = open(trip + '/portal/portal' + str(lvl) + '.txt', 'w')
        for i in range(len(portalxy)):
            for j in range(len(portalxy[i])):
                portal_write.write(str(portalxy[i][j]) + ' ')
            if i != len(portalxy) - 1:
                portal_write.write('\n')
        portal_write.close()
    count_lvl = open(trip + '/lvl/count_lvl.txt','r')
    if lvl == int(count_lvl.read()) + 1:
        count_lvl.close()
        count_lvl = open(trip + '/lvl/count_lvl.txt', 'w')
        count_lvl.write(str(lvl))
        count_lvl.close()
        max_lvl = open(trip + '/lvl/maxlvl.txt', 'r')
        if int(max_lvl.read()) == lvl  - 1:
            max_lvl.close()
            max_lvl = open(trip + '/lvl/maxlvl.txt', 'w')
            max_lvl.write(str(lvl))
            max_lvl.close()
    lvl_open = open(trip + '/lvl/count_lvl.txt', 'r')
    lvl = int(lvl_open.read()) + 1
    lvl_open.close()
    return lvl

black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
red = (255,0,0)
red2 = (200,0,0)
blue = (0,0,255)
yellow = (255,255,0)
cyan = (0,255,255)
grey = (190,190,190)
orange = (255,165,0)
brown = (139,69,19)
purple = (160,32,240)
DarkGreen = (0,128,0)
grey2 = (220,220,220)
Green2 = (180,255,140)

pi = 3.141592653
rectxy = [[8,8,64,8]]
mousedown = 0
event_naezd = 0
naezdxy = []
dop = []

trip = sys.path[0]

count_open = open(trip + '/lvl/count_lvl.txt', 'r')
lvl = int(count_open.read()) + 1
count_open.close()
p = True
portalxy = []
delete = 1
portal = 1
page = 1
door = 0
button_changelvl = [13,220,155,30]
button_createlvl = [240,220,155,30]
button_clear = [23,410,65,16]
button_continue = [364, 410,42,16]
button_return = [2,410,20,16]
button_delete = [89,410,106,16]
button_save = [338,410,68,16]
button_addportal = [218,410,119,16]
select_lvl = [180,200,48,24]
back = [343,120,15,15]
back_color = red
button_changelvl_color = button_createlvl_color = button_clear_color = button_continue_color = button_return_color = button_delete_color = button_save_color = button_addportal_color = grey2
direction = [0,0,0,0] #right/left/down/up
size = [408,428]
screen = pygame.display.set_mode(size)

snake_head_right = pygame.image.load(trip + "/Image/Headright.png").convert()
snake_head_right.set_colorkey(white)
snake_tail_right = pygame.image.load(trip + "/Image/Tailright.png").convert()
snake_tail_right.set_colorkey(white)
snake_body_h = pygame.image.load(trip + "/Image/Horizontal.png").convert()
return_p = pygame.image.load(trip + '/Image/sreturn.png').convert()
return_p.set_colorkey(white)
door_p = pygame.image.load(trip + '/Image/door.png').convert()
door_p.set_colorkey(white)

number_portal = 0
portal_image = []
color = white
for i in range(6):
    portal_image.append(pygame.image.load(trip + '/Image/portal' + str(i+1) + '.png').convert())
    if i == 3 or i == 5:
        color = black
    else:
        color = white
    portal_image[i].set_colorkey(color)

pygame.display.set_caption('Constructor')

done = True
clock = pygame.time.Clock()

while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if page == 1:
                    if button_createlvl[0] <= x_mouse0 <= button_createlvl[0] + button_createlvl[2] and button_createlvl[1] <= y_mouse0 <= button_createlvl[1] + button_createlvl[3]:
                        button_createlvl_color = grey
                    if button_changelvl[0] <= x_mouse0 <= button_changelvl[0] + button_changelvl[2] and button_changelvl[1] <= y_mouse0 <= button_changelvl[1] + button_changelvl[3]:
                        button_changelvl_color = grey
                elif page == 1.5:
                    if back[0] <= x_mouse0 <= back[0] + back[2] and back[1] <= y_mouse0 <= back[1] + back[3]:
                        back_color = red2
                elif page == 3:
                    if button_clear[0] <= x_mouse0 <= button_clear[0] + button_clear[2] and button_clear[1] <= y_mouse0 <= button_clear[1] + button_clear[3]:
                        button_clear_color = grey
                    elif portal == 1 and button_continue[0] <= x_mouse0 <= button_continue[0] + button_continue[2] and button_continue[1] <= y_mouse0 <= button_continue[1] + button_continue[3]:
                        button_continue_color = grey
                    elif button_return[0] <= x_mouse0 <= button_return[0] + button_return[2] and button_return[1] <= y_mouse0 <= button_return[1] + button_return[3]:
                        button_return_color = grey
                    elif portal == 1 and button_delete[0] <= x_mouse0 <= button_delete[0] + button_delete[2] and button_delete[1] <= y_mouse0 <= button_delete[1] + button_delete[3]:
                        if button_delete_color == grey2:
                            button_delete_color = grey
                        else:
                            button_delete_color = grey2
                        delete *= -1
                    elif portal != 1 and button_save[0] <= x_mouse0 <= button_save[0] + button_save[2] and button_save[1] <= y_mouse0 <= button_save[1] + button_save[3]:
                        button_save_color = grey
                    elif portal == -1 and button_addportal[0] <= x_mouse0 <= button_addportal[0] + button_addportal[2] and button_addportal[1] <= y_mouse0 <= button_addportal[1] + button_addportal[3]:
                        button_addportal_color = grey
                    else:
                        if y_mouse0 <= 408:
                            direction = [0,0,0,0]
                            mousedown = 1
                            if delete == 1 and portal == 1 and door != 1:
                                rectxy.append([x_mouse, y_mouse, 8, 8])
                                dop = rectxy[len(rectxy) - 1][0:2]
                                for i in range(len(rectxy)-1):
                                    if 0 <= x_mouse - rectxy[i][0] < rectxy[i][2] and 0 <= y_mouse - rectxy[i][1] < rectxy[i][3]:
                                        rectxy.pop()
                                        mousedown = 0
                                        break
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if page == 1:
                    if button_createlvl[0] <= x_mouse0 <= button_createlvl[0] + button_createlvl[2] and button_createlvl[1] <= y_mouse0 <= button_createlvl[1] + button_createlvl[3] and button_createlvl_color == grey:
                        page += 1
                        button_createlvl_color = grey2
                        draw_page1()
                        pygame.display.flip()
                        clock.tick(20)
                    else:
                        button_createlvl_color = grey2
                    if button_changelvl[0] <= x_mouse0 <= button_changelvl[0] + button_changelvl[2] and button_changelvl[1] <= y_mouse0 <= button_changelvl[1] + button_changelvl[3]:
                        page += 0.5
                        er  = 1
                        lvl_str = ''
                        button_changelvl_color = grey2
                        draw_page1()
                        pygame.display.flip()
                        clock.tick(20)
                    else:
                        button_changelvl_color = grey2
                elif page == 1.5:
                    if back[0] <= x_mouse0 <= back[0] + back[2] and back[1] <= y_mouse0 <= back[1] + back[3] and back_color == red2:
                        page = 1
                        back_color = red
                        draw_select_lvl()
                        pygame.display.flip()
                        clock.tick(20)
                    else:
                        back_color = red
                elif page == 3:
                    if button_clear[0] <= x_mouse0 <= button_clear[0] + button_clear[2] and button_clear[1] <= y_mouse0 <= button_clear[1] + button_clear[3] and button_clear_color == grey:
                        rectxy = [rectxy[0]]
                        if door == 2:
                            rectxy.append([0,0,16,16])
                            door = 1
                        portalxy = []
                        button_clear_color = grey2
                        portal = 1
                        number_portal = 0
                    else:
                        button_clear_color = grey2
                    if portal == 1 and portal == 1 and button_continue[0] <= x_mouse0 <= button_continue[0] + button_continue[2] and button_continue[1] <= y_mouse0 <= button_continue[1] + button_continue[3] and button_continue_color == grey:
                        button_continue_color = grey2
                        portal = -1
                    else:
                        button_continue_color = grey2
                    if button_return[0] <= x_mouse0 <= button_return[0] + button_return[2] and button_return[1] <= y_mouse0 <= button_return[1] + button_return[3] and button_return_color == grey:
                        if door == 2 and len(rectxy) == 2:
                            h = 2
                            door = 1
                        else: h = 1
                        if len(rectxy) != h and portal == 1:
                            rectxy.pop()
                        elif portal == 0 and portalxy != []:
                            portalxy.pop()
                            number_portal -= 0.5
                        button_return_color = grey2
                    else:
                        button_return_color = grey2
                    if portal != 1 and button_save[0] <= x_mouse0 <= button_save[0] + button_save[2] and button_save[1] <= y_mouse0 <= button_save[1] + button_save[3] and button_save_color == grey:
                        lvl = save(lvl)
                        page = 1
                        rectxy = [[8, 8, 64, 8]]
                        portalxy = []
                        door = 0
                        portal = 1
                    else:
                        button_save_color = grey2
                    if portal != 1 and button_addportal[0] <= x_mouse0 <= button_addportal[0] + button_addportal[2] and button_addportal[1] <= y_mouse0 <= button_addportal[1] + button_addportal[3] and button_addportal_color == grey:
                        button_addportal_color = grey2
                        portal = 0
                        lvl_type += 1
                    mousedown = 0
                    event_naezd = 0
                    naezdxy = []
                    if not p:
                        p = True
        if event.type == pygame.KEYDOWN and mousedown == 0:
            if event.key == pygame.K_BACKSPACE:
                if page == 1.5:
                    lvl_str = lvl_str[0:len(lvl_str)-1]
                elif page == 3:
                    if door == 2 and len(rectxy) == 2:
                        door = 1
                        h = 2
                    else:
                        h = 1
                    if len(rectxy) != h and portal == 1:
                        rectxy.pop()
                    elif portal == 0 and portalxy != []:
                        portalxy.pop()
                        number_portal -= 0.5
                    button_return_color = grey2
            if page == 1.5:
                if  len(lvl_str) < len(str(lvl)):
                    if event.key == pygame.K_1:
                        lvl_str += '1'
                    if event.key == pygame.K_2:
                        lvl_str += '2'
                    if event.key == pygame.K_3:
                        lvl_str += '3'
                    if event.key == pygame.K_4:
                        lvl_str += '4'
                    if event.key == pygame.K_5:
                        lvl_str += '5'
                    if event.key == pygame.K_6:
                        lvl_str += '6'
                    if event.key == pygame.K_7:
                        lvl_str += '7'
                    if event.key == pygame.K_8:
                        lvl_str += '8'
                    if event.key == pygame.K_9:
                        lvl_str += '9'
                    if event.key == pygame.K_0:
                        lvl_str += '0'
                if event.key == pygame.K_RETURN and lvl_str != '':
                    if 16 < int(lvl_str) < lvl:
                        page += 0.5
                        lvl = int(lvl_str)
                        rectxy_open = open(trip + '/lvl/lvl' + str(lvl) + '.txt', 'r')
                        for line in rectxy_open:
                            rectxy.append([int(i) for i in line.split()])
                            if len(rectxy[len(rectxy)-1]) == 4 and (rectxy[len(rectxy)-1][0] == -8 or rectxy[len(rectxy)-1][0] == 408 or  rectxy[len(rectxy)-1][1] == -1 or rectxy[len(rectxy)-1][1] == 408):
                                rectxy.pop()
                                break
                        rectxy.pop(1)

                    else:
                        if int(lvl_str) <= 16:
                            er = 0
                        else:
                            er = 0.5
                        lvl_str = ''
            if page == 2:
                if event.key == pygame.K_1:
                    lvl_type = 10
                    rectxy[0] = [8,8,24,8]
                    if len(rectxy) > 1 and len(rectxy[1]) == 2:
                        rectxy.pop(1)
                    page += 1
                elif event.key == pygame.K_2:
                    lvl_type = 20
                    door = 1
                    page += 1
                    if len(rectxy) > 1 and len(rectxy[1]) == 2:
                        rectxy[1].append(16)
                        rectxy[1].append(16)
                        door = 2
                    else:
                        if len(rectxy) > 1:
                            rectxy.append(rectxy[1])
                            rectxy[1] = [0,0,16,16]
                        else:
                            rectxy.append([0,0,16,16])
                elif event.key == pygame.K_3:
                    if len(rectxy) > 1 and len(rectxy[1]) == 2:
                        rectxy.pop(1)
                    lvl_type = 30
                    page += 1

    pos = pygame.mouse.get_pos()
    x_mouse0 = pos[0]
    y_mouse0 = pos[1]

    x_mouse = x_mouse0 - x_mouse0%8
    y_mouse = y_mouse0 - y_mouse0%8
    if y_mouse0 > 408:
        y_mouse = 400
    if page == 1:
        page = 1
    elif page == 3:
        if portal == 1:
            if door == 1:
                d = True
                if mousedown == 1:
                    if x_mouse >= 400 or y_mouse >= 400:
                        d = False
                    for i in range(len(rectxy)):
                        if i != 1 and ((0 <= x_mouse - rectxy[i][0] <= rectxy[i][2] and 0 <= y_mouse - rectxy[i][1] <= rectxy[i][3]) or \
                                (0 <= x_mouse + 8 - rectxy[i][0] <= rectxy[i][2] and 0 <= y_mouse + 8 - rectxy[i][1] <= rectxy[i][3]) or \
                                (0 <= x_mouse  - rectxy[i][0] <= rectxy[i][2] and 0 <= y_mouse + 8 - rectxy[i][1] <= rectxy[i][3]) or \
                                (0 <= x_mouse + 8 - rectxy[i][0] <= rectxy[i][2] and 0 <= y_mouse - rectxy[i][1] <= rectxy[i][3])):
                            d = False
                            break
                    if d == True:
                        rectxy[1] = [x_mouse, y_mouse, 16, 16]
                        door = 2
                        mousedown = 0
            else:
                if mousedown == 1 and delete == 1:
                    if event_naezd == 0 and 0 <= x_mouse <= 408 and 0 <= y_mouse <= 408:
                        if abs(x_mouse - dop[0]) >= abs(y_mouse - dop[1]):
                            rectxy[len(rectxy) - 1][3] = 8
                            rectxy[len(rectxy) - 1][0:2] = dop
                            if x_mouse - dop[0] >= 0:
                                direction = [1,0,0,0]
                                rectxy[len(rectxy)-1][2] = x_mouse - rectxy[len(rectxy)-1][0] + 8
                            else:
                                direction = [0,1,0,0]
                                rectxy[len(rectxy)-1][0] = x_mouse
                                rectxy[len(rectxy)-1][2] = -x_mouse + dop[0] + 8
                        else:
                            rectxy[len(rectxy) - 1][2] = 8
                            rectxy[len(rectxy) - 1][0:2] = dop
                            if y_mouse - dop[1] >= 0:
                                direction = [0,0,1,0]
                                rectxy[len(rectxy) - 1][3] = y_mouse - rectxy[len(rectxy) - 1][1] + 8
                            else:
                                direction = [0,0,0,1]
                                rectxy[len(rectxy) - 1][1] = y_mouse
                                rectxy[len(rectxy) - 1][3] = -y_mouse + dop[1] + 8

                    if event_naezd != 1:
                        event_naezd, naezdxy = check_naezd(event_naezd,naezdxy)
                    else:
                        if direction == [1,0,0,0]:
                            if x_mouse < naezdxy[0]:
                                event_naezd = 0
                        elif direction == [0,1,0,0]:
                            if x_mouse > naezdxy[0]:
                                event_naezd = 0
                        elif direction == [0,0,1,0]:
                            if y_mouse < naezdxy[1]:
                                event_naezd = 0
                        elif direction == [0,0,0,1]:
                            if y_mouse > naezdxy[1]:
                                event_naezd = 0
                elif delete == -1 and mousedown == 1:
                    if door == 2:
                        n = 2
                    else:
                        n = 1
                    for i in range(n,len(rectxy)):
                        if rectxy[i][0] <= x_mouse0 <= rectxy[i][0] + rectxy[i][2] and rectxy[i][1] <= y_mouse0 <= rectxy[i][1] + rectxy[i][3]:
                            rectxy.pop(i)
                            break
        else:
            if portal == 0:
                if mousedown == 1 and p:
                    for i in range(len(rectxy)):
                        if rectxy[i][0] <= x_mouse0 <= rectxy[i][0] + rectxy[i][2] and rectxy[i][1] <= y_mouse0 <= rectxy[i][1] + rectxy[i][3]:
                            p = False
                    for i in range(len(portalxy)):
                        if portalxy[i][0] == x_mouse and portalxy[i][1] == y_mouse:
                            p = False
                    if p and len(portalxy) < 12:
                        portalxy.append([x_mouse,y_mouse])
                        number_portal += 0.5
                    p = False

    if page == 1:
        draw_page1()
    elif page == 1.5:
        draw_select_lvl()
    elif page == 2:
        draw_page2()
    elif page == 3:
        draw_page3()

    pygame.display.flip()

    clock.tick(20)

pygame.quit()
os.system(os.path.join(sys.path[0],'../Snake.py'))