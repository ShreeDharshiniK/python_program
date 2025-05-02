
operation=input("add/sub/mul/div:")
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))



if(operation=="add"):
    print(a+b)
elif(operation=="sub"):
    print(a-b)
elif(operation=="mul"):
    print(a*b)
elif(operation=="div"):
    print(a/b)
else:
    print("Invalid Operation")
