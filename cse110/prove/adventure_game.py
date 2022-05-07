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
            print("")
        # Choice 1.1.1.2 - HONEYDUKES. 
        if next_shop.lower() == "honeydukes":
            print("")
        
    # Choice 1.1.2 - GROUNDS.
    if celebrate.lower() == "grounds":
        fight = input("While the three of you are relaxing under a tree, minding your own business, Malfoy, Crabbe, and Goyle decide to try and steal your snacks. You only have time for one spell. Do you use EXPELLIARMUS or ACCIO? ")
        # Should one of these end in losing the snacks?
        # Choice 1.1.2.1
        if fight.lower() == "expelliarmus":
            print("Success!! You’ve stolen Malfoy’s wand. Goyle fights you for it and gives it back to Malfoy. At this point you’ve gotten the attention of the people around you and Malfoy realizes he’s lost this round. They meander back to the castle, bullying some first years as they go.")
        # Choice 1.1.2.2
        if fight.lower() == "accio":
            print("Crabbe and Goyle have stolen your snacks, but luckily you’re just as fast and snatch them right back using accio. Unfortunately, that gave them the same idea. You go back and forth with accio until Hermione steps in and uses the protego charm to stop them from getting the snacks again. What would you do without her :) ")
        # Hidden choice 1.1.2.3
        if fight.lower() == "stupefy":
            print("All three of you think of the same spell: stupefy! The poor slytherins didn’t have a chance. You send their limp bodies flying down the hill so you can continue enjoying your evening, and your snacks :)")
        # Hidden Choice 1.1.2.4
        if fight.lower() == "petrificus totalus":
            print("You catch Malfoy right as he’s about to snatch your Bertie Bott’s Every Flavor Beans. Now stiff as a board lying face first in the dirt, Crabbe and Goyle drag him all the way back to the castle. They would perform the counter curse, but they don’t know how. You, Ron, and Hermione can’t stop laughing :) ")

    # Choice 1.1.3 - HAGRID.
    if celebrate.lower() == "hagrid":
        # change name of hagrid variable to match question.
        hagrid = input("You each fill Hagrid in on your test scores and he’s so happy for you all. He rewards you with three rock cakes each. ")
        # Choice 1.1.3.1

        # Choice 1.1.3.2

# Choice 1.2 - QUIDDITCH. 
if evening.lower() == "quidditch":
    hospital_wing = input("Rotten luck!! You get hit by a bludger and spend 3 days in the hospital wing :( Hermione is not impressed with your choice to not study and refuses to lend you her notes. While you’re recovering in the hospital wing, you can either PLAY a game with Ron or catch up on HOMEWORK? ")
    # Choice 1.2.1 - PLAY.
    if hospital_wing.lower() == "play":
        choose_game = input("You and Ron are trying to decide what to play. Do you want to play WIZARD’S CHESS or EXPLODING SNAP? ")
        # Choice 1.2.1.1 - WIZARD'S CHESS.
        if choose_game.lower() == "wizard's chess":
            print("You put up a good fight, but of course Ron wins in the end. Oh well. At least you have your friends to hang out with while you recover. It certainly still beats doing homework.")
        # Choice 1.2.1.2 - EXPLODING SNAP. 
        if choose_game.lower() == "exploding snap":
            print("Your game of exploding snap gets out of hand… Ron nearly burns off one of his eyebrows and you two are making such a ruckus that Madam Pomfrey kicks him out. You wait in the hospital wing alone while you heal. :( Perhaps you’ll take a nap…")
    # Choice 1.2.2 - HOMEWORK.
    if hospital_wing.lower() == "homework":
        # CHANGE QUESTION FOR CHO CHANG. 
        cho_chang = input("Your efforts soften Hermione and she decides to help you study. It pays off!! You do so well in your charms exam that you catch the attention of Cho Chang ;) When you see her again in the next D.A. meeting, do you go TALK to her or ADMIRE her from afar? ")
        # Choice 1.2.2.1
        if cho_chang.lower() == "talk":
            print("")
        # Choice 1.2.2.2
        if cho_chang.lower() == "admire":
            print("")