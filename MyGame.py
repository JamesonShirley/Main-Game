import tkinter as tk
class item:
    def __init__(self, name, type, amount):
        self.name = name
        self.type = type
        self.amount = amount

class mob:
    def __init__(self, name, hp, armor, attack, inventory = []):
        self.name = name
        self.hp = hp
        self.armor = armor
        self.attack = attack
        self.alive = True
        self.iteminventory = list([])
        self.inventory = list([])


    def takedamage(self, damage):
        self.hp -= damage - self.armor
        self.die()
        return self.alive
    
    def die(self):
        if self.hp < 1:
            self.alive = False

    def MyInventory(self, item):
        self.iteminventory.append(item)
        self.inventory.append(item.name)
        if item.type == "offense":
            self.attack += item.amount
        else:
            self.armor += item.amount

name = "Jameson"#input("Please enter your name")



player = mob(name, 100, 0, 15)
sword = item("sword", "offense", 5)
player.MyInventory(sword)
iterator = 0
def on_exitbutton_click():
    global player
    player.hp = 0
    player.die()
    window.destroy()

def find_encounter():
    print("hi")

def attack():
    print("hi")

def flee():
    print('hi')

def on_action_click():
    if iterator == 0:
        Action_Button.config(text = "Attack")
        iterator += 1
        find_encounter()
    elif iterator == 1:
        attack()

def on_flee_click():
    if iterator == 0:
        Flee_Button.config(text = "Flee")
        iterator += 1
        find_encounter()
    elif iterator == 1:
        flee()


while player.alive:
    window = tk.Tk()
    Player_Inventory = tk.Label(text = player.inventory)
    Player_Name = tk.Label(text = (player.name + '\n' + "HP: " + str(player.hp)), width = 100)
    Main_Text = tk.Label(text = "Hi", height = 5)
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