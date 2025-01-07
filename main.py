print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-=\"'"=.__________________|_______
|                   |    __.--" , ; `\"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     ($) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************''')
print("Welcome to the Classified Treasure Quest!")
print("Your mission is to make the correct decisions to find the treasure...")
print("You start the game at the edge of a canyon..\n")
print("There is a bridge to the right that goes into the forest...")
print("Or a bridge to the left that goes into the mountains...")
first_choice = input("Which way do you go? (right/left)\n").lower()
if first_choice == "left":
  print("You walk onto the bridge to the mountains and succesfully cross to the other side.\n")
  print("When you get to the other side you look ahead and see a boulder blocking your path.\n")  
  second_choice = input("Do you want to push the boulder out of the way or go around (push/around)\n").lower()
  if second_choice == "push":
    print("You successfully push the boulder out of the way and can continue along the path.\n")
    third_choice = input("You continue on the path and see two caves. One above you that you can climb too or one in the ground that you can crawl into.\nDo you want to crawl or climb? (crawl/climb)\n").lower()
    if third_choice == "climb":
      print("You climb up the cliff and succesfully reach the cave.\nYou find two chests inside the cave.\n")
      fourth_choice = input("Do you want to open the chest on the left or the right? (left/right)\n").lower()
      if fourth_choice == "right":
        print("CONGRATULATIONS YOU FOUND THE TREASURE!!!\n")
        print('''       ,,,,,,,,,,,,,
    .;;;;;;;;;;;;;;;;;;;,.
  .;;;;;;;;;;;;;;;;;;;;;;;;,
.;;;;;;;;;;;;;;;;;;;;;;;;;;;;.
;;;;;@;;;;;;;;;;;;;;;;;;;;;;;;' .............
;;;;@@;;;;;;;;;;;;;;;;;;;;;;;;'.................
;;;;@@;;;;;;;;;;;;;;;;;;;;;;;;'...................
`;;;;@;;;;;;;;;;;;;;;@;;;;;;;'.....................
 `;;;;;;;;;;;;;;;;;;;@@;;;;;'..................;....
   `;;;;;;;;;;;;;;;;@@;;;;'....................;;...
     `;;;;;;;;;;;;;@;;;;'...;.................;;....
        `;;;;;;;;;;;;'   ...;;...............;.....
           `;;;;;;'        ...;;..................
              ;;              ..;...............
              `                  ............
             `                      ......
            `                         ..
           `                           '
          `                           '
         `                           '
        `                           `
        `                           `,
        `
         `
           `.''')
      else:
        print("There is a cobra inside the chest that bites you, you die from your injuries...try again.")
        print('''    
                     uu$$$$$$$$$$$uu
                  uu$$$$$$$$$$$$$$$$$uu
                 u$$$$$$$$$$$$$$$$$$$$$u
                u$$$$$$$$$$$$$$$$$$$$$$$u
               u$$$$$$$$$$$$$$$$$$$$$$$$$u
               u$$$$$$$$$$$$$$$$$$$$$$$$$u
               u$$$$$$"   "$$$"   "$$$$$$u
               "$$$$"      u$u       $$$$"
                $$$u       u$u       u$$$
                $$$u      u$$$u      u$$$
                 "$$$$uu$$$   $$$uu$$$$"
                  "$$$$$$$"   "$$$$$$$"
                    u$$$$$$$u$$$$$$$u
                     u$"$"$"$"$"$"$u
          uuu        $$u$ $ $ $ $u$$       uuu
         u$$$$        $$$$$u$u$u$$$       u$$$$
          $$$$$uu      "$$$$$$$$$"     uu$$$$$$      GAME OVER!!
        u$$$$$$$$$$$uu    """""    uuuu$$$$$$$$$$
        $$$$"""$$$$$$$$$$uuu   uu$$$$$$$$$"""$$$"
         """      ""$$$$$$$$$$$uu ""$"""
                   uuuu ""$$$$$$$$$$uuu
          u$$$uuu$$$$$$$$$uu ""$$$$$$$$$$$uuu$$$
          $$$$$$$$$$""""           ""$$$$$$$$$$$"
           "$$$$$"                      ""$$$$""
             $$$"                         $$$$"                                        ''')
    else:
      print("You crawl into the cave and rocks collapse onto you killing you..try again.\n")
      print('''    
                   uu$$$$$$$$$$$uu
                uu$$$$$$$$$$$$$$$$$uu
               u$$$$$$$$$$$$$$$$$$$$$u
              u$$$$$$$$$$$$$$$$$$$$$$$u
             u$$$$$$$$$$$$$$$$$$$$$$$$$u
             u$$$$$$$$$$$$$$$$$$$$$$$$$u
             u$$$$$$"   "$$$"   "$$$$$$u
             "$$$$"      u$u       $$$$"
              $$$u       u$u       u$$$
              $$$u      u$$$u      u$$$
               "$$$$uu$$$   $$$uu$$$$"
                "$$$$$$$"   "$$$$$$$"
                  u$$$$$$$u$$$$$$$u
                   u$"$"$"$"$"$"$u
        uuu        $$u$ $ $ $ $u$$       uuu
       u$$$$        $$$$$u$u$u$$$       u$$$$
        $$$$$uu      "$$$$$$$$$"     uu$$$$$$      GAME OVER!!
      u$$$$$$$$$$$uu    """""    uuuu$$$$$$$$$$
      $$$$"""$$$$$$$$$$uuu   uu$$$$$$$$$"""$$$"
       """      ""$$$$$$$$$$$uu ""$"""
                 uuuu ""$$$$$$$$$$uuu
        u$$$uuu$$$$$$$$$uu ""$$$$$$$$$$$uuu$$$
        $$$$$$$$$$""""           ""$$$$$$$$$$$"
         "$$$$$"                      ""$$$$""
           $$$"                         $$$$"                                        ''')
  else: 
    print("You go around the boulder and run into a mountain lion that attacks you..you die, try again\n")
    print('''    
             uu$$$$$$$$$$$uu
          uu$$$$$$$$$$$$$$$$$uu
         u$$$$$$$$$$$$$$$$$$$$$u
        u$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$"   "$$$"   "$$$$$$u
       "$$$$"      u$u       $$$$"
        $$$u       u$u       u$$$
        $$$u      u$$$u      u$$$
         "$$$$uu$$$   $$$uu$$$$"
          "$$$$$$$"   "$$$$$$$"
            u$$$$$$$u$$$$$$$u
             u$"$"$"$"$"$"$u
  uuu        $$u$ $ $ $ $u$$       uuu
 u$$$$        $$$$$u$u$u$$$       u$$$$
  $$$$$uu      "$$$$$$$$$"     uu$$$$$$      GAME OVER!!
u$$$$$$$$$$$uu    """""    uuuu$$$$$$$$$$
$$$$"""$$$$$$$$$$uuu   uu$$$$$$$$$"""$$$"
 """      ""$$$$$$$$$$$uu ""$"""
           uuuu ""$$$$$$$$$$uuu
  u$$$uuu$$$$$$$$$uu ""$$$$$$$$$$$uuu$$$
  $$$$$$$$$$""""           ""$$$$$$$$$$$"
   "$$$$$"                      ""$$$$""
     $$$"                         $$$$"                                        ''')
