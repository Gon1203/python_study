from random import randint

print("Welcom to Python Casino")
pc_choice = randint(1,50)

playing = True

while playing:
    user_choice = int(input("Choose number:"))
    if user_choice == pc_choice:
        print("You win!")
        playing = False
    elif user_choice > pc_choice:
        print("Lower!")
    else:
        print("Higher!")
        
        

