import sys

count = int(sys.stdin.readline())
arr = []

for i in range(count):
    num1, num2 = map(int, sys.stdin.readline().split())
    
    arr.append(num1 + num2)

for i in arr:
    print(i)
