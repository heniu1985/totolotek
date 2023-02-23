'''Main modul of programm
'''
from totolotek import functions


def main():
    '''Main function of programm in which rest of function will be called
    '''
    functions.welcome_message()

    user_numbers = input('Podaj 6 liczb [1-49] oddzielone przecinkami: ')
    user_numbers = functions.change_user_input_to_list(user_numbers)

    if functions.check_user_numbers(user_numbers):
        drawn_numbers = functions.draw_numbers()
        number_of_draws = functions.how_many_draws_to_win(user_numbers, drawn_numbers)
        time_to_win = functions.how_long_it_will_take(number_of_draws)
        expenses = functions.expenses_to_win(number_of_draws)
        print(time_to_win)
        print(f'Na wszystkie losy wydasz {expenses} zł.')
        print(number_of_draws)
    else:
        print('Podano złe liczby')


if __name__ == '__main__':
    main()
