def enter_num(tip):

    """
    проверка ввода чисел от пользователя

    """

    input_num = None
    while input_num is None:
        input_num = input(tip)
        try:
            input_num = float(input_num)
        except ValueError:
            print(f'Ошибка ввода! Вы ввели не число - {input_num}')
            input_num = None
    return input_num
