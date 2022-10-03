play=input()
while play !='off':
    if play=='game':
        print('Добро пожаловать в игру "Угадай число!" (xтобы заврешить работу введите "off"')
        for i in range(3):
            num1=input('Введите число: ')
            if num1=="5":
                print('Вы виграли билет на концерт!')
            elif num1=="off":
                break
    play = input("Хотите сыграть еще? ")