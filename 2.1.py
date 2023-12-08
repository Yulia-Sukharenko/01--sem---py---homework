def maxk(arr,k):
    n = len(arr) 
    ans = maxsum = 0
    
    for i in range(k, n + 1):
        ans = sum(arr[i - k : i]) 
        
        if ans > maxsum:
            maxsum = ans     
    return maxsum

n = int(input("Введите количество элементов массива: "))
k = int(input("Введите период: "))
arr = []

if k > n:
    print("Ошибка")
else:
    print('Введите элементы массива: ')
    for i in range(n):
        arr.append(int(input()))
    print('Ответ: ', maxk(arr, k))