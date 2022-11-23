import sys
import time 


numero_ip = int(input('Digite um número inteiro e positivo: '))

if numero_ip <= 0 :
    print('É obrigatório que se digite um número positivo ou maior que zero.')

if numero_ip % 2 == 0 :
    print(f'O número {numero_ip} é PAR')
    nome_personalidade = input('Digite o nome de uma prsonalidade famosa: ')
    print(f'O nome da personalidade {nome_personalidade.upper()} em maiscúlo.')
    print(f'O nome da personalidade {nome_personalidade.lower()} em maiscúlo.')
else:
    n1 = int(input('Digite um valor: '))
    n2 = int(input('Digite um valor: '))
    n3 = int(input('Digite um valor: '))
    if ((n1 != n2) and (n1 != n3) and n2 != n3):
        soma = n1 + n2 + n3
        media = soma / 3

        if ((n1 > n2) and (n1 > n3)):
            maior = n1  
        elif ((n2 > n1) and (n2 > n3)):
            maior = n2
        else:
            maior = n3

        print(f'O maior número é: {maior}. O somatório é: {soma}. A média é: {media}.')