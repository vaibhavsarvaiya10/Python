var1=10

num1=0
num2=1
sum=0

print(num1)
print(num2)

def fib(x,y,z):
    if(z>0):
        sum = x + y
        print(sum)
        x, y = y, sum
        fib(x,y,z-1)

fib(num1,num2,var1)
