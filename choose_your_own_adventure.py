name = input("Type Your Name: ")
print("Welcome",name,"to this adventure!")


answer = input("You are on a dirt road, it has come to an end and you can go left or right . which way would you like to go?").lower()

if answer == "left":
    answer = input("You come to a river, you walk around or swim accross? Type walk to walk around and swim to swim to swim accross: ").lower()
    
    if answer == 'swim':
        print("You swan across and were eaten by an alligator.")
    
    elif answer == 'walk':
        print("You walked for many miles,ran out of water and you lost the game.")
        
    else:
        print("Not a valid option. You lose")
    
elif answer == "right":
    answer = input("You come to a bridge,it looks wobbly, do you want to cross it or head back (cross/back)?").lower()
    
    if answer == 'back':
            print("You go back and lose.")
    
    elif answer == 'cross':
        answer = input("You cross the bridge and meet a strenger. Do you talk to them").lower()
        if answer == "yes":
            print("You talk to the stranger and they give you gold. You Win!")
        
        elif answer == "no":
            print("You ignore the stranger and they are offended. You lose!")
        
        else:
            print("Not a valid option. You Lose!")
        
    else:
        print("Not a valid option. You lose")

else:
    print("Not a valid option. You lose")
    
print("Thank You for trying" + name)

