#4. Пользователь вводит целое положительное число.
#Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
n = int(input("Введите целое положительное число: "))
max_digit = n % 10
while n != 0:
    last_digit = n % 10
    if last_digit > max_digit:
        max_digit = last_digit
    n //= 10
print(max_digit)


