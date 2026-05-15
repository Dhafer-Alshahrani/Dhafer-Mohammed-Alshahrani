num = int(input("Enter a number :"))
print("-"*20)

print (""" THIS IS THE SYSTEM TO MEASURE THE NUMBER SIGN AND MAGANITUDE :
        - "Negative large"  if the number is less than -100
  - "Negative small"  if the number is between -100 and 0 (not 0)
  - "Zero"            if the number is exactly 0
  - "Positive small"  if the number is between 0 and 100 (not 0)
  - "Positive large"  if the number is greater than 100""")
print("-"*20)
if num<-100:
    print("The number is Negative large")
elif -100<=num<0:
    print ("The number is Negative small")    
elif num==0:
    print ("The number is Zero") 
elif 0<num<=100:
    print ("The number is Positive small")
elif 100<num:
    print ("The number is Positive large")            

print("-"*20)
