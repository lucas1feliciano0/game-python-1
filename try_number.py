# -*- coding: utf-8 -*-
import random

user_name = raw_input('Digite seu nome: ')

level = None

while level == None:
    print('1 - Fácil')
    print('2 - Intermediário')
    print('3 - Difícil')

    try:
        user_choose = int(raw_input('Digite o número do nível:'))
        level = user_choose
    except Exception as e:
        print('Digite um número válido.')
    else:
        print('Bem-vindo ao jogo, {}.'.format(user_name))
    
random_range = level * 100
rigth_answer = random.randint(1, random_range)
user_answer = 0

hit = False

while not hit:
    try:
        user_answer = int(raw_input('Digite um número de 1 a {}: '.format(random_range)))
    except Exception as e:
        print('Digite um NÚMERO válido. Burro...')
        user_answer = int(raw_input('Digite um número de 1 a {}: '.format(random_range)))
    
    hit = (rigth_answer == user_answer)
    
    if not hit:
        print('Opa... errou! Tenta de novo aí.')

        if user_answer < rigth_answer:
            print('Tente um número maior.')
        else:
            print('Tente um número menor.')
    

print('Parabéns! Você acertou.')
