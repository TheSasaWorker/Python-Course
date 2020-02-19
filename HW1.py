import random
print('Disclaimer: please input the exact same strings in Fight/Run, Y/N situations, otherwise the action is not going to work. Case sensitive.')
beta_choose = input('Would you like to test the beta? Y/N ')
if beta_choose != 'Y' and beta_choose != 'N':
    beta_choose = 'N'
    print('The game has been automatically set to the newest version.')
print('Start off by creating your character: ')
name = input('Name: ')
diff = 11
diff_choose = 'NaN'
while diff_choose != 'Y' and diff_choose != 'N':
    diff_choose = input('Would you like to choose your difficulty? Y/N ')
    if diff_choose == 'Y':
        while diff > 10:
            diff = int(input('Difficulty: '))
            if diff > 10:
                print('Please input a difficulty lower than 10.')
    elif diff_choose == 'N':
        diff = random.randint(1, 10)
    else:
        print('Please answer with Y/N. ')
    if diff_choose == 'Y' or diff_choose == 'N':
        diff_confirm = input('Are you sure you want to choose difficulty ' + str(diff) + ' ? Y/N ')
        if diff_confirm == 'Y':
            print('Difficulty has been set to ' + str(diff))
        else:
            print('Please reselect your difficulty level.')
            diff_choose = 'NaN'
            diff = 11
dmg_take = random.randint(diff*3, diff*5) + 10
dmg_heal = int(50 / diff)
hp = int(1000 / diff)
if beta_choose == 'N':    
    print(name + " a luat la dificultatea " + str(diff) + " " + str(dmg_take) + " damage si\n" + "a regenerat " + str(dmg_heal) + " viata. ")
else:
    if diff == 1 or diff == 2:
        print('Very easy difficulty. Recommended for beginners, or people looking to just run through the story. The enemy gets significant disadvantages, while the player gets significant advantages.')
    elif diff == 3 or diff == 4:
        print('Easy difficulty. A bit harder than Very Easy, but still moderately simple. Recommended for people who people who want to run through the story while also getting a bit of combat experience. Enemies get a slight disadvantage, while the player gets a slight advantage.')
    elif diff == 5 or diff == 6:
        print('Normal difficulty. As the name would suggest, this is the recommended difficulty for the first playthrough. Mix of combat & story. Enemies are equal to you in terms of stats.')
    elif diff == 7 or diff == 8:
        print('Hard difficulty. Intended for people experienced with Dungeon Crawlers, and for people replaying this. Enemies get a slight combat advantage.')
    elif diff == 9 or diff == 10:
        print('Insane difficulty. Choose with caution. Intended only for masochists, and people with too much free time on their hands. Expect to be focused on the combat.')
    info_more = input('Would you like to see advanced info? Y/N ')
    if info_more == 'Y':
        print(name + ' has a health pool of ' + str(hp) + ' life points.\n' + name +  ' will take ' + str(dmg_take) + ' damage per hit.\n' + name + ' will heal ' + str(dmg_heal) + ' health points per potion.')
    game_on = 0
    while game_on != 1:
        start_game = input('Would you like to start the game? Y/N ')
        if start_game == 'Y':
            game_on = 1
        else:
            print('Please write Y should you want to start the game.')
    pts = 0
    while game_on == 1:
        enemy_type = random.randint(1, 5)
        if enemy_type == 1:
            enemy = 'Wolver'
        elif enemy_type == 2:
            enemy = 'Slime'
        elif enemy_type == 3:
            enemy = 'Skeleton'
        elif enemy_type == 4:
            enemy = 'Lost Soul'
        else:
            enemy = 'Trojan'
        enemy_elem = random.randint(1, 8)
        if enemy_elem == 1:
            elem = 'Fire'
        elif enemy_elem == 2:
            elem = 'Water'
        elif enemy_elem == 3:
            elem = 'Ice'
        elif enemy_elem == 4:
            elem = 'Wind'
        elif enemy_elem == 5:
            elem = 'Thunder'
        elif enemy_elem == 6:
            elem = 'Earth'
        elif enemy_elem == 7:
            elem = 'Light'
        else:
            elem = 'Dark'
        print('You have encountered a wild ' + elem + ' ' + enemy + '!')
        action = input('What would you like to do? Fight/Run ')
        if action == 'Fight':
            hp = int(hp - dmg_take * enemy_type / 2)
            potion_get = random.randint(1, 3)
            if potion_get == 1:
                hp = hp + dmg_heal
            pts = pts + 10 * enemy_type * enemy_elem
            if hp <= 0:
                print('You have died to a ' + elem + ' ' + enemy + '!')
                game_on = 0
            print('You are now ' + str(hp) + ' hp.')
        else:
            print('You have escaped the ' + elem + ' ' + enemy + ' with ' + str(hp) + ' hp!')
            game_on = 0
            pts = pts + hp * 2
    print('You have earned ' + str(pts) + ' points!')
    print('Thank you for playing "Generic Dungeon Crawler 1000" !')
    more_info = input('Would you like to follow the development of GDC1K? Y/N ')
    if more_info == 'Y':
        print('Here is a link to our source code: ')
