age = int(input("how old are you?"))

if age < 18:
    print("You can't dring")
elif age >= 18 and age <= 35:
    print("You drink beer!")
elif age == 60 or age == 70:
    print("Birthday party!")
else:
    print("Go ahead!")
    
True and True == True
False and True == False
True and False == False
False and False == False
