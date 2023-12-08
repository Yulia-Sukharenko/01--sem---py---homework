

def primediv(x):
    a = [i for i in range(2, x + 2)]
    mx = -99999999999

    for i in range(2,x+2):
        for j in range(len(a)):
            print(a)
            if (a[j] % i == 0) and (a[j] != i) and (a[j] in a):
                a[j] = 0

    for i in range(a.count(0)):
        a.remove(0)

    for i in a:
        if x % i ==0:
            if i > mx:
                mx = i

    if x in a:
        return "Простое число"
    else:
        return mx
    
x = int(input())
print(primediv(x))