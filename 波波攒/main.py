import random
import math
import skill
from hero import *

def Battle(hero1, hero2):
    hero1_skill = hero1.choose_random_skill_with_weights()
    hero2_skill = hero2.choose_random_skill_with_weights()

    hero1.consume_mp(hero1_skill.mp) 
    hero1.add_mp(hero1_skill.mp_restore)
    
    hero2.consume_mp(hero2_skill.mp)
    hero2.add_mp(hero2_skill.mp_restore)

    #交互技能
    if (hero1_skill.damage > 0 and hero1_skill.ignore_defence == True):
        hero2.be_damage(hero1_skill.damage)
    elif (hero1_skill.damage > 0):
        damage = max(hero1_skill.damage - hero2_skill.defence_power, 0)
        hero2.be_damage(damage)

    if (hero2_skill.damage > 0 and hero2_skill.ignore_defence == True):
        hero1.be_damage(hero2_skill.damage)
    elif (hero2_skill.damage > 0):
        damage = max(hero2_skill.damage - hero1_skill.defence_power, 0)
        hero1.be_damage(damage)

    return (hero1_skill, hero2_skill)


if __name__ == '__main__':
    hero1_win_count = 0
    hero2_win_count = 0
    draw_count = 0
    total_count = 1000
    if_print = True
    if (total_count > 1): if_print = False
    for i in range(0, total_count):
        hero1 = hero_strategy_more_super_attack_init()
        hero2 = hero_strategy_more_attack_init()
        while(True):
            if (hero1.hp == 0 and hero2.hp == 0):
                draw_count+=1
            if (hero1.hp == 0 and hero2.hp > 0):
                hero2_win_count += 1
            if (hero2.hp == 0 and hero1.hp > 0):
                hero1_win_count += 1
            if (hero2.hp == 0 or hero1.hp == 0):
                break
            
            (hero1_skill, hero2_skill) = Battle(hero1, hero2)
            if (if_print):
                print(f"【{hero1.name}】使用技能【{hero1_skill.name}】，【{hero2.name}】使用技能【{hero2_skill.name}】。战斗结果：{{{hero1.name},hp:{hero1.hp},mp:{hero1.mp}}}，{{{hero2.name},hp:{hero2.hp},mp:{hero2.mp}}}")
    print(f"hero1 win: {hero1_win_count}")
    print(f"hero2 win: {hero2_win_count}")
    print(f"draw: {draw_count}")
    hero1_win_rate = (hero1_win_count + draw_count/2)/total_count
    print(f"hero1 win rate: {hero1_win_rate}")
    print(f"hero2 win rate: {1 - hero1_win_rate}")
