import math
import time

def intro():

    global divi, a1, multi
    soma = 0
    print('''  
    -----------------------------------------
    |                                       |
    |CALCULADORA POR TERMINAL [DOIS NÚMEROS]| 
    |                                       |
    -----------------------------------------
    ''')
    print('Opções de operação')
    print('[1] SOMA')
    print('[2] SUBTRAÇÃO')
    print('[3] DIVISÃO')
    print('[4] MULTIPLICAÇÃO')
    print('[5] RADICIAÇÃO DE QUADRADOS')
    print('[6] RADICIAÇÃO DE CUBOS')
    print('[7] EXPONENCIAÇÃO')
    print('[8] PORCENTAGEM')
    print('[9] FATORIAL')
    print('[10] SENO')
    print('[11] COSSENO')
    print('[12] TANGENTE')
    print('[0] SAIR')
    ope = input('Qual operação você deseja?  ')
    if ope == '1':
        print('------------------------')
        print('Você escolheu soma!')
        print('------------------------')
        for i in range(1, 3):
            a1 = int(input(f'Digite o n° {i}/2:  '))
            soma = soma + a1
        print(f'A soma dos números é: {soma}')
        time.sleep(1)
    if ope == '2':
        print('------------------------')
        print('Você escolheu subtração!')
        print('------------------------')
        for i in range(1, 3):
            a1 = int(input(f'Digite o n° {i}/2:  '))
            if i == 2:
                break
            sub =  a1
        print(f'{a1} subtraido de {sub} é : {sub - a1}')
        time.sleep(1)
    if ope == '3':
        print('------------------------')
        print('Você escolheu divisão!')
        print('------------------------')
        for i in range(1, 3):
            a1 = int(input(f'Digite o n° {i}/2:  '))
            if i == 2:
                break
            divi = a1
        print(f'A divisão entre {divi} e {a1} é: {divi / a1}')
        time.sleep(1)
    if ope == '4':
        print('------------------------')
        print('Você escolheu multiplicação!')
        print('------------------------')
        for i in range(1, 3):
            a1 = int(input(f'Digite o n° {i}/2:  '))
            if i == 2:
                break
            multi =  a1
        print(f'Multiplicação entre {multi} e {a1} é: {multi * a1}')
        time.sleep(1)
    if ope == '5':
        print('------------------------')
        print('Você escolheu radiciação de quadrados!')
        print('------------------------')
        a1 = int(input('Digite o radicando  '))
        sqr_root = math.sqrt(a1)
        print(f'A raiz quadrada de {a1} é: {sqr_root}')
        time.sleep(1)
    if ope == '6':
        print('------------------------')
        print('Você escolheu radiciação de cubos!')
        print('------------------------')
        a1 = int(input('Digite o radicando  '))
        c_root = math.pow(a1, 1/3)
        print(f'A raiz cúbica de {a1} é: {c_root}')
        time.sleep(1)
    if ope == '7':
        print('------------------------')
        print('Você escolheu exponenciação!')
        print('------------------------')
        base = int(input('Digite a base  '))
        expoente =  int(input('Digite o expoente  '))
        expo = base ** expoente
        print(f'O resultado é: {expo}')
        time.sleep(1)
    if ope == '8':
        print('------------------------')
        print('Você escolheu porcentagem!')
        print('------------------------')
        num1 = int(input('Digite a porcentagem '))
        num2 = int(input('Digite o valor '))
        porce = (num2 * (num1/100))
        print(f'{num1} % de {num2}: {porce}')
        time.sleep(1)
    if ope == '9':
        print('------------------------')
        print('Você escolheu fatorial!')
        print('------------------------')
        num_fat = int(input('Digite o valor:'))
        res_fat = math.factorial(num_fat)
        print(f'O resultado de {num_fat}! é: {res_fat} ')
        time.sleep(1)
    if ope == '10':
        print('------------------------')
        print('Você escolheu seno!')
        print('------------------------')
        num_sen = int(input('Digite o valor:'))
        res_sen = math.sin(num_sen)
        print(f'O seno de {num_sen}! é: {res_sen} ')
        time.sleep(1)
    if ope == '11':
        print('------------------------')
        print('Você escolheu cosseno!')
        print('------------------------')
        num_cos = int(input('Digite o valor:'))
        res_cos = math.cos(num_cos)
        print(f'O cosseno de {num_cos}! é: {res_cos} ')
        time.sleep(1)
    if ope == '12':
        print('------------------------')
        print('Você escolheu tangente!')
        print('------------------------')
        num_tan = int(input('Digite o valor:'))
        res_tan = math.tan(num_tan)
        print(f'A tangente de {num_tan}! é: {res_tan} ')
        time.sleep(1)
    if ope == '0':
        print('Obrigado! Até mais')
    else:
        print(msg_continue())
def msg_continue():
    conti = input('Continuar?[s/n]')
    if conti == 's':
        print(intro())
    elif conti == 'n':
        print('Obrigado!')
    else:
        print(msg_continue())
print(intro())
