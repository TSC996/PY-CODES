import random
objects = ['none','stone','paper','scissors']
a=input('stone,paper,scissors \n')
b=random.randint(1,3)
def start():
    if(a=='stone'):
        if(objects[b]==1):
            print('Its tie!')
        elif(objects[b]==2):
            print("You loose, Better luck next time!")
        elif(objects[b]==3):
            print("Yay!,You win.")
    elif(a=='paper'):
        if(objects[b]==1):
            print("Yay!,you win")
        elif(objects[b]==2):
            print("Its tie")
        else:
            print("You loose, Better luck next time!")
    elif(a=='scissors'):
        if(objects[b]==1):
            print("You loose, Better luck next time")
        elif(objects[b]==2):
            print("Yay!,you win")
        else:
            print('Its tie!')
start()