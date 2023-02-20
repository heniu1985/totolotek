'''Modul with tests for functions modul
'''


from totolotek import functions


def test_welcome_message():
    '''Tests welcome_message function
    '''
    message = 'Witaj w programie TOTOLOTEK, który obliczy jak długo możesz czekać na wygraną w LOTTO.'
    assert functions.welcome_message() == message


def test_change_user_input_to_list():
    '''Tests change_user_input_to_list function
    '''
    assert functions.change_user_input_to_list('2, 5, 34, 49, 13, 19') == [2, 5, 34, 49, 13, 19]


def test_check_user_numbers():
    '''Tests chceck_user_number function
    '''
    assert functions.check_user_numbers([2, 5, 34, 49, 13, 19]) is True
    assert functions.check_user_numbers([2, 4, 5, 3]) is False
    assert functions.check_user_numbers([2, 5, 18, 34, 49, 13, 19]) is False
    assert functions.check_user_numbers([2, 5, 34, 49, 56, 19]) is False
    assert functions.check_user_numbers([]) is False


def test_draw_numbers():
    '''Tests draw_numbers function
    '''
    assert isinstance(functions.draw_numbers(), list)
    assert len(functions.draw_numbers()) == 6


def test_compare_numbers():
    '''Tests compare_numbers function
    '''
    assert functions.compare_numbers([1, 2, 3, 4, 5, 6], [6, 1, 2, 3, 5, 4]) is True
    assert functions.compare_numbers([1, 2, 3, 4, 5, 6], [4, 5, 23, 54, 12, 34]) is False


def test_how_many_draws_to_win():
    '''Tests how_many_draws function
    '''
    assert isinstance(functions.how_many_draws_to_win([1, 2, 3, 4, 5, 6], [6, 1, 2, 3, 5, 4]), int)
    assert isinstance(functions.how_many_draws_to_win([1, 2, 3, 4, 5, 6], [6, 1, 33, 5, 4]), int)


def test_how_long_it_will_take():
    '''Tests how_long_it_will_take function
    '''
    assert functions.how_long_it_will_take(10) == 23
    assert functions.how_long_it_will_take(3546) == 8274


def test_expenses_to_win():
    '''Tests expenses_to_win function
    '''
    assert functions.expenses_to_win(3333) == 9999
    assert functions.expenses_to_win(345, 2) == 690
    assert functions.expenses_to_win(5, 5) == 25
