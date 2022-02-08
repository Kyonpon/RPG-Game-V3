import random
import Enemies
import Functions
import time


# Randomized the normal enemy list
shuffle_norm_enemy_list = [x for x in Enemies.normal_enemy_list]
random.shuffle(shuffle_norm_enemy_list)

# Randomize the boss list
shuffle_boss_enemy_list = [x for x in Enemies.boss_enemy_list]
random.shuffle(shuffle_boss_enemy_list)


# player stats
player_hp = 250
player_mana = 150
player_mana_potion = random.randint(1,10)
player_hp_potion = random.randint(0,10)
player_physical_atk = 200
player_base_magical_atk = 65
player_score = 0
player_max_hp = 250
player_max_mana = 150


rand_reward = random.randint(0, len(Enemies.item_list) - 1)
reward_item = Enemies.item_list[rand_reward]
reward_item = reward_item.in_inventory + 1



is_playing = True
while is_playing:

    is_fullfilled_req_battles = False

    # ------ BATTTLE FOR NORMAL ENEMIES ------------
    for battling_normal_enemy in shuffle_norm_enemy_list:
        if player_hp > 0:
            print('')
            Functions.print_player_status(player_hp, player_mana, player_hp_potion, player_mana_potion, player_score)
            print('Enemy Type: ' + str(battling_normal_enemy.type))
            print('Enemy Health: ' + str(battling_normal_enemy.health))
            print('1')
            Functions.print_actions()
            # This variable will be used as enemy health during the battle
            # This is needed because so we don't change the default values, cause this gets reset every enemy
            damaged_enemy = battling_normal_enemy.health

        # This will loop as long the damaged_enemy is above 0
        is_defeated = False
        while not is_defeated:
            # makes the player_hp to cur_player_hp
            cur_player_hp = player_hp
            cur_player_mp = player_mana
            cur_player_hp_potion = player_hp_potion
            cur_player_mp_potion = player_mana_potion
            cur_player_score = player_score

            # Default damage to enemy
            dealt_damage = 0

            player_attacked = False
            while not player_attacked:
                # Gets user Input
                print('test')
                print('SYSTEM: CHOOSE A ACTION')
                player_action = Functions.main_input_system()

                # Player Attack
                # physical attack
                if player_action == 'LT':
                    damaged_enemy = Functions.physical_atk(player_physical_atk, damaged_enemy)
                    dealt_damage = player_physical_atk
                    player_attacked = True

                # magical attack
                if player_action == 'RT':
                    # IF_1 Checks if the user have enough mana
                    if player_mana > 50:
                        print('DEBUG: HAVE THE REQUIRED MANA')
                        Functions.print_magic_atk()
                        # W1 Will loop until the user choose a right option
                        waiting_magical_atk = True
                        while waiting_magical_atk:
                            possible_magic_atk = ['Q', 'W']
                            used_magic_atk = input('➤ ').upper()
                            # IF_2 checks if the user input is in possible inputs
                            if used_magic_atk in possible_magic_atk:
                                # IF_3 checks if what attack user used
                                if used_magic_atk == 'Q':
                                    damaged_enemy = Functions.magic_atk(player_base_magical_atk,
                                                        'FIRE',
                                                        battling_normal_enemy.magical_resistance,
                                                        battling_normal_enemy.magical_weakness,
                                                        battling_normal_enemy.health)
                                    damaged_enemy = round(damaged_enemy,0)
                                    cur_player_mp = cur_player_mp - 40
                                    dealt_damage = Functions.magically_damage_done
                                    waiting_magical_atk = False
                                    player_attacked = True

                                # IF_3 checks if what attack user used
                                elif used_magic_atk == 'W':
                                    damaged_enemy = Functions.magic_atk(player_base_magical_atk,
                                                        'WATER',
                                                        battling_normal_enemy.magical_resistance,
                                                        battling_normal_enemy.magical_weakness,
                                                        battling_normal_enemy.health)
                                    damaged_enemy = round(damaged_enemy, 0)
                                    cur_player_mp = cur_player_mp - 40
                                    dealt_damage = Functions.magically_damage_done
                                    waiting_magical_atk = False
                                    player_attacked = True
                            # IF_2 checks if the user input is in possible inputs
                            else:
                                print('SYSTEM: INVALID INPUT')
                                waiting_magical_atk = True
                    # IF_1 Checks if user have enough mana
                    elif player_mana < 50:
                        print('SYSTEM: YOU DON\'T HAVE ENOUGH MANA')

                # drink health potion
                if player_action == 'A':
                    if cur_player_hp_potion > 0:

                        if cur_player_hp >= player_max_hp:
                            print('SYSTEM: YOU HAVE MAX HEALTH')
                            print('-----------------------------------------------------------')
                            player_attacked = False

                        if cur_player_hp < player_max_hp:
                            cur_player_hp = Functions.drink_health_potion(cur_player_hp, player_max_hp)
                            print('HEALING.....')
                            time.sleep(1)
                            print('SYSTEM: HEALED FOR 50 HP')
                            print('SYSTEM: YOU\'RE CURRENT HEALTH IS: ' + str(cur_player_hp))
                            print('-----------------------------------------------------------')
                            cur_player_hp_potion = cur_player_hp_potion - 1
                            player_attacked = False

                    else:
                        print('SYSTEM: YOU DON\'T HAVE ENOUGH HP POTIONS')
                        print('-----------------------------------------------------------')
                        player_attacked = False

                # drink mana potion
                if player_action == 'B':
                    if cur_player_mp_potion > 0:

                        if cur_player_mp >= player_max_mana:
                            print('SYSTEM: YOU HAVE MAX MANA')
                            print('-----------------------------------------------------------')
                            player_attacked = False

                        if cur_player_mp < player_max_mana:
                            cur_player_mp = Functions.drink_mana_potion(cur_player_mp, player_max_mana)
                            print('ABSORBING MANA......')
                            time.sleep(1)
                            print('SYSTEM: YOU\'RE CURRENT MANA IS: ' + str(cur_player_mp))
                            print('-----------------------------------------------------------')
                            cur_player_mp_potion = cur_player_mp_potion - 1
                            player_attacked = False


                    else:
                        print('SYSTEM: YOU DON\'T HAVE ENOUGH MP POTIONS')
                        print('-----------------------------------------------------------')
                        player_attacked = False

                # appraise
                if player_action == 'X':
                    Functions.print_enemy_stats(battling_normal_enemy.magical_resistance,
                                                battling_normal_enemy.magical_weakness,
                                                battling_normal_enemy.physical_atk,
                                                battling_normal_enemy.magical_atk)

                # items
                if player_action == 'Y':
                    Functions.print_items()
                    waiting_choosing_a_item = True
                    while waiting_choosing_a_item:
                        possible_item = ['Q', 'W', 'E', 'X']
                        used_item = input('➤ ').upper()

                        if used_item in possible_item:
                            if Enemies.max_hp_potion.in_inventory > 0:
                                if used_item == 'Q':
                                    cur_player_hp = player_max_hp
                                    print('HEALED TO MAX HP')
                                    print('YOUR\'E CURRENT HP IS: ' + str(cur_player_hp))
                                    waiting_choosing_a_item = False
                                    player_attacked = False
                                    Enemies.max_hp_potion.in_inventory = Enemies.max_hp_potion.in_inventory - 1
                            else:
                                print('YOU DON\'T HAVE THIS ITEM')

                            if Enemies.max_mp_potion.in_inventory > 0:
                                if used_item == 'W':
                                    cur_player_mp = player_max_mana
                                    print('REGENERATED TO MAX MP')
                                    print('YOUR\'E CURRENT HP IS: ' + str(cur_player_mp))
                                    waiting_choosing_a_item = False
                                    player_attacked = False
                                    Enemies.max_mp_potion.in_inventory = Enemies.max_mp_potion.in_inventory - 1
                            else:
                                print('YOU DON\'T HAVE THIS ITEM')

                            if Enemies.instant_kill_potion.in_inventory > 0:
                                if used_item == 'E':
                                    damaged_enemy = 0
                                    waiting_choosing_a_item = False
                                    player_attacked = True
                                    dealt_damage = battling_normal_enemy.health
                                    Enemies.instant_kill_potion.in_inventory = Enemies.instant_kill_potion.in_inventory - 1
                            else:
                                print('YOU DON\'T HAVE THIS ITEM')

                            if used_item == 'X':
                                waiting_choosing_a_item = False

                        else:
                            print('SYSTEM: INVALID INPUT')
                            waiting_choosing_a_item = True

            if player_attacked:
                    # Player Attacking Sequence
                    dealt_damage = round(dealt_damage,0)
                    print('')
                    print('Attacking....')
                    time.sleep(1)
                    print('You Dealt: ' + str(dealt_damage))
                    print('Enemy Health ' + str(damaged_enemy))
                    print('')

            # Enemy Attacking Sequence and GUI
            # This if-else statement make sure the enemy is will be able to attack if it's alive
            if damaged_enemy > 0:
                # This list contains possibles attacks of the enemy which is physical and magical
                enemy_atk = [battling_normal_enemy.physical_atk, battling_normal_enemy.magical_atk]
                # DEBUG: SEE HOW MUCH DAMAGE IT SHOULD DO [PHYSCIAL, MAGICAL]
                # print(enemy_atk)
                # Randomized the enemy attack type
                enemy_atk_type = random.randint(0, 1)
                print('Your Opponent is attacking...')

                # if the enemy_attack_type spits out a 2 it will be physical attack
                if enemy_atk_type == 0:
                    time.sleep(1)
                    # this will be the damaged player hp
                    cur_player_hp = Functions.enemy_attacking(enemy_atk[0], cur_player_hp)
                    print('Your Enemy Dealt Physical Damage to you : ' + str(battling_normal_enemy.physical_atk))
                    print('Your HP: ' + str(cur_player_hp))
                    print('')

                # if the enemy_attack_type spits out a 1 it will be magical attack
                elif enemy_atk_type == 1:
                    time.sleep(1)
                    # this will be the damaged player hp
                    cur_player_hp = Functions.enemy_attacking(enemy_atk[1], cur_player_hp)
                    print('Your Enemy Dealt Magical Damage to you : ' + str(battling_normal_enemy.magical_atk))
                    print('Your HP: ' + str(cur_player_hp))
                    print('')

                # Updated GUI
                Functions.print_player_status(cur_player_hp,
                                              cur_player_mp,
                                              cur_player_hp_potion,
                                              cur_player_mp_potion,
                                              cur_player_score)

                print('Enemy Type: ' + str(battling_normal_enemy.type))
                print('Enemy Health: ' + str(damaged_enemy))
                print('2')
                Functions.print_actions()

            # if the enemy hp drops down below 0 the for loop
            if damaged_enemy <= 0:
                cur_player_score = cur_player_score + 1
                print('SYSTEM: ENEMY DEFEATED!!')
                battling_normal_enemy.health = battling_normal_enemy.health + random.randint(35, 60)
                battling_normal_enemy.physical_atk = battling_normal_enemy.physical_atk + random.randint(10, 25)
                battling_normal_enemy.magical_atk = battling_normal_enemy.magical_atk + random.randint(5, 15)
                is_defeated = True


            # makes the cur_player_hp to player_hp
            player_hp = cur_player_hp
            player_mana = cur_player_mp
            player_hp_potion = cur_player_hp_potion
            player_mana_potion = cur_player_mp_potion
            player_score = cur_player_score


    # -------- TRANSITION BETWEEN NORMAL BATTLE TO BOSS BATTLE ------
    is_fullfilled_req_battles = True

    # ---------BOSS BATTLE --------
    while is_fullfilled_req_battles:
        # battle for boss enemies:
        boss_randomizer = random.randint(0,1)
        cur_boss = (shuffle_boss_enemy_list[boss_randomizer])

        if player_hp > 0:
            print('')
            Functions.print_player_status(player_hp, player_mana, player_hp_potion, player_mana_potion, player_score)
            print('Enemy Type: ' + str(cur_boss.type))
            print('Enemy Health: ' + str(cur_boss.health))
            print('1')
            Functions.print_actions()
            # This variable will be used as enemy health during the battle
            # This is needed because so we don't change the default values, cause this gets reset every enemy
            damaged_enemy = cur_boss.health

        # This will loop as long the damaged_enemy is above 0
        is_defeated = False
        while not is_defeated:
            # makes the player_hp to cur_player_hp
            cur_player_hp = player_hp
            cur_player_mp = player_mana
            cur_player_hp_potion = player_hp_potion
            cur_player_mp_potion = player_mana_potion
            cur_player_score = player_score


            # Default damage to enemy
            dealt_damage = 0

            player_attacked = False
            while not player_attacked:
                # Gets user Input
                print('SYSTEM: CHOOSE A ACTION')
                player_action = Functions.main_input_system()

                # Player Attack
                # physical attack
                if player_action == 'LT':
                    damaged_enemy = Functions.physical_atk(player_physical_atk, damaged_enemy)
                    dealt_damage = player_physical_atk
                    player_attacked = True

                # magical attack
                if player_action == 'RT':
                    # IF_1 Checks if the user have enough mana
                    if player_mana > 50:
                        print('DEBUG: HAVE THE REQUIRED MANA')
                        Functions.print_magic_atk()
                        # W1 Will loop until the user choose a right option
                        waiting_magical_atk = True
                        while waiting_magical_atk:
                            possible_magic_atk = ['Q', 'W']
                            used_magic_atk = input('➤ ').upper()
                            # IF_2 checks if the user input is in possible inputs
                            if used_magic_atk in possible_magic_atk:
                                # IF_3 checks if what attack user used
                                if used_magic_atk == 'Q':
                                    damaged_enemy = Functions.magic_atk(player_base_magical_atk,
                                                        'FIRE',
                                                        cur_boss.magical_resistance,
                                                        cur_boss.magical_weakness,
                                                        cur_boss.health)
                                    damaged_enemy = round(damaged_enemy,0)
                                    cur_player_mp = cur_player_mp - 40
                                    dealt_damage = Functions.magically_damage_done
                                    waiting_magical_atk = False
                                    player_attacked = True

                                # IF_3 checks if what attack user used
                                elif used_magic_atk == 'W':
                                    damaged_enemy = Functions.magic_atk(player_base_magical_atk,
                                                        'WATER',
                                                        cur_boss.magical_resistance,
                                                        cur_boss.magical_weakness,
                                                        cur_boss.health)
                                    damaged_enemy = round(damaged_enemy, 0)
                                    cur_player_mp = cur_player_mp - 40
                                    dealt_damage = Functions.magically_damage_done
                                    waiting_magical_atk = False
                                    player_attacked = True
                            # IF_2 checks if the user input is in possible inputs
                            else:
                                print('SYSTEM: INVALID INPUT')
                                waiting_magical_atk = True
                    # IF_1 Checks if user have enough mana
                    elif player_mana < 50:
                        print('SYSTEM: YOU DON\'T HAVE ENOUGH MANA')

                # drink health potion
                if player_action == 'A':
                    if cur_player_hp_potion > 0:

                        if cur_player_hp >= player_max_hp:
                            print('SYSTEM: YOU HAVE MAX HEALTH')
                            print('-----------------------------------------------------------')
                            player_attacked = False

                        if cur_player_hp < player_max_hp:
                            cur_player_hp = Functions.drink_health_potion(cur_player_hp, player_max_hp)
                            print('HEALING.....')
                            time.sleep(1)
                            print('SYSTEM: HEALED FOR 50 HP')
                            print('SYSTEM: YOU\'RE CURRENT HEALTH IS: ' + str(cur_player_hp))
                            print('-----------------------------------------------------------')
                            cur_player_hp_potion = cur_player_hp_potion - 1
                            player_attacked = False

                    else:
                        print('SYSTEM: YOU DON\'T HAVE ENOUGH HP POTIONS')
                        print('-----------------------------------------------------------')
                        player_attacked = False

                # drink mana potion
                if player_action == 'B':
                    if cur_player_mp_potion > 0:

                        if cur_player_mp >= player_max_mana:
                            print('SYSTEM: YOU HAVE MAX MANA')
                            print('-----------------------------------------------------------')
                            player_attacked = False

                        if cur_player_mp < player_max_mana:
                            cur_player_mp = Functions.drink_mana_potion(cur_player_mp, player_max_mana)
                            print('ABSORBING MANA......')
                            time.sleep(1)
                            print('SYSTEM: YOU\'RE CURRENT MANA IS: ' + str(cur_player_mp))
                            print('-----------------------------------------------------------')
                            cur_player_mp_potion = cur_player_mp_potion - 1
                            player_attacked = False


                    else:
                        print('SYSTEM: YOU DON\'T HAVE ENOUGH MP POTIONS')
                        print('-----------------------------------------------------------')
                        player_attacked = False

                # appraise
                if player_action == 'X':
                    Functions.print_enemy_stats(cur_boss.magical_resistance,
                                                cur_boss.magical_weakness,
                                                cur_boss.physical_atk,
                                                cur_boss.magical_atk)

                # items
                if player_action == 'Y':
                    Functions.print_items()
                    waiting_choosing_a_item = True
                    while waiting_choosing_a_item:
                        possible_item = ['Q', 'W', 'E', 'X']
                        used_item = input('➤ ').upper()

                        if used_item in possible_item:
                            if Enemies.max_hp_potion.in_inventory > 0:
                                if used_item == 'Q':
                                    cur_player_hp = player_max_hp
                                    print('HEALED TO MAX HP')
                                    print('YOUR\'E CURRENT HP IS: ' + str(cur_player_hp))
                                    waiting_choosing_a_item = False
                                    player_attacked = False
                                    Enemies.max_hp_potion.in_inventory = Enemies.max_hp_potion.in_inventory - 1
                            else:
                                print('YOU DON\'T HAVE THIS ITEM')

                            if Enemies.max_mp_potion.in_inventory > 0:
                                if used_item == 'W':
                                    cur_player_mp = player_max_mana
                                    print('REGENERATED TO MAX MP')
                                    print('YOUR\'E CURRENT HP IS: ' + str(cur_player_mp))
                                    waiting_choosing_a_item = False
                                    player_attacked = False
                                    Enemies.max_mp_potion.in_inventory = Enemies.max_mp_potion.in_inventory - 1
                            else:
                                print('YOU DON\'T HAVE THIS ITEM')

                            if Enemies.instant_kill_potion.in_inventory > 0:
                                if used_item == 'E':
                                    damaged_enemy = 0
                                    waiting_choosing_a_item = False
                                    player_attacked = True
                                    dealt_damage = cur_boss.health - random.randint(50, 100)
                                    Enemies.instant_kill_potion.in_inventory = Enemies.instant_kill_potion.in_inventory - 1
                            else:
                                print('YOU DON\'T HAVE THIS ITEM')

                            if used_item == 'X':
                                waiting_choosing_a_item = False

                        else:
                            print('SYSTEM: INVALID INPUT')
                            waiting_choosing_a_item = True

            if player_attacked:
                    # Player Attacking Sequence
                    dealt_damage = round(dealt_damage,0)
                    print('')
                    print('Attacking....')
                    time.sleep(1)
                    print('You Dealt: ' + str(dealt_damage))
                    print('Enemy Health ' + str(damaged_enemy))
                    print('')

            # Enemy Attacking Sequence
            # This if-else statement make sure the enemy is will be able to attack if it's alive
            if damaged_enemy > 0:
                # This list contains possibles attacks of the enemy which is physical and magical
                enemy_atk = [cur_boss.physical_atk, cur_boss.magical_atk]
                # DEBUG: SEE HOW MUCH DAMAGE IT SHOULD DO [PHYSCIAL, MAGICAL]
                # print(enemy_atk)
                # Randomized the enemy attack type
                enemy_atk_type = random.randint(0, 1)
                print('Your Opponent is attacking...')

                # if the enemy_attack_type spits out a 2 it will be physical attack
                if enemy_atk_type == 0:
                    time.sleep(1)
                    # this will be the damaged player hp
                    cur_player_hp = Functions.enemy_attacking(enemy_atk[0], cur_player_hp)
                    print('Your Enemy Dealt Physical Damage to you : ' + str(cur_boss.physical_atk))
                    print('Your HP: ' + str(cur_player_hp))
                    print('')

                # if the enemy_attack_type spits out a 1 it will be magical attack
                elif enemy_atk_type == 1:
                    time.sleep(1)
                    # this will be the damaged player hp
                    cur_player_hp = Functions.enemy_attacking(enemy_atk[1], cur_player_hp)
                    print('Your Enemy Dealt Magical Damage to you : ' + str(cur_boss.magical_atk))
                    print('Your HP: ' + str(cur_player_hp))
                    print('')



                # Updated GUI
                Functions.print_player_status(cur_player_hp, player_mana, player_hp_potion, player_mana_potion,
                                              player_score)
                print('Enemy Type: ' + str(cur_boss.type))
                print('Enemy Health: ' + str(damaged_enemy))
                print('2')
                Functions.print_actions()

            # if the enemy hp drops down below 0 the for loop
            elif damaged_enemy <= 0:
                player_score += 5
                print('SYSTEM: ENEMY DEFEATED!!')
                cur_boss.health = cur_boss.health + random.randint(50,100)
                cur_boss.magical_atk = cur_boss.magical_atk + random.randint(40, 70)
                cur_boss.physical_atk = cur_boss.physical_atk + random.randint(50,80)
                is_defeated = True

            # makes the cur_player_hp to player_hp
            player_hp = cur_player_hp
            player_mana = cur_player_mp
            player_hp_potion = cur_player_hp_potion
            player_mana_potion = cur_player_mp_potion
            player_score = cur_player_score

        rand_reward = random.randint(0, len(Enemies.item_list) - 1)
        reward_item = Enemies.item_list[rand_reward]
        reward_item = reward_item.in_inventory + 1

        is_fullfilled_req_battles = False

























