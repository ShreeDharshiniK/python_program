a=int(input("Enter your tamil mark:"))
b=int(input("Enter your english mark:"))
c=int(input("Enter your maths mark:"))
d=int(input("Enter your science mark:"))
e=int(input("Enter your Social marks:"))
add=(a+b+c+d+e)
avg=(add/5)
if(avg<35):
    print("Additional class is required")
else:
    print("You are good to go")
