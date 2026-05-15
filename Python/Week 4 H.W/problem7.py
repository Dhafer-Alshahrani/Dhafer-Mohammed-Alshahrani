age = int(input("Enter your age :"))
job=input("Do you have a job ? :")
if job=="False":
  print("Flase")
elif job=="True":
  print("True")
income = int(input("Enter your monthly income :")) 
print("-"*20)

print("""THIS IS THE CONDITIONS FOR LOANS :
      - Age must be between 21 and 65 (inclusive).
  - The applicant must have a job (answer "yes" or "no").
  - Monthly income (in SAR) determines the result:
       income >= 5000          -> "Approved"
       income between 3000 and 4999 -> "Approved with conditions"
       income below 3000       -> "Rejected: low income""")
print("-"*20)

if 21<=age<=65:
  if job=="True":
    if 5000<=income:
     print("Approved")
    elif 3000<=income<=4999:
      print("Approved with conditions")
    else:
      print("Rejected: low income") 
elif 21>age or age>65: # I prefered to separate them to be clear 
  print("age not eligible")
elif job=="False":
  print("no job")         

print("-"*20)
