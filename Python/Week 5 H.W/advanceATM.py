MANAGED_BY_DHAFER = 1
CURRENCY ="SAR"
balance = 1000
print(f"""
1 - Show Balance
2 - Deposit
3 - Withdraw
0 - Exit""")
t1 = int(input("Choose an option:  "))
for i in range(1): 
    if t1==1:
        print(f""" You have a Now you have a {balance}{CURRENCY} in balance""")
        print(f""" Do you want to contiue : 
1 - Deposit
2 - Withdraw
3 - Exit""")
        f1 = int(input("What do you want to do : "))
        if f1==1:
            print("With this option you are willing to deposit an amount of money")
            print(f"""choose an amount: 
             1: 50
             2: 100
             3: 200
             4: 500 """)
            d1 =int(input("What do you want to deposit:  "))
            for x in range(1): 
             if d1==1:
                 print(f"""Now you have a {balance + 50}{CURRENCY}""")
             elif d1==2:
                 print(f"""Now you have a {balance + 100}{CURRENCY}""")    
             elif d1==3:
                 print(f"""Now you have a {balance + 200}{CURRENCY}""")
             elif d1==4:
                 print(f"""Now you have a {balance + 500}{CURRENCY}""")
             else : 
                 print("invalid amount")  
        elif f1==2:
            a1 = int(input("What is the amout you want to withdraw :"))
            if a1<=balance:
               print(f"""This is your balance now : {balance - a1}""")
            elif a1>balance:
              print(f"""{a1} is more then your balance """)
        elif f1==3:
             print("Goodpye!")
        else : 
                print("invalid amount") 
    elif t1==2:
            print("With this option you are willing to deposit an amount of money")
            print(f"""choose an amount: 
             1: 50
             2: 100
             3: 200
             4: 500 """)
            d1 =int(input("What do you want to deposit:  "))
            for d in range(1): 
             if d1==1:
                 print(f"""Now you have a {balance + 50}{CURRENCY}""")
             elif d1==2:
                 print(f"""Now you have a {balance + 100}{CURRENCY}""")    
             elif d1==3:
                 print(f"""Now you have a {balance + 200}{CURRENCY}""")
             elif d1==4:
                 print(f"""Now you have a {balance + 500}{CURRENCY}""")
             else : 
                 print("invalid amount")  
                 break
             print(f""" Do you want to contiue : 
1 - Withdraw
2 - Exit""")
            k1 = int(input("What do you want to do : "))
            for k in range(1): 
                if k1==1:
                 a1 = int(input("What is the amout you want to withdraw :"))
                 if a1<=balance:
                   print(f"""This is your balance now : {balance - a1}""")
                 elif a1>balance:
                   print(f"""{a1} is more then your balance """)
                elif k1==2:
                 print("Goodbye!")
                else:
                 print("invalid amount")          
    elif t1==3:
        a1 = int(input("What is the amout you want to withdraw :"))
        if a1<=balance:
            print(f"""This is your balance now : {balance - a1}""")
        elif a1>balance:
            print(f"""{a1} is more then your balance """)
        else : 
             print("invalid amount")
             break
        print(f""" Do you want to contiue : 
1 - Show balance
2 - Deposit
3- Exit""")  
        ha1 =int(input("What do you want to do : "))
        for h in range(1):
          if ha1==1:
                 print(f""" You have a Now you have a {balance}{CURRENCY} in balance""")
          elif ha1==2:
            print("With this option you are willing to deposit an amount of money")
            print(f"""choose an amount: 
             1: 50
             2: 100
             3: 200
             4: 500 """)
            d1 =int(input("What do you want to deposit:  "))
            for x in range(1): 
             if d1==1:
                 print(f"""Now you have a {balance + 50}{CURRENCY}""")
             elif d1==2:
                 print(f"""Now you have a {balance + 100}{CURRENCY}""")    
             elif d1==3:
                 print(f"""Now you have a {balance + 200}{CURRENCY}""")
             elif d1==4:
                 print(f"""Now you have a {balance + 500}{CURRENCY}""")
             else : 
                 print("invalid amount")    
          elif ha1==3:
              print("Goodbye!")

          else:
              print("Invalid amount")            
    elif t1==0:
        print("Goodbye!")   
 

