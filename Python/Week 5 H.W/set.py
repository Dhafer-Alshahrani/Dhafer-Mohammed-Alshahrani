# the First :

colors = {"red", "blue", "green"} 
colors.add("yellow")
print(colors)
colors.add("red")
print(len(colors))
color=colors.isdisjoint("yellow")
colorr =colors.isdisjoint("red")
print(f"""
Size: {len(colors)},
Red in set: {color},
yellow in set: {colorr} """)
# The expected output`:`
print(f"""
size: {len(colors)} , 
red in set: {colors.isdisjoint('red')} , 
yellow in set:  {colors.isdisjoint('yellow')}""")

#===========================================================


# the Second :  
nums = [1, 2, 2, 3, 4, 4, 5, 1]
make =set([1, 2, 2, 3, 4, 4, 5, 1])
make1= len(make)
# The expected output`:`
print(f"""
unique values : {make},
Count of unique values: {make1}""")

#===========================================================
 # the Third :  
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
d1 =a.union(b)
d2 =a.intersection(b)
d3 = a.difference(b)
# The expected output`:`
print(f"""
Union : {d1},
Intersection : {d2},
In a but Not in b : {d3}""")

