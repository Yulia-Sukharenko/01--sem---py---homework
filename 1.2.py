def MOD():
    a = int(input())
    b = int(input())
    m = int(input())

    Summa = 0

    while b > 0:
        if b % 2 == 1:
            Summa = (Summa + a) % m
        a = (a * 2) % m
        b //= 2

    print('Ответ: ' , Summa)
MOD()