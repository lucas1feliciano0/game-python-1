# -*- coding: utf-8 -*-
import random

class colors: 
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


user_name = input('{}Digite seu nome: {}'.format(colors.OKCYAN, colors.OKBLUE))

level = None
playing = True

while playing:

    while level == None:
        print('{}1 - Fácil'.format(colors.OKGREEN))
        print('2 - Intermediário')
        print('3 - Difícil')

        try:
            user_choose = int(input('{}Digite o número do nível:'.format(colors.HEADER)))
            if user_choose <= 3 and user_choose > 0:
                level = user_choose
            else:
                raise Exception(IOError)
        except Exception as e:
            print('{}Digite um número válido.'.format(colors.FAIL))
        else:
            print('{}Bem-vindo ao jogo, {}.'.format(colors.OKGREEN, user_name))

    random_range = level * 100
    rigth_answer = random.randint(1, random_range)
    user_answer = 0

    attempts = 50 // level
    hit = False

    while not hit and attempts > 0:
        print('{}Você tem {} tentativas.'.format(colors.OKCYAN, attempts))
        try:
            user_answer = int(input('Digite um número de 1 a {}: '.format(random_range)))
        except Exception as e:
            print('{}Digite um número válido.'.format(colors.FAIL))

            user_answer = int(
                input('Digite um número de 1 a {}: '.format(random_range)))

        hit = (rigth_answer == user_answer)

        if not hit:
            print('{}Opa... errou! Tenta de novo aí.'.format(colors.FAIL))
            attempts -= 1

            if user_answer < rigth_answer:
                print('{}Tente um número maior.'.format(colors.OKGREEN))
            else:
                print('{}Tente um número menor.'.format(colors.HEADER))
        else:
            print('{}Parabéns! Você acertou.'.format(colors.OKGREEN))

    user_want_play = False

    while True:
        try:
            print('{}1 - Sim'.format(colors.OKBLUE))
            print('{}2 - Não. Que jogo terrível!'.format(colors.FAIL))

            user_want_play = int(input('{}Deseja jogar novamente? '.format(colors.OKBLUE)))

            if user_want_play > 2 or user_want_play < 1:
                raise Exception(IOError)

        except Exception as e:
            print('{}Digite um número válido.'.format(colors.FAIL))

            continue
        break
        
    if user_want_play == 1:
        playing = True
        print('Ok, jogue novamente!')
    else:
        playing = False
        print('Poxa... mas tudo bem!')
