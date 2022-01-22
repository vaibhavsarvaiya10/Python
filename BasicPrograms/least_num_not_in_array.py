def solution(A):
    # write your code in Python 3.6
    for i in range(0,100):
        if i not in A:
            print(i)
            break


lim=int(input("Enter limit : "))
arr=[]
for j in range(lim):
    val=int(input("Enter a value : "))
    arr.append(val)

solution(arr)