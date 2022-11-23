while True:
    num = int(input('Digite um numero numero: '))
    if num > 0:
        print('O valor digitado é positivo')
    if num %2 :
        print("Ímpar")
        n1 = (input("Digite tres valores diferentes:"))
        n2 = (input("Digite tres valores diferentes:"))
        n3 = (input("Digite tres valores diferentes:"))
        if(n1==n2==n3):
          print("Os números digitados são iguais")
        else:
          print("Os números digitados são diferentes")
        if n1 > n2:
          print(n1)
        elif n2 > n1:
         print(n2)
       
        
    else:
       print("Par")
       pers = (input("Digite o nome de uma personalidade sua:"))
       print(f'Personalidade: {pers}')
    
