import random
import time
import math 

List = []
RoleList = []
SUSmetre = []

print("welcome!")
print("in this, you can play mafia!")
choice = input("So, whats your name: ")
List.append(choice)
player = choice
number = int(input("How many other players(mininum is 3): "))

for i in range(number):
    choice = input("name the player: ")
    List.append(choice)

number += 1

mafia = number/3
mafia = int(mafia)

innocent = number - mafia

doctor = 0
if number > 5:
    innocent = innocent - 1
    doctor = 1
    wizard = 0

for i in range(innocent):
    RoleList.append("innocent")

for i in range(mafia):
    RoleList.append("mafia")

for i in range(doctor):
    RoleList.append("doctor")
    #RoleList.append("wizard")

if "doctor" in RoleList:
    innocent = innocent + 1

if "wizard" in RoleList:
    innocent = innocent + 1

for i in range(number):
    SUSmetre.append(0)

print(RoleList)

random.shuffle(RoleList)

print(RoleList)
#print(RoleList)
confirm_kill = False
kill = 0
DOC_protect = 0
WIZ_identify = 0
stop = len(List)
stop = stop - 1
discussion = number
wait = 0
chance = 0
chance2 = 0
chance3 = 0

odds = 0

largest = 0

wizard_check = False
WIZ_target = False
WIZ_accuse = False
WIZ_reveal = False

def wizard_check(chance):
    while wizard_check != True:    
        chance = random.randint(0, stop)
        if RoleList[chance] == "wizard":
            return chance

if "wizard" in RoleList:
    wizard_name = wizard_check(0)
    print(type(wizard_name))

Bemafia = False
player_action = False
player_accused = 0
player_side = False
choi = -5
print("You are", RoleList[0])
stop = len(List)
stop = stop - 1
if RoleList[0] == "mafia":
    Bemafia = True
    print("The other mafia are: ")
    for i in range(stop):
        if RoleList[i] == 'mafia':
            print(List[i])

accuse_mafia_action = False
    
