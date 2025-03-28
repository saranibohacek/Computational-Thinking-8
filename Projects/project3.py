#Beginning
robe_bear_points=0
basic_bear_points=0
bee_bear_points=0
bat_bear_points=0
heart_bear_points=0

#Middle
answer=input("which color do you like the most A)pink, B)red, C)black, D)yellow, E)white")
if answer == "A":
    robe_bear_points+=1
elif answer == "B":
    heart_bear_points+=2
elif answer == "C":
    bat_bear_points+=2
elif answer == "D":
    bee_bear_points+=2
elif answer == "E":
    basic_bear_points+=1

answer=input("how would you want to spend your weekend? A)spa, B)go on a date, C)explore abandoned places, D)go to a flower field, E)see my friends")
if answer == "A":
    robe_bear_points+=3
elif answer == "B":
    heart_bear_points+=3
elif answer == "C":
    bat_bear_points+=2
elif answer == "D":
    bee_bear_points+=2
elif answer == "E":
    basic_bear_points+=2

answer=input("what's your fav season? A)winter, B)summer, C)fall, D)spring, E)none")
if answer == "A":
    robe_bear_points+=2
elif answer == "B":
    heart_bear_points+=2
elif answer == "C":
    bat_bear_points+=3
elif answer == "D":
    bee_bear_points+=3
elif answer == "E":
    basic_bear_points+=2

answer=input("what's your fav school subject? A)breaks, B)english, C)science, D)history, E)lunch")
if answer == "A":
    robe_bear_points+=2
elif answer == "B":
    heart_bear_points+=2
elif answer == "C":
    bat_bear_points+=3
elif answer == "D":
    bee_bear_points+=3
elif answer == "E":
    basic_bear_points+=2

answer=input("what's your fav movie genre? A)drama, B)romance, C)horror, D)adventure, E)comedy")
if answer == "A":
    robe_bear_points+=3
elif answer == "B":
    heart_bear_points+=3
elif answer == "C":
    bat_bear_points+=3
elif answer == "D":
    bee_bear_points+=3
elif answer == "E":
    basic_bear_points+=2

#End
if robe_bear_points > heart_bear_points and robe_bear_points > bat_bear_points and robe_bear_points > bee_bear_points and robe_bear_points > basic_bear_points:
    print("you're the bartholomew bear bathrobe!")
elif heart_bear_points>bat_bear_points and heart_bear_points>bee_bear_points and heart_bear_points>basic_bear_points:
    print("you're the bartholomew bear heartthrob!")
elif bat_bear_points>bee_bear_points and bat_bear_points>basic_bear_points:
    print("you're the bartholomew bear bat!")
elif bee_bear_points>basic_bear_points:
    print("you're the bartholomew bear bumblebee!")
else:
    print("you're the bartholomew bear classic!")
