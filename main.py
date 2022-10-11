n = int(input("Введите число\n"))
mas = []
for i in range (n+1):
    mas.append(i)
mas[1] = 0
i = 2
t = 0;
while (i <= n):
    if (mas[i] != 0):
        j = 2*i
        while (j <= n):
            mas[j] = 0
            t = j
            j += i
    i += 1
i -= 1
while (i > 0):
    if (mas[i] != 0):
        print(mas[i])
        break
    i -= 1