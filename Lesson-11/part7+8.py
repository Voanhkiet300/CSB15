from random import *

Skill1 = {"Name": "Tackle", "Minimum level": 1, "Damage": 5, "Hit rate": 0.3}
Skill2 = {"Name": "Quick Attack", "Minimum level": 2, "Damage": 3, "Hit rate": 0.5}
Skill3 = {"Name": "Strong Kick", "Minimum level": 4, "Damage": 9, "Hit rate": 0.2}
Skill = {}
# phan 7:
def phan7():
    print("skill 1:", Skill1["Name"])
    print("skill 2:", Skill2["Name"])
    print("skill 3:", Skill3["Name"])

# phan 8:
def phan8():
    level = randint(1, 4)
    print("Your level is:", level)
    print("skill 1:", Skill1["Name"])
    print("skill 2:", Skill2["Name"])
    print("skill 3:", Skill3["Name"])
    a = input("Choose skill by number: ")

    def check_skill(a, level):
        global Required_level
        if a == "1":
            Skill.update(Skill1)
            print("\nYou chose", Skill["Name"])
            Required_level = 1
            return True
        elif a == "2":
            Skill.update(Skill2)
            print("\nYou chose", Skill2["Name"])
            Required_level = 2
            return True
        elif a == "3":
            Skill.update(Skill3)
            print("\nYou chose", Skill3["Name"])
            Required_level = 4
            return True
        else:
            print("Invalid input")
            return False
        

    def check_Hit_rate(Skill):
        if random() <= Skill["Hit rate"]:
            print("Damage:", Skill["Damage"])
        else:
            print("Missed")


    def check_level(Skill, level, Required_level):
        if level >= Required_level:
            check_Hit_rate(Skill)
        else:
            print("Cannot deploy. Required level", Required_level)

    if check_skill(a, level):
        check_level(Skill, level, Required_level)









n = input("Nhập phần muốn chạy: ")
while not n.isdigit():
    n = int(input("Nhập lại bài muốn chạy: "))
while int(n) > 8 or  int(n) < 7:
    n = int(input("Nhập lại bài muốn chạy: "))
n = int(n)
if n == 1:
    phan7()
else:
    phan8()