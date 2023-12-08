def fuctorial(x): #факториал - умножение с единицы до самого числа
    result = 1
    for i in range(1, x + 1):
        result *= i
    return result

def zeros(x): # статистика показала, что в факториале каждого пятого числа +1 ноль
    return x // 5
x = int(input())
print(fuctorial(x), zeros(x))
