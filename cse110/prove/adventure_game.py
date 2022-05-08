# Put spaces after questions!!

# Choice 1.
evening = input("You’re Harry Potter and you’re in your fifth year of Hogwarts. You have a free evening tonight. Do you STUDY for your O.W.Ls or practice with the QUIDDITCH team? ")

# Choice 1.1 - STUDY.
if evening.lower() == "study":
    celebrate = input("Hermione is very proud. Even better, you get mostly Os on your exams!! Great choice. After the O.W.Ls, you, Ron, and Hermione decide you need to celebrate!! Should you get BUTTERBEER from Hogsmeade, spend an evening relaxing on the GROUNDS, or visit HAGRID? ")
    # Choice 1.1.1 - BUTTERBEER.
    if celebrate.lower() == "butterbeer":
        next_shop = input("After you finish up at The Three Broomsticks, you decide you have time to check out one more shop. Do you go to ZONKO’S Joke Shop or HONEYDUKES Sweetshop? ")
        # Choice 1.1.1.1 - ZONKO'S.
        if next_shop.lower() == "zonko's":
            hermione = input("Hermione finds Fred and George testing on first years. Do you let her FREAK OUT on them or try and drag her back to the CASTLE? ")
            # Choice 1.1.1.1.1 - FREAK OUT. 
            if hermione.lower() == "freak out":
                print("While Hermione is telling off Fred and George, you sneak away and buy candy since you know she’ll be in no mood to watch you shop after this. ")
            # Choice 1.1.1.1.2 - CASTLE. 
            elif hermione.lower() == "castle":
                print("She stomps off in a huff and spends the rest of the weekend in the library. Turns out it was no use anyways because she still reported them. Fred and George appreciate your efforts, but they’re no help with your homework.")
            else:
                print("Please try again. :)")
        # Choice 1.1.1.2 - HONEYDUKES. 
        elif next_shop.lower() == "honeydukes":
            candy = input("You arrive at Honeydukes, do you want to buy Bertie Bott’s Every Flavor BEANS or Chocolate FROGS? ")
            # Choice 1.1.1.2.1
            if candy.lower() == "beans":
                print("Eeeeeeew!! You get dog food :(. Ron thinks it’s hilarious though.")
            # Choice 1.1.1.2.2
            elif candy.lower() == "frogs":
                print("Woohoo!! Ron finds the Agrippa chocolate frog card!! What a successful day off :)")
            else:
                print("Please try again. :)")
        else:
            print("Please try again. :)")
      
    # Choice 1.1.2 - GROUNDS.
    elif celebrate.lower() == "grounds":
        fight = input("While the three of you are relaxing under a tree, minding your own business, Malfoy, Crabbe, and Goyle decide to try and steal your snacks. You only have time for one spell. Do you use EXPELLIARMUS or ACCIO? ")
        # Should one of these end in losing the snacks?
        # Choice 1.1.2.1 - EXPELLIARMUS.
        if fight.lower() == "expelliarmus":
            print("Success!! You’ve stolen Malfoy’s wand. Goyle fights you for it and gives it back to Malfoy. At this point you’ve gotten the attention of the people around you and Malfoy realizes he’s lost this round. They meander back to the castle, bullying some first years as they go.")
        # Choice 1.1.2.2 - ACCIO.
        elif fight.lower() == "accio":
            print("Crabbe and Goyle have stolen your treacle tart!! You think better of using accio because you’ve underestimated the speed at which they can consume food and you no longer want it back. Better luck next time :(")
        # Hidden choice 1.1.2.3 - STUPEFY.
        elif fight.lower() == "stupefy":
            print("All three of you think of the same spell: stupefy! The poor slytherins didn’t have a chance. You send their limp bodies flying down the hill so you can continue enjoying your evening, and your snacks :)")
        # Hidden Choice 1.1.2.4 - PETRIFICUS TOTALUS.
        elif fight.lower() == "petrificus totalus":
            print("You catch Malfoy right as he’s about to snatch your Bertie Bott’s Every Flavor Beans. Now stiff as a board lying face first in the dirt, Crabbe and Goyle drag him all the way back to the castle. They would perform the counter curse, but they don’t know how. You, Ron, and Hermione can’t stop laughing :)")
        else:
            print("Please try again. :)")
    # Choice 1.1.3 - HAGRID.
    elif celebrate.lower() == "hagrid":
        hagrid = input("You each fill Hagrid in on your test scores and he’s so happy for you all. He rewards you with three rock cakes each. Professor Umbridge shows up to give Hagrid his teaching review while you’re there. Do you hide in the forbidden FOREST or make a mad DASH back to the castle under the invisibility cloak? ")
        # Bug bug bug bug bug bug
        # Choice 1.1.3.1 - FOREST.
        if hagrid.lower() == "forest":
            print("After what feels like forever, you see Professor Umbridge make her way back to the castle. You decide to go back to Hagrid’s hut to comfort him. Hermione makes him some tea while Ron pats him awkwardly on the elbow.")
        # Choice 1.1.3.2 - CASTLE.
        elif hagrid.lower() == "dash":
            print("You make it inside, but are immediately caught by Mrs. Norris. Filch is not far away of course, and the invisibility cloak doesn’t fit the three of you like it used to. You’re caught and Professor McGonagall puts you in detention. :(")
        else:
            print("Please try again. :)")
    else:
        print("Please try again. :)")
