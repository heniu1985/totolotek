'''Modul with all functions of the programm
'''
from random import randint


def welcome_message():
    '''Function returns welcome message

    Returns:
        str: Text of welcome message
    '''
    return 'Witaj w programie TOTOLOTEK, który obliczy jak długo możesz czekać na wygraną w LOTTO.'


def change_user_input_to_list(*args: int) -> list:
    '''Function change user numbers to list

    Returns:
        list: List of user inputs
    '''
    return list(args)


def check_user_numbers(user_numbers: list) -> bool:
    '''Function checks that user inputs are integers and that he inputs only six numbers

    Args:
        user_numbers (list): List of user inputs

    Returns:
        bool: Return True when user input consits of six integers
    '''
    if len(user_numbers) != 6:
        return False

    for number in user_numbers:
        if not isinstance(number, int):
            return False

        if number not in range(1, 50):
            return False

    return True


def draw_numbers() -> list:
    '''Function draw six numbers between 1 and 49

    Returns:
        list: List of numbers
    '''
    output = []
    for _ in range(6):
        number = randint(1, 49)
        output.append(number)

    return output


def compare_numbers(user_numbers: list, drawn_numbers: list) -> bool:
    '''Function compare drawn numbers with unmbers given by user

    Args:
        user_numbers (list): List of numbers given by user
        drawn_numbers (list): List of drawn numbers

    Returns:
        bool: _description_
    '''
    if set(user_numbers) == set(drawn_numbers):
        return True

    return False
