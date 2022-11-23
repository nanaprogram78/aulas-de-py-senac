#1
for num in range(1, 51):
    print(num)

#2
numero = int(input('Informe o numero para ver a tabuada: '))
for i in range(1, 11):
    print(numero, 'X', i, '=', (numero * i))

#3
print('--- dois em dois ----')
for numero in range(1, 101):
    if numero % 2 == 0:
        print(numero)


#4
print('--- num sete --- ')
for num in range(5, 101):
    if (num % 7 == 0 and num % 5 != 0):
        print(num)

#5
print('---soma---')
soma_numeros = 0
numero = int(input("Por favor, insira um número: "))
for i in range(1, numero + 1, 1):
    soma_numeros += i
print("A soma é = ", soma_numeros)

#6
print('--- tras para frente ---')
palavra= input("Entre com uma string para inverter: ")
for char in range(len(palavra) - 1, -1, -1):
  print(palavra[char], end="")
print("\n")

#7
print('--- numeros pares e impares ---')
numeros = (1, 2, 14, 4, 5, 6, 7, 8, 10) 
contador_par = 0
contador_impar = 0
for x in numeros:
        if not x % 2:
            contador_par=contador_par+1
        else:
            contador_impar=contador_impar+1
print("Quantidade de números pares:",contador_par)
print("Quantidade de números impares:",contador_impar)

#8
print('--- string ---')
texto = input("Digite algo: ")
digitos=0
letras=0
for x in texto:
    if x.isdigit():
        digitos=digitos+1
    elif x.isalpha():
        letras=letras+1
    else:
        pass
print("Total de letras: ", letras)
print("Total de Digitos:", digitos)

#9
print('--- lista de numeros ---')
lista= []
for i in range(100, 401):
    s = str(i)
    if (int(s[0]) % 2 == 0) and (int(s[1]) % 2 == 0) and (int(s[2]) % 2 == 0):
        lista.append(s)
print(",".join(lista))

#10
print("--- Fatorial de um número ---")
factorial = 1
num = int(input("Digite um número para calcular: "))
if num < 0:
    print("Não existe fatorial para número negativo")
elif num == 0:
    print("O fatorial de 0 é 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print("O fatorial de", num, "é", factorial)

#11
print('--- verificaçao de numeros ---')
print("Digite os numeros para verificar")
n_faz=0
faz_parte=0
for num in range(0,10):
    num = int(input("Digite um número : "))
    if(num>=10 and num<=20):
        faz_parte= faz_parte + 1
    else:
        n_faz= n_faz + 1

print("São: ",faz_parte,"números que estão dentro do intervalo[10,20]")
print("São: ",n_faz,"números que estão fora do intervalo[10,20]")