print("-" * 20)
print("Введите число от 100 до 999")
num = int(input(": "))
suma = 0
mul = 1
while num > 0:
    a = num % 10
    suma = suma + a
    mul = mul * a
    num = num // 10
print("Сумма: ", suma)
print("Произведение: ", mul)
print("-" * 20)
