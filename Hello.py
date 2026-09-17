print("Hello world")
print("rahul mali")

#variable is container x=10, value can change to 15, 10, or anything

name = "Rahul" # Rahul name will get save in variable name [name]
#print(name)
name = "Shradha" # no need to give data type, python will automatically detect the data type    
print(name)
print(type(name)) # to check the data type of variable
#your_name = input("Enter your name: ")
#print("Hello", "Your name is", your_name)

#age = input("Enter your age:")
#print("Hello", "Your age is", age)

#new_age = int(age) + 1
#print("your new age is", new_age)

print(1 + 2.5) # 3.5 (Type Conversion) Implicit
print(1 + int(2.5)) # 3 (Type Casting) Explicit

#a = input("Enter first number: ")
#b = input("Enter second number: ")
#sum = int(a) + int(b)
#print(sum )

#string operation
#full_name = "Rahul Mali"
#print(full_name.upper()) 
#print(full_name.lower())

Revenue =[10,20,30,40]

for rev in Revenue:
    #print("Revenue values are", rev)
    print(f"Revenue:{rev}")