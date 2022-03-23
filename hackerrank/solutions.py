
def diagonalDif(arr):
    dSum1=0
    dSum2=0
    for i in range(len(arr[0])):
        for j in range(len(arr[0])):
            if i == j:
                dSum1+=arr[i][j]
            if i+j==len(arr[0])-1:
                dSum2+=arr[i][j]
        
    return abs(dSum1-dSum2)

def staircase(n):
    # Write your code here
    for i in range(1,n+1):
        space=n-i
        for j in range(space):
            print("",end=" ")
        for x in range (i):
            print("#",end="")
        print("")

def miniMaxSum(arr):
    # Write your code here
    min=arr[0]
    max=arr[0]

    for i in arr:
        if i>=max:
            max=i
        if i<=min:
            min=i
    maxSum=0
    minSum=0
    for i in arr:
        if i!=max:
            minSum+=i
        else:
            max=0
        if i!=min:
            maxSum+=i
        else:
            min=0
    print(minSum,end=" "),print(maxSum)

def birthdayCakeCandles(candles):
    # Write your code here
    max=candles[0]
    for i in candles:
        if i>max:
            max=i
    
    return candles.count(max)

s="1234"
k=int(s[0:2])+2

print(k,type(k))