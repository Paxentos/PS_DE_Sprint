x1, x2 = input('Введите первое двоичное число\n'), input(
    'Введите второе двоичное число\n')
 
Multiply = int(x1, 2) * int(x2, 2)
binaryMul = bin(Multiply)[2:]
print(binaryMul)