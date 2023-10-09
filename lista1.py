# 1 Questão:

print("Informe suas nota aqui." )
nota1 = int(input ("Digite sua nota sem virgula:" ))
print("Primeira nota: " + str(nota1))

print("Informe suas nota aqui:")
nota2 = int(input ("Digite sua nota sem virgula:" ))
print("Primeira nota: " + str(nota2))

print("Informe suas nota aqui:")
nota3 = int(input ("Digite sua nota sem virgula:" ))
print("Primeira nota: " + str(nota3))

notas = nota1 + nota2 + nota3
media = notas / 3
print("Sua média é essa: " + str(media))

# 2 Questão:

numero = int(input("Mirella digite qualquer número:" ))
if numero % 2 == 0:
    print("Esse número é par")
else:
    print("Esse número é impar")

# 3 Questão:

numero = int(input("Mirella digite qualquer número:" ))
if numero < 0:
    print("Por favor, insira um número possitivo.")
else:
    print("Números pares de 0 ate seu {numero}: ")
    for i in range(0, numero + 1, 2):
        print(i)

# 4 Questão:

numeros = input("Digite uma lista de números separados por espaço: ")

numeros_lista = [int(num) for num in numeros.split()]

maior_valor = numeros_lista[0]
menor_valor = numeros_lista[0]

for num in numeros_lista:
    if num > maior_valor:
        maior_valor = num
    if num < menor_valor:
        menor_valor = num

print(f"O maior valor da lista é: {maior_valor}")
print(f"O menor valor da lista é: {menor_valor}")

# 5 Questão:

numeros_lista = [1, 2 , 5, 10, 12]

soma_pares = 0
quantidade_pares = 0

for num in numeros_lista:
    if num % 2 == 0:
        soma_pares += num
        quantidade_pares += 1

if quantidade_pares > 0:
    media_pares = soma_pares / quantidade_pares
    print(f"A média dos números pares é: {media_pares:.2f}")
else:
    print("Não foram digitados números pares.")

# 6 Questão:

numeroInteiro = int(input("Digite um número inteiro:"))

if numeroInteiro < 0:
    print("O fatorial não está definido para números negativos.")
elif numeroInteiro == 0:
    print("O fatorial de 0 é 1.")
else:
    fatorial = 1
    for i in range(1, numeroInteiro + 1):
        fatorial *= i
    print(f"O fatorial de {numeroInteiro} é {fatorial}.")

# 7 Questão:

valor = int(input("Informe um valor:"))

a, b = 0, 1


print(a, b, end=" ")


while b < valor:
    c = a + b
    print(c, end=" ")
    a, b = b, c

# 8 Questão: 

num = int(input('Digite o valor: '))

primo = True
for i in range(2, num):
    if num % i == 0:
        primo = False
        break
if primo:
    print(num, "é primo")

else:
    print(num, "não é primo")

# 9 Questão:

nomes = input("Digite uma lista de nomes separados por vírgula: ").split(",")


nova_lista = []

for nome in nomes:
    nome = nome.strip()
    if nome.startswith('A') or nome.startswith('a'):
        nova_lista = [].append(nome)

print("Nomes que começam com 'A':")
for nome in nova_lista:
    print(nome)

# 10 Questão:

import random

opcoes = ["Pedra", "Papel", "Tesoura"]

print("Escolha uma opção:")
print("1. Pedra")
print("2. Papel")
print("3. Tesoura")
escolha_usuario = int(input("Digite o número da sua escolha (1/2/3): "))

if escolha_usuario < 1 or escolha_usuario > 3:
    print("Escolha inválida. Por favor, escolha 1, 2 ou 3.")
else:
    escolha_usuario -= 1

    escolha_computador = random.randint(0, 2)

    print(f"Você escolheu {opcoes[escolha_usuario]}.")
    print(f"O computador escolheu {opcoes[escolha_computador]}.")

    if escolha_usuario == escolha_computador:
        print("Empate!")
    elif (escolha_usuario == 0 and escolha_computador == 2) or \
         (escolha_usuario == 1 and escolha_computador == 0) or \
         (escolha_usuario == 2 and escolha_computador == 1):
        print("Você venceu!")
    else:
        print("O computador venceu!")
        