#check whether the given numnber is armstrong or not

numb=input('Enter the number: ')
n=int(numb)
order=len(numb)
num=n
#print(order)
sum=0
while n>0:
    n1=n%10
    sum=sum+(n1**order)
    n=n//10
print(sum)     
if sum==num:
    print('Number is Armstrong')
else:
    print('Number is Not Armstrong')    
