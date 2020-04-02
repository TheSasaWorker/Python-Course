from graphics import *
win = GraphWin(title = 'graphics window', width = 600, height = 600)
Line(Point(200, 0), Point(200, 600)).draw(win)
Line(Point(400, 0), Point(400, 600)).draw(win)
Line(Point(0, 200), Point(600, 200)).draw(win)
Line(Point(0, 400), Point(600, 400)).draw(win)
game_end = 0
# MAKING TABLE

# GET BOX NUMBER BEGIN

def get_box(posX, posY):
    if posX < 200:
        box_X = 1
    elif posX > 400:
        box_X = 3
    else:
        box_X = 2
    if posY < 200:
        box_Y = 1
    elif posY > 400:
        box_Y = 3
    else:
        box_Y = 2
    box_no = (box_Y - 1) * 3 + box_X
    return box_no

# GET BOX NUMBER END


# FORM LINES BEGIN

def form_line1(place_no):
    if place_no % 3 == 0:
        line1_y1 = (place_no / 3 - 1) * 200
        line1_y2 = place_no / 3 * 200
        line1_x1 = (place_no % 3 + 2)* 200
        line1_x2 = (place_no % 3 + 3) * 200
    else:
        line1_y1 = place_no // 3 * 200
        line1_y2 = (place_no // 3 + 1) * 200
        line1_x1 = (place_no % 3 - 1) * 200
        line1_x2 = place_no % 3 * 200
    line1 = Line(Point(line1_x1, line1_y1), Point(line1_x2, line1_y2))
    line1.setFill('red')
    line1.setWidth(3)
    return line1

def form_line2(place_no):
    
    if place_no % 3 == 0:
        line2_y1 = (place_no / 3 - 1) * 200
        line2_y2 = place_no / 3 * 200
        line2_x2 = (place_no % 3 + 2) * 200
        line2_x1 = (place_no % 3 + 3) * 200
    else:
        line2_y1 = place_no // 3 * 200
        line2_y2 = (place_no // 3 + 1) * 200
        line2_x2 = (place_no % 3 - 1) * 200
        line2_x1 = place_no % 3 * 200
    line2 = Line(Point(line2_x1, line2_y1), Point(line2_x2, line2_y2))
    line2.setFill('red')
    line2.setWidth(3)
    return line2    

# FORM LINES END


# FORM CIRCLE BEGIN

def form_circle(place_no):
    if place_no % 3 == 0:
        circle_center_y = place_no / 3
        circle_center_x = 3
    else:
        circle_center_y = place_no // 3 + 1
        circle_center_x = place_no % 3
    circle = Circle(Point((circle_center_x - 1) * 200 + 100 , (circle_center_y - 1) * 200 + 100), 100)
    circle.setWidth(3)
    circle.setOutline('blue')
    return circle

# FORM CIRCLE END


# CHECK GAME FINISH START

def game_finish(x_cells, o_cells):
    win_combos = [[1, 5, 9], [3, 5, 7], [1, 2, 3], [1, 4, 7], [4, 5, 6], [7, 8, 9], [2, 5, 8], [3, 6, 9]]
    win_x = 0
    win_o = 0
    for test in win_combos:
        continue_x = 1
        continue_o = 1
        for i in test:
            if continue_x == 0 and continue_o == 0:
                break
            if continue_x == 1:
                if i not in x_cells:
                    continue_x = 0
            if continue_o == 1:
                if i not in o_cells:
                    continue_o = 0
        if continue_x == 1:
            return 1
            break
        elif continue_o == 1:
            return 2
            break

# CHECK GAME FINISH END


# GAME BEGIN

def game():
    occupied_x = []
    occupied_o = []
    turn = 0
    while True:
        while turn == 0:
            print('Player 1\'s turn(X)')
            mouse = win.getMouse()
            place_X = mouse.getX()
            place_Y = mouse.getY()
            place_no = get_box(place_X, place_Y)
            if place_no in occupied_x or place_no in occupied_o:
                print('Please select an empty box.')
            else:
                form_line1(place_no).draw(win)
                form_line2(place_no).draw(win)
                occupied_x.append(place_no)
                turn = 1
            if len(occupied_x) + len(occupied_o) == 9:
                return -1
                break
            elif game_finish(occupied_x, occupied_o) == 1:
                return 1
                break
            elif game_finish(occupied_x, occupied_o) == 2:
                return 2
                break
        while turn == 1:
            print('Player 2\'s turn(O)')
            mouse = win.getMouse()
            place_X = mouse.getX()
            place_Y = mouse.getY()
            place_no = get_box(place_X, place_Y)
            if place_no in occupied_x or place_no in occupied_o:
                print('Please select an empty box.')
            else:
                form_circle(place_no).draw(win)
                occupied_o.append(place_no)
                turn = 0
            if len(occupied_x) + len(occupied_o) == 9:
                return -1
                break
            elif game_finish(occupied_x, occupied_o) == 1:
                return 1
                break
            elif game_finish(occupied_x, occupied_o) == 2:
                return 2
                break
game_end = game()
if game_end == -1:
    print('Draw')
elif game_end == 1:
    print('Player 1 wins')
elif game_end == 2:
    print('Player 2 wins')
# GAME END