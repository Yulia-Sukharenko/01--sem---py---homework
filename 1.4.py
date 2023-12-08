def intersect (a, b):
    res = ''
    for i in range(32):
        if a % 10  == b % 10 == 1: #пересечение множеств - в обоих числах на одном и том же месте должны стоять единицы
            res += '1'
        a //= 10
        b //= 10
    return res

    
    

a = int(input())
b = int(input())
print(intersect(a,b))