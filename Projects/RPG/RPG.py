import random

health = 100
x = 0
y = 0

print("""
   ▄████████    ▄████████    ▄████████    ▄███████▄    ▄████████    ▄████████    ▄██████▄  ▄██   ▄   
  ███    ███   ███    ███   ███    ███   ███    ███   ███    ███   ███    ███   ███    ███ ███   ██▄ 
  ███    ███   ███    ███   ███    █▀    ███    ███   ███    █▀    ███    █▀    ███    █▀  ███▄▄▄███ 
  ███    ███  ▄███▄▄▄▄██▀  ▄███▄▄▄       ███    ███  ▄███▄▄▄      ▄███▄▄▄      ▄███        ▀▀▀▀▀▀███ 
▀███████████ ▀▀███▀▀▀▀▀   ▀▀███▀▀▀     ▀█████████▀  ▀▀███▀▀▀     ▀▀███▀▀▀     ▀▀███ ████▄  ▄██   ███ 
  ███    ███ ▀███████████   ███    █▄    ███          ███    █▄    ███    █▄    ███    ███ ███   ███ 
  ███    ███   ███    ███   ███    ███   ███          ███    ███   ███    ███   ███    ███ ███   ███ 
  ███    █▀    ███    ███   ██████████  ▄████▀        ██████████   ██████████   ████████▀   ▀█████▀  
               ███    ███                       
Welcome to the world of Arepeegy. After escaping from prison and fleeing                                                     
     """)

while True:
    action = input("What do you want to do? \n  ")

    if "?" in action:
        print("Do you need help? Type /help")

    elif action == "/help":
        print("""Commands:
        Directions: 'Go North' or 'Go to woods'
        Merchant
        Engage
        Look around
        Explore / Go random diection
        Coordinates
        Equipment
        Inventory
        """
        )
    elif "go north" in action:
        print("You go North")
        x+=1
    elif "go south" in action:
        print("You go South")
        x-=1
    elif "go east" in action:
        print("You got East")
        y+=1
    elif "go west" in action:
        print("You got West")
        y-=1
    
    if "coordinates" in action or "location" in action:
        print(f"Your coordinates are: {x},{y}")
        if x==0 and y==0:
            print("MOVE already")
    
    if action == "end" or action == "q":
        print("[ENDING LOOP]")
        break

    

#class player:
    #def __init__(self, health):
      #  self.health = health
        
#def get_health(self):
    #return self.health

#def set_health(self):
   # self.health = new_health
  #e  new_health = 100



#get_health(self)