# 1 Questão:

soma_notas = 0


notas = [float(input(f"Digite a {i+1}ª nota: ")) for i in range(5)]

media = sum(notas) / 5

if media >= 7:
    print(f"Média: {media:.2f} - Aprovado!")
else:
    print(f"Média: {media:.2f} - Reprovado.")

# 2 Questão:

def calcular_fatorial(x):
    if x < 0:
        return "Apenas numeros positivos!"
    elif x == 0:
        return 1
    else:
        fatorial = 1
        for i in range(1, x + 1):
            fatorial *= i
        return fatorial


numero = int(input("Digite um número inteiro positivo: "))


resultado = calcular_fatorial(numero)
print(f"O fatorial de {numero} é {resultado}")

# 3 Questão:
import re

def palidromo(frase):
    # Remove espaços e pontuações
    frase = re.sub(r'[^\w\s]', '', frase)
    # Converte a frase para letras minúsculas
    frase = frase.lower()
    # Verifica se a frase é igual quando lida de trás para frente
    return frase == frase[::-1]

frase1 = "dvd"
frase2 = "lalal"
frase3 = "python"

print(palidromo(frase1)) 
print(palidromo(frase2))
print(palidromo(frase3))

# 4 Questão:

numero = int(input("Digite um número inteiro positivo: "))


if numero < 0:
    print("Por favor, digite um número inteiro positivo.")
else:
    
    soma_digitos = 0

    
    numero_str = str(numero)


    for digito in numero_str:
        soma_digitos += int(digito)

    print("A soma dos dígitos de", numero, "é", soma_digitos)

# 5 Questão:

def primo(numero):
    # Verifique se o número é menor que 2 (números negativos e 0 não são primos)
    if numero <= 1:
        return False
    # Verifique se o número é divisível por qualquer número de 2 até a raiz quadrada do número
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    # Se não houver nenhum divisor entre 2 e a raiz quadrada do número, o número é primo
    return True

# Exemplo de uso:
numero = int(input("Digite um número: "))
if primo(numero):
    print(numero, "é um número primo.")
else:
    print(numero, "não é um número primo.")

# 6 Questão:

def contar_vogais(string):
    # Inicializa um contador de vogais
    contador = 0

    # Converte a string para letras minúsculas para garantir a contagem correta
    string = string.lower()

    # Percorre a string e verifica cada caractere
    for caractere in string:
        if caractere in 'aeiou':
            contador += 1

    return contador

# Solicita ao usuário que digite uma string
entrada = input("Digite uma string: ")

# Chama a função contar_vogais para contar as vogais na string
quantidade_vogais = contar_vogais(entrada)

# Exibe o resultado
print("A quantidade de vogais na string é:", quantidade_vogais)

# 7 Questão:

def calcular_imc(peso, altura):
    # Verifica se a altura está em metros
    if altura < 1:
        raise ValueError("A altura deve ser fornecida em metros.")

    # Calcula o IMC
    imc = peso / (altura ** 2)
    
    return imc

# Solicita ao usuário que insira seu peso (em kg) e altura (em metros)
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

# Chama a função calcular_imc para calcular o IMC
imc = calcular_imc(peso, altura)

# Exibe o resultado
print("Seu IMC é:", imc)

# 8 Questão:

def celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_para_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

print("Escolha uma opção:")
print("1. Celsius para Fahrenheit")
print("2. Fahrenheit para Celsius")

opcao = int(input("Digite o número da opção desejada: "))

if opcao == 1:
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = celsius_para_fahrenheit(celsius)
    print(f"{celsius} graus Celsius é igual a {fahrenheit:.2f} graus Fahrenheit.")
elif opcao == 2:
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    celsius = fahrenheit_para_celsius(fahrenheit)
    print(f"{fahrenheit} graus Fahrenheit é igual a {celsius:.2f} graus Celsius.")
else:
    print("Opção inválida. Por favor, escolha 1 ou 2.")

# 9 Questão:

# Função para realizar a adição
def adicao(a, b):
    return a + b

# Função para realizar a subtração
def subtracao(a, b):
    return a - b

# Função para realizar a multiplicação
def multiplicacao(a, b):
    return a * b

# Função para realizar a divisão
def divisao(a, b):
    if b == 0:
        return "Erro! Divisão por zero."
    else:
        return a / b

print("Escolha uma operação:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

# Solicita ao usuário que insira a opção desejada
opcao = input("Digite o número da operação desejada: ")

# Solicita ao usuário que insira os números para a operação
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Realiza a operação com base na escolha do usuário
if opcao == '1':
    resultado = adicao(numero1, numero2)
    operacao = "adição"
elif opcao == '2':
    resultado = subtracao(numero1, numero2)
    operacao = "subtração"
elif opcao == '3':
    resultado = multiplicacao(numero1, numero2)
    operacao = "multiplicação"
elif opcao == '4':
    resultado = divisao(numero1, numero2)
    operacao = "divisão"
else:
    resultado = "Opção inválida"
    operacao = ""

# Exibe o resultado da operação
if operacao:
    print(f"O resultado da {operacao} é: {resultado}")
else:
    print(resultado)

# 10 Questão:

def gerar_fibonacci(numero_de_termos):
    # Inicialize a lista para armazenar os termos da sequência
    fibonacci = []
    
    # Inicialize os primeiros dois termos
    a, b = 0, 1

    # Adicione os primeiros dois termos à lista
    fibonacci.append(a)
    fibonacci.append(b)

    # Gere os termos subsequentes até o número desejado de termos
    for _ in range(2, numero_de_termos):
        # Calcule o próximo termo
        c = a + b
        fibonacci.append(c)

        # Atualize os valores de a e b para os próximos cálculos
        a, b = b, c

    return fibonacci

# Solicita ao usuário o número de termos desejado
numero_de_termos = int(input("Digite o número de termos da sequência de Fibonacci desejado: "))

# Chama a função gerar_fibonacci para gerar a sequência
sequencia = gerar_fibonacci(numero_de_termos)

# Exibe a sequência gerada
print("Sequência de Fibonacci:")
for termo in sequencia:
    print(termo, end=" ")

