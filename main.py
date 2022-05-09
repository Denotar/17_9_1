def binary_search(array, element, left, right):
    if left > right:
        return left
    middle = (right + left) // 2
    if array[middle] == element:
        return middle

    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)

try:
    massiv = [int(n) for n in input('Введите числа через пробел:\n').split()]
    massiv.sort()
    nomer = int(input('А теперь введи число любое число:\n'))
    print(binary_search(massiv, nomer, 0, len(massiv) - 1) - 1)
    print(binary_search(massiv, nomer, 0, len(massiv) - 1))
    print(massiv)


except:
    print('Ты ввел какую-то левую шляпу')
