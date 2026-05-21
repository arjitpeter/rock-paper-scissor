import random
elements = ["rock", "paper", "scissor"]
comp = random.choice(elements)
human = str(input("pick your element(rock/paper/scissor):- ")).lower()

# .lower() is used to fix the problem is human enters their element in caps
# not in command is used to filter out the other words except rock paper and scissor

if human not in elements:
    print("pick from the rock paper scissor")

#now we can run the logic

else:
    if human == comp:
        print(f"comp chose {comp} and its a tie")
    elif human != comp:
        if human == elements[0] and comp == elements[1]:
            print(f"comp chose {comp}, you lost")
        elif human == elements[0] and comp == elements[2]:
            print(f"comp chose {comp}, you won")
        elif human == elements[1] and comp == elements[0]:
            print(f"comp chose {comp}, you won")
        elif human == elements[1] and comp == elements[2]:
            print(f"comp chose {comp}, you lost")
        elif human == elements[2] and comp == elements[0]:
            print(f"comp chose {comp}, you lost")
        elif human == elements[2] and comp == elements[1]:
            print(f"comp chose {comp}, you won")