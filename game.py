"""Guess the number"""

import numpy as np

number = np.random.randint(1, 101) # загадываем число от 1 до 100.

count = 0 # количество попыток 

while True:
    count+=1
    predict_number = int(input("Guess number: "))
    
    if predict_number > number:
        print("Число должно быть меньше!")
        
    elif predict_number < number:
        print("Число должно быть больше!")
        
    else:
        print(f"Угадал, молодец! Это число = {number}, за {count} попыток")
        break # выход из цикла после победы.
    