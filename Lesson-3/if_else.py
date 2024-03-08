import random
# # age
# age = int(input("How old are you? "))

# if (age <= 0):
#     print("haven't born yet")
# elif (age < 5):
#     print("baby")
# elif (age < 13):
#     print("children")
# elif (age < 20):
#     print("teenager")
# elif (age < 65):
#     print("adult")
# else:
#     print("elderly")




# keo bua bao

skillList = ["bua" , "bao", "keo"]

userSkill = input("Enter your skill(bua/bao/keo): ")


machineSkill = random.choice(skillList)

def checkSkill(user, machine):
    if (userSkill == "bua"):
        print("You choose:\t\t bua")
        print("Computer choose:\t", machine)
        if (machine == "bua"):
            print("Draw")
        elif (machine == "keo"):
            print("You win")
        else:
            print("You lose")
    
    if (userSkill == "keo"):
        print("You choose:\t\t keo")
        print("Computer choose:\t", machine)
        if (machine == "keo"):
            print("Draw")
        elif (machine == "bao"):
            print("You win")
        else:
            print("You lose")
    
    if (userSkill == "bao"):
        print("You choose:\t\t bao")
        print("Computer choose:\t", machine)
        if (machine == "bao"):
            print("Draw")
        elif (machine == "bua"):
            print("You win")
        else:
            print("You lose")

checkSkill(userSkill, machineSkill)