# Choice 1.2 - QUIDDITCH. 
elif evening.lower() == "quidditch":
    hospital_wing = input("Rotten luck!! You get hit by a bludger and spend 3 days in the hospital wing :( Hermione is not impressed with your choice to not study and refuses to lend you her notes. While you’re recovering in the hospital wing, you can either PLAY a game with Ron or catch up on HOMEWORK? ")
    # Choice 1.2.1 - PLAY.
    if hospital_wing.lower() == "play":
        choose_game = input("You and Ron are trying to decide what to play. Do you want to play WIZARD’S CHESS or EXPLODING SNAP? ")
        # Choice 1.2.1.1 - WIZARD'S CHESS.
        if choose_game.lower() == "wizard's chess":
            print("You put up a good fight, but of course Ron wins in the end. Oh well. At least you have your friends to hang out with while you recover. It certainly still beats doing homework.")
        # Choice 1.2.1.2 - EXPLODING SNAP. 
        elif choose_game.lower() == "exploding snap":
            print("Your game of exploding snap gets out of hand… Ron nearly burns off one of his eyebrows and you two are making such a ruckus that Madam Pomfrey kicks him out. You wait in the hospital wing alone while you heal. :( Perhaps you’ll take a nap…")
        else:
            print("Please try again. :)")
    # Choice 1.2.2 - HOMEWORK.
    elif hospital_wing.lower() == "homework":
        # CHANGE QUESTION FOR CHO CHANG. 
        ravenclaw_game = input("Your efforts soften Hermione and she decides to help you study. It pays off!! You’re now caught up on your homework and it’s good to have Hermione back. You recover just in time for the quidditch match against Ravenclaw. Do you start searching for the snitch on the LEFT or RIGHT side of the quidditch pitch? ")
        # Choice 1.2.2.1 - LEFT.
        if ravenclaw_game.lower() == "left":
            print("Crunch!! You get clobbered by another bludger and end up in the hospital wing again. You just can’t catch a break, can you? ")
        # Choice 1.2.2.2 - RIGHT.
        elif ravenclaw_game.lower() == "right":
            print("You see the snitch dancing around Cho Chang’s head. You dive towards her and catch it!! Gryffindor wins!! After the game she tells you she’s impressed with your flying. ;)")
        else:
            print("Please try again. :)")
    else:
        print("Please try again. :)")
else:
    print("Please try again. :)")