def Fibs_system(x):
    Fib_nom = [1, 2]
    i = 2
    while (Fib_nom[-1] < x): #заполняем массив числами Фиббоначи пока не будет числа больше введенного
        Fib_nom.append(Fib_nom[i-1] + Fib_nom[i-2])
        i += 1
    Fib_nom = Fib_nom[::-1] #переворачиваем массив, чтобы удобнее было работать с числами
    ans = ''
    for i in range(len(Fib_nom)): #переводим введенное число в систему счисления Фиббоначи с помощью предыдущего массива
        if Fib_nom[i] > x:
            ans += '0'
        if Fib_nom[i] <= x:
            ans += '1'
            x -= Fib_nom[i]
    ans = str(int(ans))
    print ("Количество нулей ", ans.count('0'))
    print ('Количество единиц ', ans.count('1'))

x = int(input())
Fibs_system(x)
