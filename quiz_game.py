print("Welcomee to my computer Quiz!")

playing = input("Do you want to play?.. ")

if playing.lower() != "yes":
    quit()
    
print("Okay! Let's Play:)")
score = 0

                # first quiz 
                
answer = input("what does CPU Stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score +=1
else:
    print("Incorrect!")
    
                    # second quiz 
    
answer = input("what does GPU stand for? ")
if answer.lower() == "graphical processing unit":
    print('Correct!')
    score +=1
else:
    print("Incorrect!")
    
                    # third quiz 
    
answer = input("what does RAM Stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score +=1
else:
    print("Incorrect!")
    
                        # fourth quiz 
    
answer = input("what does ROM Stand for? ")
if answer.lower() == "random only memory":
    print('Correct!')
    score +=1
else:
    print("Incorrect!")

                # fifth quiz 

answer = input("what does PSU Stand for? ")
if answer.lower() == "power supply unit":
    print('Correct!')
    score +=1
else:
    print("Incorrect!")

        # Result score here 
print("You Got!",score,"out of 4")
print("You Got", score / 4 * 100,"%. right answer")
    