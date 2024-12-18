import math


def get_numbers():
    while True:
        try:
            a = int(input("Введите первое натуральное число: "))
            b = int(input("Введите второе натуральное число: "))
            if a <= 0 or b <= 0:
                print("Числа должны быть натуральными.")
            else:
                return a, b
        except ValueError:
            print("Ошибка: Введите корректное число.")


def nod(a, b):
    while b != 0:
        a, b = b, a % b
    return a


num1, num2 = get_numbers()
custom_nod = nod(num1, num2)
print(f"НОД (вычисленный вручную): {custom_nod}")
print(f"НОД (с использованием math.gcd): {math.gcd(num1, num2)}")
