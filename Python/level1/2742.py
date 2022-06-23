import sys

n = int(sys.stdin.readline())

if n <= 100000:
    for i in range(n):
        print(n - i)
