print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

left_or_right_choice = input("Left or Right: ")

if left_or_right_choice == "left" or left_or_right_choice == "Left":

  swim_or_wait_choice = input("Swim or Wait: ")

  if swim_or_wait_choice == "Wait" or swim_or_wait_choice == "wait":

    which_door_choice = input("Which Door! 'Red' , 'Blue' or 'Yellow': ")
  
    if which_door_choice == "Yellow" or which_door_choice == "yellow":
      print("You Win!")
    elif which_door_choice == "Blue" or which_door_choice == "blue":
      print("Eaten by beasts.Game Over")
    elif which_door_choice == "Red" or which_door_choice == "red":
      print("Burned by fire. Game Over.")
    else:
      print("Game Over")   

  elif swim_or_wait_choice == "Swim" or left_or_right_choice == "swim":
     print("Attacked by trout. Game Over.")

  else:    
     print("Attacked by trout. Game Over.")

else:
  print("Fall into a hole. Game Over.")


