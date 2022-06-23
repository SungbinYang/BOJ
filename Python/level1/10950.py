count = int(input())
arr = []

for i in range(count):
    num1, num2 = map(int, input().split())
    arr.append(num1 + num2)
    
for i in arr:
    print(i)
