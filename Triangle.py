# У треугольника сумма любых двух сторон должна быть больше третьей

numbers = list(map(int, input('Введите три числа через пробел: ').split()))
numbers.sort()
if numbers[2] >= numbers[0] + numbers[1]:
    print('Треугольник построить невозможно')
else:
    if numbers[0] == numbers[1] == numbers[2]:
        print('Равносторонний треугольник')
    if numbers[0] == numbers[1] != numbers[2]:
        print('Равнобедренный треугольник')
    if numbers[0] != numbers[1]:
        print('Разносторонний треугольник')
