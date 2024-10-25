from User import User
import os

from Utils import SIGNIN, LOGIN


def limpa_tela():
    os.system('cls')

def titulo(tipo_titulo=LOGIN):

    if tipo_titulo == LOGIN:
        tituloatual = 'LOGIN'
    else:
        tituloatual = 'SIGN IN'

    print('-' + ('---' * 6))
    print('|' + ('   ' * 2) + tituloatual + ('   ' * 2) + '|')
    print('-' + ('---' * 6))

def escolhe_chosen_option():
    print('Choose an option')
    print('-' + ('---' * 6))
    print('[1] LOGIN')
    print('[2] SIGN IN')
    print('[0] CLOSE')
    print('-' + ('---' * 6))
    return input(': ')

def try_again():
    print('Choose an option: ')
    print('-' + ('---' * 6))
    print('[1] Try again')
    print('[2] Change password')
    print('[3] Sign In ')
    print('-' + ('---' * 6))
    return input(': ')

def new_password():
    print('Change your password')
    print('-' + ('---' * 6))

def closed(option):
    return option == '0'

already_executed = False
execute_again = False
chosen_option = ''
sign_in = False
closed_program = False
login_found = False

while True:
    sign_in = False
    login_found = False

    if (not already_executed) or execute_again:
        chosen_option = escolhe_chosen_option()

        closed_program = closed(chosen_option)
        if closed_program:
            break

        already_executed = True

    while not (chosen_option in ['1', '2']):
        limpa_tela()
        chosen_option = escolhe_chosen_option()

    closed_program = closed(chosen_option)
    if closed_program:
        break

    if chosen_option == '1':
        titulo()
        user = User()
        user.username = input('Username: ')
        user.password = input('Password: ')

        login_found = user.login_verification()

        if not login_found:
            print('No login found, certify that your username and password are corret.')
            answer = try_again()

            if answer == '1':
                continue
            elif answer == '2':
                limpa_tela()
                new_password()
                user.password = input('Type your new password: ')
                user.add_data()
            else:
                sign_in = True
        else:
            print(f'Welcome {user.username}!')


    if (chosen_option == '2') or sign_in:
        limpa_tela()
        titulo(SIGNIN)
        user = User()
        user.username = input('Username: ')
        user.password = input('Password: ')

        user.add_data()

    execute_again = False if (not closed_program) and (input('\n' + 'Type "0" to finish or any other to restart: ') == '0') else True
    if not execute_again:
        break
