#Escrever um programa em Python para exibir os números de 1 até 50 na tela
x = 1
while x <= 50:
    print(x)
    x = x + 1
print('-------')

#Faça um programa em Python que imprima os 10 primeiros números
x = 1
while x <= 10:
    print(x)
    x = x + 1
print('-------')
#Faça um programa para escrever a contagem regressiva do lançamento de um foguete. O programa deve imprimir 10, 9, 8, …, 1, 0 e Fogo! na tela
x = 10
while x >= 0:
    print(x)
    x = x - 1
print("Fogo!")
print('-------')
#Faça um programa em Python para imprimir de 1 até o número digitado pelo usuário, mas,dessa vez, apenas os números ímpares
ultimo = int(input("Digite um numero:"))
x = 1
while x <= ultimo:
    print(x)
    x = x + 2
print('-------')
# Reescreva o programa anterior para escrever os 10 primeiros múltiplos de 3
fim = 30
x = 3
while x <= fim:
    print(x)
    x = x + 3
#Altere o programa anterior para exibir os resultados no mesmo formato de uma tabuada: 2x1 = 2, 2x2 = 4...
t = int(input("Tabuada de:"))
x = 1
while x <= 10:
    print(f"{t} x {x} = {t * x}")
    x = x + 1
#Crie um programa em Linguagem Python que solicite a senha de um usuário e depois, peça pra digitar novamente até que as duas senhas sejam correspondentes
senha1 = input("Digite a senha: ")
senha2 = input("Confirme a senha: ")
while senha1 != senha2:
    print("Senha errada, digite novamente.")
    senha1 = input("Digite a senha: ")
    senha2 = input("Confirme a senha: ")

print("senha confirmada, parabéns!")
#Faça um programa em Python que leia uma quantidade de números inteiros digitados pelo usuário, até que o usuário digite 0. Ao final, mostre a soma de todos os números digitados
total=0
numero=int(input("Digite um número: "))
while numero != 0:
    total+=numero
    numero=int(input("Digite um número: "))
print("Soma dos números= ",total)
#Faça um programa em Python que leia uma quantidade de números inteiros e positivos digitados pelo usuário, até que o usuário digite 0. Ao final, informe o maior número digitado o menor númerodigitado e a quantidade de números pares
#Não consegui fazer.
#Faça um programa em Python que permita que o usuário insira valores de produtos comprados por um cliente qualquer. O programa deve encerrar quando o usuário digitar “SAIR”. Se o usuário digitarum valor negativo não deve ser processado e um novo valor deve ser solicitado como entrada. Ao inal, informe o valor total a pagar, lembrando que, caso as vendas ultrapassem o total de R$3.000,00, deverá ser aplicado um desconto de 12%. Mostrar ao final valor total, o valor do descontoe o valor líquido
total=0
valor=float(input("Informe o valor do produto: R$"))
while valor!=0:
    if valor<0:
        print("Valor inválido.")
    else:
        total=total+valor;
    valor=float(input("Informe o valor do produto: R$"))
if total>3000:
    total-=total*0.1
print("Total a pagar: R$", total)
#Mudei a forma de sair, pois, não consigo trazer para string.
#Faça um programa em Python para calcular a soma e a média de x números inteiros inseridos pelo usuário. Digite -1 para terminar
#Nao  consegui fazer
