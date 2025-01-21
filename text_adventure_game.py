import random
intro_art = r"""
 _____                           _ _   
/  ___|                         (_) |  
\ `--. _   _ _ __ ___  _ __ ___  _| |_ 
 `--. \ | | | '_ ` _ \| '_ ` _ \| | __|
/\__/ / |_| | | | | | | | | | | | | |_ 
\____/ \__,_|_| |_| |_|_| |_| |_|_|\__|                                         
"""
print(intro_art)

user_name = input("Hello, what is your name? ").title()
print()
print(f"Well, {user_name}, welcome to Summit. Let's see if you can reach the top...")
print("You have decided to attempt the climb of Mt. Shadowspire which has been known near impossible;\n"
              "only a few people have successfully completed the summit, will you be another?")
print("You get to the parking lot, and you experience a shiver that shoots down your spine.\n"
              "You look around, and see a sign that says you may only use one climbing tool on your climb,\n"
              "but you prepared to use two - A picaxe and a ski pole.")

print()

print("You may only bring one; this is your first decision to make.")
print("a) Ski pole")
print("b) Picaxe")

player_info = [user_name.title()]
while True:
    user_choice1 = input(f"{player_info[0]}, which do you choose? (a/b): ").lower()
    if user_choice1 == 'a':
        print("The ski pole is not a good form of protection.... Wrong choice.")
        continue
    elif user_choice1 == 'b':
        print("Great choice! The picaxe has multiple uses and might be helpful for your adventure.")
        break
    else:
        print("Please input a valid answer.")
        continue
print()
print("Now that you have chosen your tool, you make sure you're ready to go. ")
print("As you start at the bottom of the mountain, you encounter another decision to be made.\n"
      "There are two paths, no signs telling you which one to take.")
print()
print("a) Left path")
print("b) Right path")
print()
blah = random.randint(1,2)
print("The game has decided to choose your destiny for you!")
print()
if blah == 1:
    print("It has decided you take the left path!")
    print()
    print("Now, you start your climb. After you've walked for a couple\n"
                  "of minutes, you're already getting tired and want to sit down\n"
                  "even just for a second. You keep walking, take a turn and suddenly\n"
                  "see a very small house. You walk closer to it, do you knock on the door\n"
                  "or leave it alone?")
    print("a) Knock on the door")
    print("b) Leave it alone and keep climbing")
    user_choice3 = input("Which do you choose? (a/b): ").lower()
    if user_choice3 == "a":
        print("You have chosen to knock on the door! You wait a second,\n"
                      "and hear creaking within the house. A man slowly opens the door\n"
                      "and given that rarely anyone comes up to him or his house, \n"
                      "he acts a little hesitant. But he sees that you're tired and must be freezing. \n"
                      "He offers you to come inside and have a quick lunch that he's made.\n"
                      "Do you accept?")
        print()
        print("a) Accept the lunch and walk inside")
        print("b) Decline the lunch but say thank you for the offer")
        user_choice4 = input(f"{player_info[0]}, which do you choose? (a/b): ").lower()
        while True:
            if user_choice4 == "a":
                print("The man smiles and you go eat lunch with him. He's a very nice man, \n"
                      "and you have a great meal! Once you're done eating, you show him your appreciation, \n"
                      "and go continue your climb.")
                break
            elif user_choice4 == "b":
                print("The man understands, and he closes the door. You continue your adventure!")
                break
            else:
                print("Please input a valid answer.")
                continue
    if user_choice3 == "b":
        print("You have chosen to leave the house alone and keep climbing the mountain. \n"
                      "Just maybe a minute later after walking past the house, you trip a little bit.\n"
                      "You're just so tired and really need to sit down at this point. You see a great little spot just up ahead.\n"
                      "You finally sit down and take off your backpack. You're able to drink water or eat a snack.")
        print()
        print("a) Drink water")
        print("b) Eat a snack")
        user_choice_4 = input("Which do you choose? (a/b): ").lower()
        while True:
            if user_choice_4 == "a":
                print("You feel a little bit better, and after sitting for a second more, you start back on your climb.")
                break
            elif user_choice_4 == "b":
                print("You feel a little bit better, and after sitting for a second more, you start back on your climb.")
                break
            else:
                print("Please input a valid answer.")
                continue
