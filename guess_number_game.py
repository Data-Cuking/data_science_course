"""Computer plays itself 'guess a number'
"""
import numpy as np


def random_predict(number: int = 1) -> int:
    """Guesses a number in not more than 8 times
    Args:
        number (int, optional): Hidden number. Defaults to 1.

    Returns:
        int: Attempt count 
    """
    count = 0
    min = 1  # lower border
    max = 100  # upper border

    # Initial predict number
    predict_number = np.random.randint(min, max + 1)

    while True:
        print('Predict number: ', predict_number)
        count += 1

        if number > predict_number:
            min = predict_number
            predict_number = min + (max - min)//2
        elif number < predict_number:
            max = predict_number
            predict_number = max - (max - min)//2
        else:
            break  # exit when guessed

    return count


number = np.random.randint(1, 101)

if __name__ == '__main__':
    random_predict(number)