'''Modul with all functions of the programm
'''
from random import randint
from math import floor


def welcome_message():
    '''Function returns welcome message

    Returns:
        str: Text of welcome message
    '''
    return 'Witaj w programie TOTOLOTEK, który obliczy jak długo możesz czekać na wygraną w LOTTO.'


def change_user_input_to_list(user_numbers: str) -> list:
    '''Function change user numbers to list

    Returns:
        list: List of user inputs
    '''
    user_numbers = user_numbers.split(',')
    user_numbers = [int(number) for number in user_numbers]

    return user_numbers


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


def how_many_draws_to_win(user_numbers: list, drawn_numbers: list) -> int:
    '''Function counts how many draws we need to win

    Args:
        user_numbers (list): List with user numbers
        drawn_numbers (list): List with drawn numbers

    Returns:
        int: Number of draws
    '''
    draw_id = 1
    while True:
        if compare_numbers(user_numbers, drawn_numbers):
            return draw_id
        else:
            drawn_numbers = draw_numbers()
            draw_id += 1


def how_many_days_it_will_take(number_of_draws: int, number_of_draws_in_week=3) -> int:
    '''Function calculate how many days you need to win in lottery

    Args:
        number_of_draws (int): Number of draws needed to win

    Returns:
        int: Number of days needed to win
    '''
    return floor((number_of_draws / number_of_draws_in_week) * 7)


def how_long_it_will_take(number_of_days: int) -> str:
    years = floor(number_of_days / 365)
    months = floor(number_of_days % 365) / 30
    days = floor(number_of_days % 365) % 30
    return f'Wygrana zajmie nam {int(years)} rok, {int(months)} miesięcy i {int(days)} dni.'


def expenses_to_win(number_of_draws: int, ticket_price: float = 3) -> float:
    '''Function calculate how much money will we spend to win in lottery

    Args:
        number_of_draws (int): Number of draws needed to win in lottery
        ticket_price (float, optional): One ticket we must spend to participate in lottery. Defaults to 3.

    Returns:
        float: Ammout of money needed to win in lottery
    '''
    return number_of_draws * ticket_price
