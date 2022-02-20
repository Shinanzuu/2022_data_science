import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загадочное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    
    while True:
        count+=1
        predict_number = np.random.randint(1, 101) # предполагаемое число
        if number == predict_number:
            break # выход из цикла если угадали
    return(count) # выпод количества попыток за которое нашел число

def score_game(random_predict) -> int:
    """За какое вол-во функция угадывает в среднем число

    Args:
        random_predict (_type_): Функция угадывания

    Returns:
        int: Среднее кол-во попыток
    """
    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls)) # находим среднее количество попыток
    
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток.')
    return(score)

if __name__ == '__main__':
    # RUN
    score_game(random_predict)