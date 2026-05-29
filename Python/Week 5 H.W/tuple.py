# the First :
person = ("Sara", 25, "Riyadh")
print(person[0])
print(person[1])
print(person[2])
print(f""" 
Name : {person[0]}
Age : {person[1]}
City : {person[2]} """)


#===========================================================
# the Second :  
colors = ("red", "green", "blue")
#colors[0]=("yellow") # ROLE : in tuple you can not add or change any thing from the tuple .

print(len(colors))
print('red' in colors)

print(f""" 
Length : {len(colors)}
red is in tuple : {'red' in colors}""")