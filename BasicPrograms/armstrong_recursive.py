sum = 0
# defining a function that takes two values as parameters, 1) user unput value and 2) the power or the length of the digits
def armpow(n,p):
	if n > 10:
		x = n % 10
		y = n // 10
		# below approach defines that we are using recursive approach for this program that is, function calling itself to perform recursion
		sum = pow(x,p) + armpow(y,p)
		return sum
	else:
		return pow(n,p)

# taking input from a user in a string format so we can easily use the len function of string and get the power that will be used further
var1=input("Enter a number : ")

# converting the user input string to number
var=int(var1)
size=len(var1)

print("Entered number :",var1)
print("Power :",size)
value=armpow(var,size)
print("Final number :",value)

# condition to check if the user input value and the final power value is the same or not, if same then it is armstrong number
if var == value:
	print("Armstong!")
else:
	print("Not armstrong!")
