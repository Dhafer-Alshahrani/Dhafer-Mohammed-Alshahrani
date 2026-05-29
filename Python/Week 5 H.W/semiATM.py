print (""" 
    1 - Check balance
    2 - Deposit 100 SAR
    3 - Withdraw 50 SAR
    4 - Exit """)

num = int(input("Enter the function you want : "))
balance = 200

match num:
    case 1: 
        print(balance)
    case 2 :
        print(balance +100 )
    case 3:
        if balance >50:
            print(balance - 50 )
        else : 
            print("Insufficient funds")            
    case 4 :
        print("Goodpye!")        
    case _:
        print("Invalid choice ") 