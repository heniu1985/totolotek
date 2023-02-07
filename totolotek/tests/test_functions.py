'''Modul with tests for functions modul
'''


from totolotek import functions


def test_welcome_message():
    '''Tests welcome_message function
    '''
    message = 'Witaj w programie TOTOLOTEK, który obliczy jak długo możesz czekać na wygraną w LOTTO.'
    assert functions.welcome_message() == message


def test_type_of_numbers():
    pass


def test_take_user_numbers():
    pass


def test_draw_numbers():
    pass


def test_compare_numbers():
    pass
