sum = 0

def test(num):
    if num > 10:
        x = num % 10
        y = num // 10
        sum = x + test(y)
        return sum
    else:
        return num

var1 = input("Enter a number : ")

print(var1)
print(len(var1))

var2 = int(var1)

print(test(var2))
