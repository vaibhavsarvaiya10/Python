sum = 0
def armpow(n,p):
	if n > 10:
		x = n % 10
		y = n // 10
		sum = pow(x,p) + armpow(y,p)
		return sum
	else:
		return pow(n,p)

var1=input("Enter a number : ")
var=int(var1)
size=len(var1)

print("Entered number :",var1)
print("Power :",size)
value=armpow(var,size)
print("Final number :",value)

if var == value:
	print("Armstong!")
else:
	print("Not armstrong!")
