'''Modul with tests for functions modul
'''


from totolotek import functions


def test_welcome_message():
    '''Tests welcome_message function
    '''
    message = 'Witaj w programie TOTOLOTEK, który obliczy jak długo możesz czekać na wygraną w LOTTO.'
    assert functions.welcome_message() == message


def test_change_user_input_to_list():
    '''Tests change_user_input_to_list function'''
    assert functions.change_user_input_to_list(2, 5, 34, 49, 13, 19) == [2, 5, 34, 49, 13, 19]
    assert functions.change_user_input_to_list() == []
    assert functions.change_user_input_to_list(2, '1') == [2, '1']


def test_check_user_numbers():
    '''Tests chceck_user_number function'''
    assert functions.check_user_numbers([2, 5, 34, 49, 13, 19]) is True
    assert functions.check_user_numbers([2, 4, 5, 3]) is False
    assert functions.check_user_numbers([2, 5, 18, 34, 49, 13, 19]) is False
    assert functions.check_user_numbers([2, 5, 34, 49, 56, 19]) is False
    assert functions.check_user_numbers([]) is False


def test_draw_numbers():
    assert isinstance(functions.draw_numbers(), list)
    assert len(functions.draw_numbers()) == 6


def test_compare_numbers():
    pass
