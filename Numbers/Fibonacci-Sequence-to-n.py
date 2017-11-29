def fib(n):
    numList = []
    curr = 1
    prev = 0
    while len(numList)<n:
        numList.append(curr)
        curr, prev = curr + prev, curr
    print(*numList, sep='\n')

n = int(input('Enter number of digits\n'))
fib(n)



