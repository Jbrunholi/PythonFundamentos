a = 5
while a:
    print(a)
    a = a - 1
    if a == 2:
        break
    print("Ultimo statement do loop while")
print("Fora do Loop WHILE")

a = [1, 2, 3, 4, 5]
for i in a:
    print(i)
    if i == 3:
        break
    print("Ultimo statement do loop for")
print("fora do Loop FOR")