text = input('Чего желаете?')

if text == "Завтрак":
    print("Каша")
    exit(0)

if text == "Обед" or text == "Ужин":
    if input("Вы хотите плотно поесть?(да/нет): ") == "да":
        print("плов")
        exit(0)

print("Котлета с пюре")