def Survive(n, k):
    men = [0] + [1] * (n - 1)
    i = count = 0
    kills = 1

    while kills < (n - 1):
        if men[i] == 1:
            count += 1
        if men[i] == 1 and count == k:
            men[i] = 0
            count = 0
            kills += 1
        i += 1
        if i >= n:
            i = 0
    return men
n = int(input('Введите количество выживающих '))
k = int(input('Очередность убийства '))
print(Survive(n, k))
