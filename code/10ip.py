a=[]
for i in range(10):
    num=int(input("Enter 10 numbers:"))
    a.append(num)
print(a)
tot_sum=sum(a)
print("The sum of given numbers",tot_sum)
av=tot_sum/10
print("The average of given numbers",av)

