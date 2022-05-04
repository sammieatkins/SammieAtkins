road = input("You come to a fork in the road, do you want to go LEFT or RIGHT? ")
road = road.lower()

if road == "left":
    print("You come to a troll!!")
    troll = input("Do you want to SLAY or BE SLAIN? ")
    troll = troll.lower()
    if troll == "slay":
        print("You search for a weapon, but sadly realize, you only have your laptop...")
        print("You look at your laptop")
    elif troll == "be slain":
        print("As you close your eyes to accept your grim fate, the troll smiles upon you...")
    else:
        print("Your lack of decision was fatal... The troll carries you away.")

elif road == "right":
    print("You find a wizard on the path.")
else:
    print("I didn't quite get that...")

