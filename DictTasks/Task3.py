"""
Напишите программу принимающую ввод информации о треке(место в чарте,исполнитель, название) пока пользователь
не введет "off". Программа должна вывести всю информацию в виде словаря вида: {(место,испонитель): название трека}
"""
result = {}

while True:
    command = input('[+] Введите - место в чарте, исполнитель, название(через запятую) или off чтобы завершить \n')
    if command == 'off':
        print('[!] Результат \n', result)
        break
    else:
        info = command.split(',')
        if len(info) != 3:
            print('[-] Возникла ошибка. Попробуйте еще раз')
            continue
        else:
            result[(info[0], info[1])] = info[2]
            print('[!] Успешно!')