elif blah == 2:
    print("It has decided you will take the right path!")
    print()
    print("Now, you start your climb. You've walked a decent amount, and are about 1/2 of the way up the mountain!\n"
              "Although suddenly, you hear a sound that you believe comes from an animal...\n"
              "You look around, and hear it again from a nearby cave. Should you go investigate or leave it alone?")
    print()
    print("a) Investigate the sound")
    print("b) Leave it alone and hope to not encounter the supposed animal in the future")
    user_choice_6 = input(f"{player_info[0]}, which do you choose? (a/b): ").lower()
    print()
    while True:
        if user_choice_6 == "a":
            print("You decided to investigate the sound. You start to walk towards the cave and hear the sound again, \n"
                      "but this time it scares you a lot. Again, you have no idea what animal this is, if it even is one.\n"
                      "Do you still wish to continue investigating?")
            print()
            print("a) Keep investigating!")
            print("b) Turn around")
            user_choice_7 = input("Which do you choose (a/b): ").lower()
            if user_choice_7 == "a":
                print("Perfect, you decided to continue searching for what made the sound. \n"
                          "You get to the mouth of the cave and see something hiding in the dark. It's quite small, \n"
                          "and continues to make a sound, except this time it sounds like whatever is making it, is in pain. \n"
                          "You walk up to it, getting closer and closer, as your heart beats faster and faster. \n"
                          "You finally get a good look at it... It's a small dog! You immediately feel the adrenaline go away, \n"
                          "and reach out your hand for the dog to smell you. He likes you! You pet him and try to see what's hurting him. \n"
                          "It's a little twig stuck in his foot:( You try to hold him still and take it out, he whines a little bit, \n"
                          "but let's you do it. After not too long, you've taken the twig out, and the dog jumps up to give you lots of kisses! \n"
                          "You think for a second about what you're next plan of action is. You decide to help him up but not take him with you on your \n"
                          "continuing adventure to the summit. You give the dog a very small amount of water you have, and walk back out of the cave.")
                break
            elif user_choice_7 == "b":
                print("Interesting choice. You turn around and continue your climb as the sound starts to fade away until you can't hear it at all anymore.")
                break
            else:
                print("Please input a valid answer.")
                continue
        elif user_choice_6 == "b":
            print("You chose to leave the supposed animal alone, so you continue your climb.")
    print()
print("You're getting very close to the summit... unusual.\n"
      "There's one last challenge you encounter. There is a mountain lion that lives about 50 meters from the summit itself, \n"
      "and this is where many people have failed. There's a 50/50 chance you survive and get around the lion. Again, this is up to fate.")
print("You walk a couple feet more, and finally see the lion. The question is do you wake it up, and that be the last thing you do, \n"
      "or do you get around it without disturbing its slumber and make it to the summit!? We shall see....")
print("You walk closer and closer, trying to be as quiet as possible. You end up having to walk within feet of the lion! Suddenly you trip! \n"
      "You put your hand over your mouth as to not let out a scream.")
print()
last_challenge = random.randint(1, 2)
while True:
    if last_challenge == 1:
        print("Very slowly, you turn your head to the lion to see if it has woken up... \n"
            "Your trip did not wake up the lion! As quietly as possible, you let out a sigh and remove your hand. \n"
            "Your heart rate drops, and you continue walking up. You're just feet from the summit!\n"
            "It has gotten significantly harder to breathe as you've climbed, but never as hard as it is now, but it seems...\n"
            f"{player_info[0].upper()}, YOU MADE IT TO THE SUMMIT!!!!! Congratulations, you are one of very few to accomplish this climb!")
        print("You catch your breath - as best you can - and look around; it's the most beautiful scenery you've ever seen.\n"
            "Now the question is can you get back down...? \n"
            "Good luck;)")
        break
    elif last_challenge == 2:
        print("Very slowly, you turn your head to the lion to see if it has woken up... \n"
              "Unfortunately, your trip has awoken the lion. \n"
              "Now it's the one slowly turning its head to you, and as it jumps at you, that's the last thing you see. \n"
              f"Unfortunately {player_info[0]}, you did not reach the summit, and have become one of many who have failed this climb. \n"
              "Better luck next time.")
        break
print()

print("THE END")