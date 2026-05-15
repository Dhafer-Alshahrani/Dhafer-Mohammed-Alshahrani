n1=int(input("Enter value1 :"))
n2=int(input("Enter value2 :"))
n3=int(input("Enter value3 :"))
print("-"*20)
print(f"This is your degrees ({n1},{n2},{n3})")
print("-"*20)
if n1==n2==n3 :
 print("Equilateral")
elif (n1==n2 ) :
  print("Isosceles")
elif (n1==n3) :
  print("Isosceles") 
elif (n2==n3) :
  print("Isosceles")   
else :
 print ("Scalene")