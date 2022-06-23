x, y, z = map(int, input().split())

if x == y == z:
    price = 10000 + x * 1000
elif (x == y) or (x == z) or (y == z):
    if x == y:
        price = 1000 + x * 100
    if x == z:
        price = 1000 + x * 100
    if y == z:
        price = 1000 + y * 100
else:
    max_num = max([x, y, z])
    price = max_num * 100

print(price)
