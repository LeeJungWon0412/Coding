t = int(input())

for i in range(1, t + 1, 1):
    a, b = map(int, input().split())
    print("Case #{:d}:".format(i), a + b)  
