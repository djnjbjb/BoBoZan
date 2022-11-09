import random
import skill

class Hero:
    name = ""
    max_hp = 0
    max_mp = 0
    hp = 0
    mp = 0
    skills = []
    skill_weights = None

    def get_valid_skills(self):
        valid_skills = []
        for skill in self.skills:
            if (skill.mp <= self.mp):
                valid_skills.append(skill)
        return valid_skills

    def choose_random_skill(self):
        valid_skills = self.get_valid_skills()
        skill = random.choice(valid_skills)
        return skill

    def choose_random_skill_with_weights(self):
        if (self.skill_weights == None):
            return self.choose_random_skill()
        valid_skills = self.get_valid_skills()
        weights = []
        for s in valid_skills:
            w = valid_skills.index(s)
            weights.append(self.skill_weights[w])
        skill = random.choices(valid_skills, weights=tuple(weights), k=1)
        return skill[0]


    def be_damage(self, damage):
        self.hp -= damage
        if (self.hp < 0):
            self.hp = 0
    
    def consume_mp(self, mp):
        self.mp -= mp
        if (self.mp < 0):
            self.mp = 0
            raise Exception("mp不够")
    
    def add_mp(self, mp):
        self.mp += mp
        if (self.mp > self.max_mp):
            self.mp = self.max_mp

def print_valid_skills(valid_skills):
    text = "["
    for skill in valid_skills:
        text += skill.name + ","
    text += "]"
    print(text)

def hero1_init():
    hero1 = Hero()
    hero1.name = "小明"
    hero1.max_hp = 900
    hero1.max_mp = 40
    hero1.hp = 900
    hero1.mp = 0
    hero1.skills = [skill.attack, skill.defence, skill.restore, skill.super_attack]
    return hero1


def hero2_init():
    hero2 = Hero()
    hero2.name = "Tom"
    hero2.max_hp = 900
    hero2.max_mp = 40
    hero2.hp = 900
    hero2.mp = 0
    hero2.skills = [skill.attack, skill.defence, skill.restore, skill.super_attack]
    return hero2

#---------------------------------------------------------------

def hero_better_attack_init():
    hero = Hero()
    hero.name = "攻击强"
    hero.max_hp = 900
    hero.max_mp = 40
    hero.hp = 900
    hero.mp = 0
    hero.skills = [skill.attack_150, skill.defence, skill.restore, skill.super_attack]
    return hero

def hero_better_defence_init():
    hero = Hero()
    hero.name = "防御强"
    hero.max_hp = 1150
    hero.max_mp = 40
    hero.hp = hero.max_hp
    hero.mp = 0
    hero.skills = [skill.attack, skill.defence_150, skill.restore, skill.super_attack]
    return hero

def hero_defence_no_cost_init():
    hero = Hero()
    hero.name = "防御不耗蓝"
    hero.max_hp = 900
    hero.max_mp = 40
    hero.hp = 900
    hero.mp = 0
    hero.skills = [skill.attack, skill.defence_no_cost, skill.restore, skill.super_attack]
    return hero

def hero_better_restore_init():
    hero = Hero()
    hero.name = "回复强"
    hero.max_hp = 900
    hero.max_mp = 40
    hero.hp = 900
    hero.mp = 0
    hero.skills = [skill.attack, skill.defence, skill.restore_more, skill.super_attack]
    return hero

def hero_more_hp_init():
    hero = Hero()
    hero.name = "血量多"
    hero.max_hp = 1100
    hero.max_mp = 40
    hero.hp = 1100
    hero.mp = 0
    hero.skills = [skill.attack, skill.defence, skill.restore, skill.super_attack]
    return hero

#--------------------------------------------------------

def hero_strategy_more_attack_init():
    hero = Hero()
    hero.name = "更多攻击"
    hero.max_hp = 900
    hero.max_mp = 40
    hero.hp = hero.max_hp
    hero.mp = 0
    hero.skills = [skill.attack, skill.defence, skill.restore, skill.super_attack]
    hero.skill_weights = [8, 1, 1, 1]
    return hero

def hero_strategy_more_defence_init():
    hero = Hero()
    hero.name = "更多防御"
    hero.max_hp = 900
    hero.max_mp = 40
    hero.hp = hero.max_hp
    hero.mp = 0
    hero.skills = [skill.attack, skill.defence, skill.restore, skill.super_attack]
    hero.skill_weights = [1, 8, 1, 1]
    return hero

def hero_strategy_more_super_attack_init():
    hero = Hero()
    hero.name = "更多强力攻击"
    hero.max_hp = 900
    hero.max_mp = 40
    hero.hp = hero.max_hp
    hero.mp = 0
    hero.skills = [skill.attack, skill.defence, skill.restore, skill.super_attack]
    hero.skill_weights = [1, 1, 1, 8]
    return hero


# test
if __name__ == '__main__':
    for i in range(0,100):
        hero = hero_strategy_more_attack_init()
        hero.mp = hero.max_mp
        print(hero.choose_random_skill_with_weights().name)
        
