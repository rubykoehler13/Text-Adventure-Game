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

def encounter_one(player_info):
    user_choice1 = input(f"{player_info[0]}, which do you choose? (a/b): ").lower()
    while True:
        if user_choice1 == 'a':
            print("The ski pole is not a good form of protection.... Wrong choice.")
            continue
        elif user_choice1 == 'b':
            print("Great choice! The picaxe has multiple uses and will be very helpful for your adventure.")
            break
    encounter_two(player_info)

def encounter_two():


def main():
    player_info = [user_name, 100]
    encounter_one(player_info)
    print("Now that you have chosen your tool, you make sure you're ready to go. ")
    print("As you start at the bottom of the mountain, you encounter another decision to be made.\n"
                  "There are two paths, no signs telling you which one to take.")
    print("a) Left path")
    print("b) Right path")
    user_choice2 = input("Which do you choose? (a/b): ").lower()
    blah = random.randint(1,2)
    if user_choice2 == 'a':
        print("Awesome, you have chosen the left path! You can continue.")
        if blah == 1:
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
                print("a) Accept the lunch and walk inside")
                print("b) Decline the lunch but say thank you for the offer")
                user_choice4 = input("Which do you choose? (a/b): ")
                while True:
                    if user_choice4 == "a":
                        print("The man smiles and makes room for you to come inside.")
                    elif user_choice4 == "b":
                        print("The man seems to be hurt, but tries not to show it. He closes the door.")
                    else:
                        print("Please input a valid answer.")
                        continue
            if user_choice3 == "b":
                print("You have chosen to leave the house alone and keep climbing the mountain. \n"
                      "Just maybe a minute later after walking past the house, you trip a little bit.\n"
                      "You're just so tired and really need to sit down at this point. You see a great little spot just up ahead.\n"
                      "You finally sit down and take off your backpack. You're able to drink water or eat a snack.")
                print("a) Drink water")
                print("b) Eat a snack")
                user_choice_4 = input("Which do you choose? (a/b): ").lower()
                while True:
                    if user_choice_4 == "a":
                        print("You feel a little bit better, and after sitting for a second more, you start back on your climb.")
                    elif user_choice_4 == "b":
                        print("You feel a little bit better, and after sitting for a second more, you start back on your climb.")
                    else:
                        print("Please input a valid answer.")
                        continue
        if blah == 2:
            print("You've started your climb. You suddenly get very hungry. You remember that you have some small snacks in your backpack,\n"
                  "so you ")


    elif user_choice2 == 'b':
        print("Great, you have chosen the right path! You may continue.")
        if blah == 2:
            pass