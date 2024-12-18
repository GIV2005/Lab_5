import random


def get_random_stones():
    return random.randint(4, 30)


def user_turn(stones_left):
    while True:
        user_choice = input("Сколько камней вы возьмёте? (1, 2 или 3): ")
        if not user_choice.isdigit():
            print("Ошибка: Введите число от 1 до 3.")
            continue

        user_choice = int(user_choice)
        if user_choice not in [1, 2, 3]:
            print("Ошибка: Можно взять только 1, 2 или 3 камня.")
        elif user_choice > stones_left:
            print("Ошибка: Нельзя взять больше камней, чем осталось.")
        else:
            return user_choice


def computer_turn(stones_left):
    for i in [1, 2, 3]:
        if (stones_left - i) % 4 == 0:
            return i
    return random.choice([1, 2, 3])


print("Добро пожаловать в игру 'Камни'!")
stones_left = get_random_stones()
print(f"В кучке {stones_left} камней.")

while stones_left > 0:
    user_choice = user_turn(stones_left)
    stones_left -= user_choice
    print(f"Вы взяли {user_choice} камня(ей). Осталось {stones_left} камней.")
    if stones_left == 0:
        print("Поздравляем! Вы победили!")
        break


    computer_choice = computer_turn(stones_left)
    stones_left -= computer_choice
    print(f"Компьютер взял {computer_choice} камня(ей). Осталось {stones_left} камней.")
    if stones_left == 0:
        print("Компьютер победил. Попробуйте снова!")
        break