nuke = 0
rng = 0
while mafia != 0 or innocent > mafia:
    nuke = (50 / number) + (25 / number)
    nuke = int(nuke)
    #NIGHT TIME
    if "wizard" in RoleList:
        wizard_name = wizard_check(0)
    time.sleep(0.25)
    print("Mafia...")
    time.sleep(0.75)
    print("WAKE UP!")
    time.sleep(0.75)
    print("Who do you want to kill?")
    time.sleep(2)
    while confirm_kill == False:
        if RoleList[0] == "mafia":
            print(List)
            try:
                kill = int(input("select according to numerical number in the list: "))
                if kill > stop:
                    print('go within the range of list!')
                else:
                    confirm_kill = True
            except:
                print("please use number to kill")
        else:
            kill = random.randint(1, stop)
        if WIZ_reveal == True and "wizard" in RoleList:
            if RoleList[kill] == "wizard":
                print("Alright... please go to sleep")
                confirm_kill = True
        elif RoleList[kill] != "mafia":
            confirm_kill = True
    print("Alright... please go to sleep")
    time.sleep(1.25)

    if "doctor" in RoleList:        
        print("Doctor...")
        time.sleep(1)
        print("WAKE UP!")
        time.sleep(0.75)
        print("Who do you want to protect?")
        time.sleep(2)
        DOC_protect = random.randint(0, stop)
        print("Alright... please go to sleep")
        time.sleep(1.25)

    if "wizard" in RoleList:
        print("Wizard...")
        time.sleep(1)
        print("WAKE UP!")
        time.sleep(0.75)
        print("Who do you want to identify?")
        time.sleep(2)
        WIZ_identify = random.randint(0, stop)
        print("Alright... please go to sleep")
        if RoleList[WIZ_identify] == "mafia":
            WIZ_target = True
        time.sleep(1.25)

        
    print("EVERYONE!")
    time.sleep(1)
    print("wake up...")
    time.sleep(1.5)
    if kill == DOC_protect:
        print("someone was going to die but was saved by the doctor.")
    else:
        print(List[kill], "is dead.")
        if WIZ_identify > kill:
            WIZ_identify = WIZ_identify - 1
        List.remove(List[kill])
        RoleList.pop(kill)
        stop = len(List)
        stop = stop - 1
        innocent = innocent - 1
        number = number - 1

    if "wizard" in RoleList:
        wizard_name = wizard_check(0)
    
    if innocent <= mafia:
        break

    #DAY TIME and DISCUSSION
    time.sleep(1)
    print("Remaining:")
    print(List)
    """
    print(RoleList)
    print(WIZ_identify)
    print(wizard_name)
    """
    print(WIZ_identify)
    time.sleep(1.75)
    print("Discuss, then hang who you think is suspicious...")
    time.sleep(2)
    print("---START DISCUSSING---")
    wait = 20 * math.log(stop + 1)
    wait = int(wait)
    for i in range(wait):
        chance = random.randint(0, 6)
        chance2 = random.randint(1, 4)
        rng = random.randint(1, 8)
        if player in List and chance2 == 1:
            try:
                choice = int(input("What do you think to do?: nothing[0], accuse[1], opinion[2], lead disscussion[3]: "))
            except:
                print(".....")
            if choice == 1:
                print(List)
                try:
                    choice = int(input("Who do you want to accuse?(use number): "))
                    player_accused = choice
                    player_action = True
                    choice = 0
                except:
                    print("use numbers, not name, or is it a typo?")
            elif choice == 2:
                try:
                    choice = int(input("HardClear[1], Trust[2], Distrust[3]"))
                    if choice == 1:
                        print(List)
                        choice = int(input("who?: "))
                        player_action = True
                        player_accused = choice
                        choice = 1
                    if choice == 2:
                        print(List)
                        choice = int(input("who?: "))
                        player_action = True
                        player_accused = choice
                        choice = 4
                        choi = 1
                    if choice == 3:
                        print(List)
                        choice = int(input("who?: "))
                        player_action = True
                        player_accused = choice
                        choice = 4
                        choi = 0
                        
                except:
                    print("use numbers")

            elif choice == 3:
                player_action = True
                
        if rng == 1 and Bemafia == True:
            chance3 = random.randint(0, stop)
            if RoleList[chance2] == 'mafia':
                accuse_mafia_action = True
            
        if WIZ_target == True and chance2 == 3:
            chance = 0
            WIZ_accuse = True

        if player_action == True:
            chance = choice
        time.sleep(1)
        if chance == 0:
            chance = random.randint(1, stop)
            if player != List[0]:
                chance = random.randint(0, stop)
            chance2 = random.randint(0, stop)
            if accuse_mafia_action == True:
                chance2 = chance3
            if player_action == True:
                chance = 0
                chance2 = player_accused
            if chance != chance2 and (RoleList[chance] != "mafia" or RoleList[chance2] != "mafia"):
                if WIZ_accuse == True and player_action == False:
                    chance = wizard_name
                    chance2 = WIZ_identify
                    print(List[wizard_name], "suspects", List[chance2],"!")

                else:
                    print(List[chance], "suspects", List[chance2],"!")
                SUSmetre[chance] += 2
                SUSmetre[chance2] += 4
                chance3 = random.randint(0, 8)
                odds = random.randint(1,5)


                if player_action != True and odds != 3 and chance2 != 0:
                    choice = int(input("What do you think to do?: nothing[0], agree[1], defend[2], redirect[3]"))
                    if choice == 1:
                        chance3 = 1
                        player_side = True
                    if choice == 2:
                        chance3 = 3
                        player_side = True
                    if choice == 3:
                        chance3 = 4
                        player_side = True


                time.sleep(1.5)
                if chance3 == 0:
                    print("The group is listening...")
                    SUSmetre[chance2] += 1
                if chance3 == 1:
                    chance3 = random.randint(1, stop)
                    if player_side == True:
                        chance3 = 0
                    if chance3 != chance and chance3 != chance2:
                        print(List[chance3], "agreed with", List[chance],"!")
                        SUSmetre[chance3] += 1
                        SUSmetre[chance2] += 2
                if chance3 == 2:
                    print("The group doesn't seemed to be convinced.")
                    SUSmetre[chance2] -= 4
                if chance3 == 3:
                    chance3 = random.randint(1, stop)
                    if player_side == True:
                        chance3 = 0
                    if chance3 != chance and chance3 != chance2:
                        print(List[chance3], "defends", List[chance2],"!")
                        SUSmetre[chance2] -= 2
                        SUSmetre[chance3] += 1
                if chance3 == 4:
                    chance3 = random.randint(1, stop)
                    if player_side == True:
                        chance3 = 0
                    if chance3 != chance and chance3 != chance2:
                        print(List[chance3], "redirects the accusation to", List[chance])
                        SUSmetre[chance2] -= 1
                        SUSmetre[chance] += 2
                        SUSmetre[chance3] += 2

        elif chance == 1:
            chance = random.randint(1, stop)
            if player != List[0]:
                chance = random.randint(0, stop)
            chance2 = random.randint(0, stop)
            if player_action == True:
                chance = 0
                chance2 = player_accused
            if chance != chance2:
                print(List[chance], "thinks", List[chance2],"might not be mafia")
                SUSmetre[chance2] -= 2
                odds = random.randint(1, 3)
                if odds == 3:
                    SUSmetre[chance] -= 1
                chance3 = random.randint(1, 5)
                if chance3 == 5:
                    chance3 = random.randint(1, stop)
                    if chance3 != chance and chance3 != chance2:
                        print(List[chance3], "now suspects both", List[chance], "and", List[chance2])
                        SUSmetre[chance2] += 3
                        SUSmetre[chance] += 3
                        SUSmetre[chance3] += 1

        elif chance == 2:
            print("The group is still discussing")
            time.sleep(1)

        elif chance == 3:
            chance = random.randint(1, stop)
            if player != List[0]:
                chance = random.randint(0, stop)
            if player_action == True:
                chance = 0
            print(List[chance], "is now leading the group discussion")

        elif chance == 4:
            chance = random.randint(1, stop)
            if player != List[0]:
                chance = random.randint(0, stop)
            chance2 = random.randint(0, stop)
            chance3 = random.randint(0, 1)
            if player_action == True:
                chance = 0
                chance2 = player_accused
                chance3 = choi
            if chance != chance2 and chance3 == 0 and (RoleList[chance] != "mafia" or RoleList[chance2] != "mafia"):
                print(List[chance], "does not seem to trust", List[chance2])
                SUSmetre[chance2] += 1

                
            elif chance != chance2 and chance3 == 1:
                print(List[chance], "seems to trust", List[chance2])
                SUSmetre[chance2] -= 1
                
        WIZ_accuse = False
        player_action = False
        player_side = False
        choice = 0
        accuse_mafia_action = False
        for i in range(2, 3):
            print(".....")
            time.sleep(0.15)


    #   DECISION ON WHO TO HANG

    print("The group made their decision!")
    time.sleep(2)
    print("They are going to hang...")
    time.sleep(2)
    
    #print(SUSmetre)
    
    largest = max(SUSmetre)
    chance = SUSmetre.index(largest)
    SUSmetre[chance] = 0
    largest = max(SUSmetre)
    chance2 = SUSmetre.index(largest)
    odds = random.randint(1, 3)
    if odds == 1 and number > 6:
        chance = chance2
    print(List[chance])
    time.sleep(1.5)
    print(".....")
    time.sleep(1.5)
    
    #print(SUSmetre)
    
    if chance != WIZ_identify and WIZ_target == True:
        print(List[wizard_name], "had revealed itself as wizard!")
        time.sleep(2)
        print(List[wizard_name], "points to", List[WIZ_identify], "as mafia!")
        time.sleep(1.5)
        chance = WIZ_identify
        WIZ_reveal = True
    if RoleList[chance] == "mafia":
        print(List[chance], "was mafia!")
        List.remove(List[chance])
        RoleList.pop(chance)
        mafia = mafia - 1
        stop = len(List)
        stop = stop - 1
    else:
        print(List[chance], "was not mafia...")
        List.remove(List[chance])
        RoleList.pop(chance)
        innocent = innocent - 1
        stop = len(List)
        stop = stop - 1

    print(List)
    """
    print(RoleList)
    print(WIZ_identify)
    print(wizard_name)
    """

    if innocent <= mafia:
        break
    if mafia == 0:
        break

    confirm_kill = False
    WIZ_target = False
    WIZ_accuse = False
    player_action = False
    player_side = False
    number = number - 1

    SUSmetre.clear()
    
    for i in range(number):
        SUSmetre.append(0)
    #print(SUSmetre)

if innocent <= mafia:
    while innocent != 0:
        kill = random.randint(0, stop)
        if RoleList[kill] != "mafia":
            List.remove(List[kill])
            RoleList.pop(kill)
            stop = len(List)
            stop = stop - 1
            innocent = innocent - 1
    print(List)
    print("Mafia wins!")

else:
    print("The Town wins!")
           
    




    



    
