def isdead():
    dead = input("Are you dead? ")
    if dead == "yes":
        print("You are dead")
    elif dead == "no":
        print("You are not dead")
    else:
        print("Please answer yes or no")
        isdead()

isdead()
