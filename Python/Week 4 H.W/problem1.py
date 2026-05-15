grade=int(input("Enter your Grade :"))
print("-"*20)


print ("""The letter grade is 
 - 90 to 100  -> A
  - 80 to 89   -> B
  - 70 to 79   -> C
  - 60 to 69   -> D
  - below 60   -> F""")
print("-"*20)
if grade>90:
        print(f"And you're grade is A")
elif 80<=grade<=90:
        print(f"And you're grade is B")
elif 70<=grade<80:
        print(f"And you're grade is C")
elif 60<=grade<70:
        print(f"And you're grade is D")
elif grade<60:
        print(f"And you've failed")
print("-"*20)
