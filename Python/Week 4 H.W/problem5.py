age = int(input("Enter your age :"))
day = input("Enter the day : ")
CURRENCY = "SAR"
print("-"*20)

if day=="Tuesday":
    if age <12:
        print(f"you will pay 10 {CURRENCY}")
    elif 12<=age<=17:
         print(f"you will pay 25 {CURRENCY}")
    elif 17<age<=59:
         print(f"you will pay 40 {CURRENCY}")
    elif 60<age :
         print(f"you will pay 15 {CURRENCY}") 

elif day!="Tuesday" :
    if age <12:
        print(f"you will pay 20 {CURRENCY}")
    elif 12<=age<=17:
         print(f"you will pay 35 {CURRENCY}")
    elif 17<age<=59:
         print(f"you will pay 50 {CURRENCY}")
    elif 60<age :
         print(f"you will pay 25 {CURRENCY}") 

print("-"*20)
