n = int(input("pl enter number.... "))
if n <= 0:
    print("NO")
else:
    while n % 2 == 0:
        n = n // 2
    if n == 1:
        print("YES")
    else:
        print("NO")
