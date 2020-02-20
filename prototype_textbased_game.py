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
dmg_heal = int(500 / diff)
hp = int(1000 / diff)
max_hp = hp
dmg_deal = int(100 / diff * 4)
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
    dead = 0
    pp_bomb = 5
    pp_slash = 15
    while game_on == 1:
        escape = 0
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
        enemy_hp = 100 * (enemy_elem + enemy_type)
        action = input('What would you like to do? Fight/Run ')
        turn = 1
        if action == 'Fight':
            while enemy_hp > 0 and hp > 0 and escape == 0:
                while turn == 0:
                    if random.randint(1, 20) == 20:
                        enemy_deal = dmg_take * enemy_type * 2
                        print('The enemy has dealt a critical hit! You have taken ' + str(enemy_deal) + ' damage!')
                        hp = hp - enemy_deal
                        turn = 1
                    else:
                        enemy_deal = dmg_take * enemy_type
                        print('You have taken ' + str(enemy_deal) + ' damage!')
                        hp = hp - enemy_deal
                        turn = 1
                print('The enemy has ' + str(enemy_hp) + ' hp remaining. \nYou have ' + str(hp) + ' hp remaining.')
                while turn == 1:
                    action_take = input('You may use a basic attack (Attack), use a Special Attack(Special), use a Health Potion(Heal) or attempt to escape(Run). ')
                    if action_take == 'Attack':
                        print('You have dealt ' + str(dmg_deal) + ' damage!')
                        enemy_hp = enemy_hp - dmg_deal
                        turn = 0
                    elif action_take == 'Special':
                        print('You have access to: \n Strong Slash ' + str(pp_slash) + ' \n Heavy Bomb ' + str(pp_bomb))
                        spec_take = input('Please select a special ability: Slash/Bomb ')
                        if spec_take == 'Slash' and pp_slash > 0:
                            slash_luck = random.randint(1, 4)
                            pp_slash = pp_slash - 1
                            if slash_luck == 1:
                                enemy_hp = int(enemy_hp / 2)
                                print('You have dealt a critical worth of ' + str(enemy_hp) + ' damage!')
                                turn = 0
                            else:
                                print('You have dealt ' + str(int(enemy_hp * 3 / 4)) + ' damage!')
                                enemy_hp = int(enemy_hp * 3 / 4)
                                turn = 0
                        elif spec_take == 'Slash' and pp_slash == 0:
                            print('You do not have enough power points to use Strong Slash.')
                        elif spec_take == 'Bomb' and pp_bomb > 0:
                            bomb_kill = random.randint(1, 5)
                            pp_bomb = pp_bomb - 1
                            if bomb_kill == 5:
                                enemy_hp = 0
                                print('You have successfully blasted the enemy off to space!')
                                turn = 0
                            else:
                                print('Your bomb managed to deal ' + str(int(enemy_hp / 3)) + ' damage.')
                                enemy_hp = int(enemy_hp * 2 / 3)
                                turn = 0
                        elif spec_take == 'Bomb' and pp_bomb == 0:
                            print('You do not have enough power points to use Heavy Bomb.')
                    elif action_take == 'Heal':
                        print('You have regained ' + str(dmg_heal) + ' life points!')
                        hp = hp + dmg_heal
                        turn = 0
                    else:
                        if random.randint(1, 2) == 1:
                            print('You succesfully escaped the battle!')
                            escape = 1
                            turn = 0
                        else:
                            print('You attempted to run but the enemy intercepted you! You took ' + str(dmg_take) + ' damage!')
                            hp = hp - dmg_take
                            turn = 0
        if hp <= 0:
            print('You have been slain by a ' + elem + ' ' + enemy + '!')
            game_on = 0
        elif enemy_hp <= 0:
            print('You have slain a ' + elem + ' ' + enemy + '! You have gained ' + str(10 * enemy_type * enemy_elem) + ' points!')
            pts = pts + 10 * enemy_type * enemy_elem
        if action == 'Run':
            print('You decided to run to a nearby inn.')
            inn_action = random.randint(1, 5)
            if inn_action == 4:
                pts_steal = random.randint(10, 100)
                hp_steal = int(random.randint(10, 50) * diff / 4)
                print('On the way to the inn you were ambushed by a Bandit! He managed to steal ' + str(pts_steal) + ' points from you and has dealt ' + str(hp_steal) + ' damage to you!')
                pts = pts - pts_steal
                hp = hp - hp_steal
                if hp <= 0:
                    dead = 1
                    game_on = 0
            elif inn_action == 5:
                pts_find = random.randint(10, 100)
                hp_find = random.randint(10, 50)
                print('On the way to the inn you stumbled upon a treasure chest! You have found ' + str(pts_find) + ' points and a concoction that granted you ' + str(hp_find) + ' hp points!')
                if hp + hp_find > max_hp:
                    hp = max_hp
                else:
                    hp = hp + hp_find
                pts = pts + pts_find
            if dead == 0:
                game_continue = 'Y'
                print('You have now arrived at the inn.')
                game_continue = input('Would you like to continue? Y/N ')
                if game_continue == 'N':
                    game_on = 0
                    print('You have decided to quietly die in your sleep.')
                else:
                    print('You have rested & eaten at the inn. You have regained 100 life points.')
                    if hp + 100 > max_hp:
                        hp = max_hp
                    else:
                        hp = hp + 100
                    pp_bomb = 5
                    pp_slash = 15
    print('Your points have been adjusted to your difficulty.')
    if diff == 1 or diff == 2:
        pts = int(pts / 4)
    elif diff == 3 or diff == 4:
        pts = int(pts / 2)
    elif diff == 7 or diff == 8:
        pts = pts * 2
    elif diff == 9 or diff == 10:
        pts = pts * 4
    print('You have earned ' + str(pts) + ' points!')
    print('Thank you for playing "Generic Dungeon Crawler 1000" !')
    more_info = input('Would you like to follow the development of GDC1K? Y/N ')
    if more_info == 'Y':
        print('Here is a link to our source code: https://github.com/TheSasaWorker/Python-Course/blob/master/HW1.py')
