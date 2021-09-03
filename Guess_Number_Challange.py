# we import here random number 
# and create a Game which name is guess number challange
# so try it


import random 
number = random.randint(1,1000)
start = 0

while True:
    input_number = int(input("Guess The Number(between 1 to 1000):"))
    start += 1
    if input_number == number:
        print("Congragulation!! Your Guess is Correct!")
        break
    elif input_number > number:
        print("Incorrect! Please Enter a smaller Number")
    else:
        print("Incorrect! Please Enter a larger number")
print("you tried", start, "Times to find the correct number")