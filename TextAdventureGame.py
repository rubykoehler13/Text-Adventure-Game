intro_art = r"""
 _____                           _ _   
/  ___|                         (_) |  
\ `--. _   _ _ __ ___  _ __ ___  _| |_ 
 `--. \ | | | '_ ` _ \| '_ ` _ \| | __|
/\__/ / |_| | | | | | | | | | | | | |_ 
\____/ \__,_|_| |_| |_|_| |_| |_|_|\__|                                         
"""
print(intro_art)

While True:
    user_name = input("Hello, what is your name? ")
    print(f"Well, {user_name}, welcome to Summit. Let's see if you can reach the top...")
    print("You have decided to attempt the climb of Mt. Sammy which has been known near impossible;\n"
          "only a few people have successfully completed the summit, will you be another?")
    print("You get to the parking lot, and you experience a shiver that shoots down your spine.\n"
          "You look around, and see a sign that says you may only use one climbing tool on your climb,\n"
          "but you prepared to use two - A picaxe and a ski pole.")
    print("You may only bring one; this is your first decision to make.")
    print("a) Ski pole")
    print("b) Picaxe")

    user_choice1 = input("Which do you choose? (a/b): ")
    if user_choice1 == 'a':
        print("The ski pole is not a good form of protection.... Wrong choice.")
        break
    elif user_choice1 == 'b':
        print("Great choice! The picaxe has multiple uses and will be very helpful for your adventure.")

    print("Now that you have chosen your tool, you make sure you have your backpack,\n"
          "and you're ready to go. ")
    print("As you start at the bottom of the mountain, you encounter another decision to be made.\n"
          "There are two paths, no signs telling you which one to take.")
    print("a) Left path")
    print("b) Right path")
    user_choice2 = input("Which do you choose? (a/b): ")
    if user_choice2 == 'a':
        print("Awesome, you have chosen the left path! You can continue.")
    elif user_choice2 == 'b':
        print("Great, you have chosen the right path! You may continue.")