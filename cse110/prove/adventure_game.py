contact = input("You're a junior in high school and prom is coming up!! You're in need of a date. Luckily, you have your crush's number. Do you TEXT or CALL them? ")
contact = contact.lower()
if contact == "text":
    print("You text them and there's no response...")
    response = input("Do you want to WAIT or send another MESSAGE? ")
    response = response.lower()
elif contact == "call":
    print("It rings... and rings... and it goes to voicemail :/")
    call_reaction = input("Do you want to leave a VOICEMAIL or CALL again? ")
else:
    print("Your indecision made your crush realize they don't want to go to prom with you. :( Bummer dude")
