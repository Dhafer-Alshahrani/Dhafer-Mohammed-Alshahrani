# the First :
student = {"name": "Ali", "age": 17, "grade": "11"}
print(student["name"])
print(student["age"])
print(student["grade"])
# The expected output`:`

print(f"""
Name : {student['name']} 
Age : {student['age']}
Grade : {student['grade']}""")
#===========================================================
  # the Second :  
prices = {"apple": 3, "banana": 2}
prices["mango"]=5
prices["apple"]=4
# The expected output`:`
print(prices)
#===========================================================
 # the Third :  
user = {"name": "Sara", "email": "sara@example.com", "city": "Jeddah"}

print(user.keys())
print("name" in user)
print("phone" in [user])
# The expected output`:`
print(f'''
Keys : {user.keys()}
Sara in dict : {"name" in user}
Phone in dict : {"phone" in user}''')
