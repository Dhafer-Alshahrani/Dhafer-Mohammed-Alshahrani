print("|||HERE IS THE ROCK , PAPER AND SCISSORS GAME|||")
print("-"*20)

n1 = input("Enter your method : ")
n2 = input("Enter your method : ")

print("-"*20)

if n1=="rock":
    if n2=="scissors":
        print("Player 1 beats Player 2")
    elif n2=="paper":
        print("Player 2 beats Player 1")
    elif n2=="rock":
        print("This game is Tie")    # I have mereg all the conditions into one nested loop
elif n1=="paper":
    if n2=="rock":
        print("Player 1 beats Player 2")
    elif n2=="scissors":
        print("Player 2 beats Player 1") 
    elif n2=="paper":
        print("This game is Tie")       
elif n1=="scissors":
    if n2=="paper":
        print("Player 1 beats Player 2")
    elif n2=="rock":
        print("Player 2 beats Player 1")
    elif n2=="scissors":
        print("This game is Tie")     


print("-"*20)
