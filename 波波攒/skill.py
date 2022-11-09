class Skill:
    name = ""
    damage = 0
    mp = 0
    mp_restore = 0
    defence_power = 0
    ignore_defence = False
    def __init__(self, name = ""):
        name = name
        return

attack = Skill()
attack.name = "攻击"
attack.mp = 10
attack.damage = 100

defence = Skill()
defence.name = "防御"
defence.mp = 5
defence.damage = 30
defence.defence_power = 100

restore = Skill()
restore.name = "攒气"
restore.mp = 0
restore.mp_restore = 10

super_attack = Skill()
super_attack.name = "强力攻击"
super_attack.mp = 20
super_attack.damage = 100
super_attack.ignore_defence = True

#--------------------------
#--------------------------

attack_150 = Skill()
attack_150.name = "攻击(150)"
attack_150.mp = 10
attack_150.damage = 150

defence_150 = Skill()
defence_150.name = "防御(150)"
defence_150.mp = 5
defence_150.defence_power = 150

defence_no_cost = Skill()
defence_no_cost.name = "防御(不耗蓝)"
defence_no_cost.mp = 0
defence_no_cost.defence_power = 100

restore_more = Skill()
restore_more.name = "攒气(更多)"
restore_more.mp = 0
restore_more.mp_restore = 15