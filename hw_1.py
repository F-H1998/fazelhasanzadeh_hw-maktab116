n = int(input("pl enter number... "))
sum_1 = 0
for i in range(1, n):
    if n % i == 0:
        sum_1 += i
if sum_1 == n:
    print("YES")
else:
    print("NO")
