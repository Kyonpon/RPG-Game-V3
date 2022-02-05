import random

def print_player_status(health, mana, health_potion, mana_potions, score):
    print('----------------------------------------------------------')
    print('Player Status' + '                              ' + 'Player Score: ' + str(score))
    print('Player HP: ' + str(health) + '                             ' + 'HP Potions: ' + str(health_potion))
    print('Player MP: ' + str(mana) + '                             ' + 'MP Potions: ' + str(mana_potions))
    print('----------------------------------------------------------')


def print_actions():
    print('----------------------------------------------------------')
    print('[LT] - Physical Attack            [RT] - Magical Attacks')
    print('[A] - Drink Health Potion         [B] - Drink Mana Potion')
    print('[X] - Flee                        [Y] - Items')
    print('----------------------------------------------------------')
    print('SYSTEM: CHOOSE A ACTION')


def print_magic_atk():
    print('-----------------------------------------------------------')
    print('[Q] - Fire Magic                  [W] - Water Magic')
    print('-----------------------------------------------------------')
    print('SYSTEM: CHOOSE AN ATTACK')


def print_items():
    print('-----------------------------------------------------------')
    print('[Q] - Instant Health Potion       [W] - Instant Mana Potion')
    print('[E] - Instant Kill Potion')
    print('-----------------------------------------------------------')
    print('SYSTEM: CHOOSE A ITEMS')


def physical_atk(user_physical_atk, enemy_hp):
    physically_damage_done = user_physical_atk
    opponent_hp = enemy_hp - physically_damage_done

    if opponent_hp < 0:
        opponent_hp = 0

    return opponent_hp


magically_damage_done = 0


def magic_atk(user_magical_atk, user_magical_element_atk, enemy_resistance, enemy_weakness, enemy_hp):
    global magically_damage_done
    # if statement tree the will check if the enemy can resist the attack or not
    # nothing will happen if user magic attack is the same enemy magic resistance
    if enemy_resistance == user_magical_element_atk:
        opponent_hp = enemy_hp

    # the magic attack will be randomly multiplied if the user uses the same magic element that enemy is weak to
    elif enemy_weakness == user_magical_element_atk:
        # this determines the range of the multiplier
        user_magic_atk_multiplyer = random.uniform(.50, .75)
        # The formula is user base magical atk plus user magical attack multiplied by the random multiplier
        magically_damage_done = user_magical_atk + (user_magical_atk * user_magic_atk_multiplyer)
        opponent_hp = enemy_hp - magically_damage_done

    # if the enemy magic attack is not the weakness of the enemy, or it is not also immune the enemy will receive the
    # user magical base damage
    else:
        magically_damage_done = user_magical_atk
        opponent_hp = enemy_hp - magically_damage_done

    # this make sure the enemy hp won't go below 0
    if opponent_hp < 0:
        opponent_hp = 0

    return round(opponent_hp, 0)


def drink_health_potion(user_health, user_max_health):
    global healed_user
    if user_health < user_max_health and user_health > 0:
        healed_user = user_health + 50

    elif user_health > user_max_health:
        print('SYSTEM: YOU HAVE MAX HEALTH')

    return healed_user


def drink_mana_potion(user_mana, user_max_mana):
    global replenished_mana
    if user_mana < user_max_mana:
        replenished_mana = user_mana + 50

    elif user_mana > user_max_mana:
        print('SYSTEM: YOU HAVE MAX MANA')

    return replenished_mana

def check_if_the_enemy_health_is_being_changed_permantly():
    b_enemy_name =[]
    before_damage = []

    for current_enemy in shuffle_enemy_list:
        before_damage.append(current_enemy.health)
        b_enemy_name.append(current_enemy.type)

    a_enemy_name = []
    after_damaged = []

    for current_enemy in shuffle_enemy_list:
        damaged = current_enemy.health - 10
        after_damaged.append(damaged)
        a_enemy_name.append(current_enemy.type)

    r_enemy_name = []
    real_health = []

    for current_enemy in shuffle_enemy_list:
        real_health.append(current_enemy.health)
        r_enemy_name.append(current_enemy.type)

    print('type ' + str(b_enemy_name))
    print('this is the health before damaged ' + str(before_damage))
    print('type ' + str(a_enemy_name))
    print('this is the health after damaged ' + str(after_damaged))
    print('type ' + str(r_enemy_name))
    print('this is the real health ' + str(real_health))

def main_input_system():
    waiting_input1 = True
    while waiting_input1:
        input1 = input('➤ ').upper()
        possible_input1 = ['LT', 'RT', 'A', 'B', 'X', 'Y']

        if input1 in possible_input1:

            if input1 == 'LT':
                return 'LT'

            elif input1 == 'RT':
                return 'RT'

            elif input1 == 'A':
                return 'A'

            elif input1 == 'B':
                return 'B'

            elif input1 == 'X':
                return 'X'

            elif input1 == 'Y':
                return 'Y'

        else:
            print('SYSTEM: INVALID INPUT')
            waiting_input1 = True


def enemy_attacking(enemy_atk, player_health):
    damaged_player = player_health - enemy_atk

    if damaged_player > 0:
        return damaged_player
    elif damaged_player <= 0:
        return damaged_player


