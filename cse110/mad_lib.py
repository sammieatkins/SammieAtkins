# Ask for story inputs.
print("Please enter the following: ")
adjective = input("adjective: ")
animal = input("animal: ")
verb1 = input("verb: ")
exclamation = input("exclamation: ")
verb2 = input("verb: ")
verb3 = input("verb: ")
adjective2 = input("adjective: ")

# Print story with user's inputs. 
# Used single quotes because there are double quotes in the story.
print(f'The other day, I was really in trouble. It all started when I saw a very {adjective.lower()} {animal.lower()} {verb1.lower()} down the hallway. "{exclamation.capitalize()}!" I yelled. But all I could think to do was to {verb2} over and over. Miraculously, that caused it to stop, but not before it tried to {verb3} right in front of my {adjective2} family. ')
