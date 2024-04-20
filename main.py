# print("python is great")

# this is comment

# print(input("Name : "))
# input() returns the string data type.

# name=input("Enter your name: ")
# age=input("Enter your age: ")
# print("You are "+name+" and "+age+" years old.")

# circle area calculator (PI r**2)
PI=3.142
r=int(input("Enter the radius value: "))
# print("The area of the circle is: "+area)
# TypeError: can only concatenate str (not "float") to str
area=str(PI*r**2)
print("The area of the circle is: "+area)
