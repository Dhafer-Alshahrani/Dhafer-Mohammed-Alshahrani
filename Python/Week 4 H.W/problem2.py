import math
year=int(input("Enter a year :"))
leap = year/4
leap1=year/100
leap2=year/400
print("-"*20)

print (leap)
print (leap1)
print (leap2)


print("-"*20)


print ("""The measurment  is: 
       -if the year accept the division by 4 it is a leap year
-if the year accept the division by 100 it's not a leap year , unles it can be divided by 400.
       Examples : 
       2000 = is a leap year 
       1900 = is not a leap year 
""")
print("-"*20)
if  year%100==0:
    if year%400==0:
        print("The year is a leap year1") 
    else : 
        print("The year is not a leap year2")
elif year%4==0:
       print("The year is a leap year3")
else : 
      print("The year is not a leap year4")