else:
    print("You walk onto the bridge to the forest and the bridge snaps due to not being secured to a tree well enough. You fall into the canyon and die, try again.")
    print('''    
             uu$$$$$$$$$$$uu
          uu$$$$$$$$$$$$$$$$$uu
         u$$$$$$$$$$$$$$$$$$$$$u
        u$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$"   "$$$"   "$$$$$$u
       "$$$$"      u$u       $$$$"
        $$$u       u$u       u$$$
        $$$u      u$$$u      u$$$
         "$$$$uu$$$   $$$uu$$$$"
          "$$$$$$$"   "$$$$$$$"
            u$$$$$$$u$$$$$$$u
             u$"$"$"$"$"$"$u
  uuu        $$u$ $ $ $ $u$$       uuu
 u$$$$        $$$$$u$u$u$$$       u$$$$
  $$$$$uu      "$$$$$$$$$"     uu$$$$$$      GAME OVER!!
u$$$$$$$$$$$uu    """""    uuuu$$$$$$$$$$
$$$$"""$$$$$$$$$$uuu   uu$$$$$$$$$"""$$$"
 """      ""$$$$$$$$$$$uu ""$"""
           uuuu ""$$$$$$$$$$uuu
  u$$$uuu$$$$$$$$$uu ""$$$$$$$$$$$uuu$$$
  $$$$$$$$$$""""           ""$$$$$$$$$$$"
   "$$$$$"                      ""$$$$""
     $$$"                         $$$$"                                        ''')