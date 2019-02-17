import string
import zipfile
import random


def check_sum():
    with open('rows.txt') as file:
        lines = file.readlines()
        sum_num = 0
        for line in lines:
            row = line.split('\t')
            row = [int(i) for i in row]
            diff = max(row) - min(row)
            sum_num = sum_num + diff
        print(sum_num)
        return sum_num


check_sum()


def read_zip_file():
    files = zipfile.ZipFile('zadanie_1_words.zip')

    for txt in files.infolist():
        single_file = files.open(txt)
        line_list = str(single_file.readlines())

        line_list = line_list.lower()
        print(line_list)
        signs = string.ascii_lowercase
        for sign in signs:
            amount_of_sign = line_list.count(sign)
            print(sign, amount_of_sign)


read_zip_file()


def rock_paper_scissors():
    choice = ('r', 'p', 's')
    user_choice = 0
    comp_won = 0
    user_won = 0

    while user_choice != 'no':
        user_choice = (input('Choose a play sign: (R)ock,(P)aper, (S)cissors or (No) if you want to close the game: '))
        user_choice = user_choice.lower()
        if user_choice == 'no':
            break

        comp_choice = random.choice(choice)
        print(user_choice)
        print(comp_choice)
        if user_choice == 'r' and comp_choice == 's' or user_choice == 's' and comp_choice == 'p' or user_choice == 'p' and comp_choice == 'r':
            print('+' + '-' * 10 + '+')
            print('| ' + 'You won!' + ' |')
            print('+' + '-' * 10 + '+')
            user_won += 1
            print('Current result: You {}:{} Computer'.format(user_won, comp_won))

        elif user_choice == 'r' and comp_choice == 'r' or user_choice == 's' and comp_choice == 's' or user_choice == 'p' and comp_choice == 'p':
            print('+' + '-' * 7 + '+')
            print('| ' + 'Draw!' + ' |')
            print('+' + '-' * 7 + '+')

        elif user_choice == 's' and comp_choice == 'r' or user_choice == 'p' and comp_choice == 's' or user_choice == 'r' and comp_choice == 'p':
            print('+' + '-' * 15 + '+')
            print('| ' + 'Computer won!' + ' |')
            print('+' + '-' * 15 + '+')
            comp_won += 1
            print('Current result: You {}:{} Computer'.format(user_won, comp_won))

        else:
            print('You have chose a wrong sign. Try again.')

        play_again = input('Do you want to play again? Write "yes" or "no".')
        play_again = play_again.lower()
        if play_again == 'yes' or play_again == 'y':
            print('=' * 80)
        elif play_again == 'no' or play_again == 'n':
            break


rock_paper_scissors()





