import tkinter as tk
import random

class item:
    def __init__(self, name, type, amount):
        self.name = name
        self.type = type
        self.amount = amount

class mob:
    def __init__(self, name, hp, armor, attack, level = 1, experience = 0, inventory = []):
        self.level = level
        self.experience = experience
        self.name = name
        self.maxhp = hp
        self.hp = hp
        self.armor = armor
        self.attack = attack
        self.alive = True
        self.iteminventory = list([])
        self.inventory = list([])
    
    def levelup(self):
        self.maxhp += random.randint(0,3)
        self.armor += random.randint(0,3)
        self.attack += random.randint(0,3)
        self.experience = 0
        self.level += 1

    def takedamage(self, damage):
        if damage > self.armor:
            self.hp -= damage - self.armor
        self.die()
        return self.alive
    
    def die(self):
        if self.hp < 1:
            self.alive = False
            self.hp = 0

    def MyInventory(self, item):
        self.iteminventory.append(item)
        self.inventory.append(item.name)
        if item.type == "offense":
            self.attack += item.amount
        else:
            self.armor += item.amount

name = "Jameson"#input("Please enter your name")

LowMobNames = ["Goblin", "HobGoblin", "Slime", "Skeleton", "Bandit", "Zombie", "Wolf"]
MediumMobNames = ["Giant", "Troll", "Ent", "Bandit Leader", "Lich", "Dire Wolf"]
HighMobNames = ["Yeti", "Stone Giant", " Great Knight", "Giant Squid"]
EpicMobNames = ["Dragon", "Kracken"]

player = mob(name, 100, 0, 5)
sword = item("sword", "offense", 5)
player.MyInventory(sword)
iterator = 0
MyNumber = 0

def on_exitbutton_click():
    global player
    player.hp = 0
    player.die()
    window.destroy()

def CreateRandomMob(strength):
    global MyNumber
    if strength == "epic":
        NewMob = mob(EpicMobNames[random.randint(0, len(EpicMobNames) - 1)], random.randint(80,320), random.randint(20,40), random.randint(32,128))
    elif strength == "high":
        NewMob = mob(HighMobNames[random.randint(0, len(HighMobNames) - 1)], random.randint(40,160), random.randint(10,20), random.randint(16,64))
    elif strength == "medium":
        NewMob = mob(MediumMobNames[random.randint(0, len(MediumMobNames) - 1)], random.randint(20,80), random.randint(0,10), random.randint(8,32))
    elif strength == "low":
        NewMob = mob(LowMobNames[random.randint(0, len(LowMobNames) - 1)], random.randint(10,40), random.randint(0,5), random.randint(2,16))
    MyNumber = 0
    return NewMob

MobList = list([])
def find_encounter():
    global player
    global MobList
    MobList = []
    Difficulty = player.level * 2
    while Difficulty > 0:
        if Difficulty >= 20:
            MobList.append(CreateRandomMob("epic"))
            Difficulty -= 20
        elif Difficulty >= 15:
            MobList.append(CreateRandomMob("high"))
            Difficulty -= 15
        elif Difficulty >= 8:
            MobList.append(CreateRandomMob("medium"))
            Difficulty -= 7
        else:
            MobList.append(CreateRandomMob("low"))
            Difficulty -= 1


def GameOver():
    Player_Name.config(text = player.name + '\n' + "Level: " + str(player.level) + "\n" + "HP: " + str(player.hp) + "\n" + "Exp: " + str(player.experience) + "\n" + "Armor: " + str(player.armor) + "\n" +"Attack: " + str(player.attack) + "\n\n\n")
    Main_Text.config(text = "Game Over")
    Action_Button.config(command = on_exitbutton_click)
    Flee_Button.config(command = on_exitbutton_click)

def attack():
    global MobList
    global MyNumber
    if MobList[MyNumber].alive:
        player.takedamage(MobList[MyNumber].attack)
        MobList[MyNumber].takedamage(player.attack)
        if not player.alive:
            GameOver()
        if not MobList[MyNumber].alive:
            MyNumber +=1

def flee():
    print('hi')

def on_action_click():
    global iterator
    global MyNumber
    Player_Name.config(text = (player.name + '\n' + "Level: " + str(player.level) + "\n" + "HP: " + str(player.hp) + "\n" + "Exp: " + str(player.experience) + "\n" + "Armor: " + str(player.armor) + "\n" +"Attack: " + str(player.attack) + "\n\n\n"), width = 100)
    if iterator == 0:
        iterator += 1
        find_encounter()
        MobListNames = ""
        for x in MobList:
            MobListNames += x.name + "\n"
        Main_Text.config(text = "Your opponents are: \n" + MobListNames)
    elif iterator == 1:
        Action_Button.config(text = "Attack")
        Flee_Button.config(text = "Flee")
        Main_Text.config(text = "Current Opponent: \n" + MobList[MyNumber].name + '\n' + "hp: " + str(MobList[MyNumber].hp) + "\n" + "Armor: " + str(MobList[MyNumber].armor) +  "\n" + "Attack: " + str(MobList[MyNumber].attack))
        attack()
        if MyNumber >= len(MobList):
            iterator = 0
            player.experience += 50
            if player.experience == 100:
                player.levelup()
            player.hp = player.maxhp
            #Else get item

def on_flee_click():
    global iterator
    if iterator == 0:
        iterator += 1
        find_encounter()
    elif iterator == 1:
        Flee_Button.config(text = "Flee")
        Action_Button.config(text = "Attack")
        Main_Text.config(text = MobList[MyNumber].name + '\n' + "hp: " + str(MobList[MyNumber].hp) + "\n" + "Armor: " + str(MobList[MyNumber].armor) +  "\n" + "Attack: " + str(MobList[MyNumber].attack))
        flee()


while player.alive:
    window = tk.Tk()
    Player_Inventory = tk.Label(text = player.inventory)
    Player_Name = tk.Label(text = (player.name + '\n' + "Level: " + str(player.level) + "\n" + "HP: " + str(player.hp) + "\n" + "Exp: " + str(player.experience) + "\n" + "Armor: " + str(player.armor) + "\n" +"Attack: " + str(player.attack) + "\n\n\n"), width = 100)
    Main_Text = tk.Label(text = "Welcome to the Arena! \n \n \n \n", height = 5)
    Player_Name.pack(side=tk.TOP, ipadx = 25)
    Action_Button = tk.Button(text = "Continue", command = on_action_click, height = 3)
    Action_Button.pack(side = tk.RIGHT, anchor= tk.SW, ipadx = 25)
    Flee_Button = tk.Button(text = "Continue", command = on_flee_click, height = 3)
    Flee_Button.pack(side = tk.LEFT, anchor = tk.SE, ipadx = 25)
    Player_Inventory.pack(side=tk.LEFT, anchor = tk.NW, ipadx = 25)
    Main_Text.pack(side = tk.TOP ,ipadx = 25)
    
    ExitButton = tk.Button(text = "EXIT", command = on_exitbutton_click)
    ExitButton.pack(side=tk.BOTTOM, ipadx = 25)

    window.mainloop()