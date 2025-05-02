a=int(input("Enter your salary:"))
b=int(input("Enter your age:"))
if(a>=20000 or b<=25):
    loan=int(input("Enter loan amount:"))
    if(loan<=50000):
        print("You are eligible for loan")
    if(loan>50000):
        print("Maximum loan amount is 50000")
else:
    print("You are not eligible for loan")

