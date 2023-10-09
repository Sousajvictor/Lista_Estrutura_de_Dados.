# 1 Questão:

class Circulo:
    def __init__(self,raio):
        self.raio = raio
    
    def calcular_area(self):
        pi = 3.14
        area = pi * (self.raio ** 2)
        return area
    

raio = 10
circulo = Circulo(raio)
area_do_circulo = circulo.calcular_area()

print(f"A área do círculo com raio {raio} é {area_do_circulo}")

# 2 Questão:

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def detalhes(self):
        return f"Titulo: {self.titulo}, autor: {self.autor}"

livro1 = Livro("Quem Pensa Enriquece", "Napoleon Hill")
detalhes_livro1 = livro1.detalhes()
print (detalhes_livro1)

livro2 = Livro ("Pai Rico, Pai Pobre", "Robert T. Kiyosaki")
detalhes_livro2 = livro2.detalhes()
print(detalhes_livro2)

# 3 Questão:

class Retangulo:
    def __init__(self,base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        area = self.base * self.altura
        return area
    
base = 5
altura = 7
retangulo= Retangulo(base, altura)
area_do_retangulo = retangulo.calcular_area()
print(f"A área do retângulo é {area_do_retangulo}")

# 4 Questão:

class ContaBancaria:
    def __init__(self, titular,saldo=0):
        self.saldo = saldo
        self.titular = titular

    def depositar (self,valor):
        if valor > 0:
            self.saldo += valor
            return f"Depósito de R${valor:.2f} realizado com sucesso. Novo saldo: R${self.saldo:.2f}"
        else:
            return "O valor do depósito inválido"
        

    def sacar (self, valor):
        if valor > 0 :
          if self.saldo >= valor:
            self.saldo -= valor
            return f"Saque de R${valor:.2f} realizado com sucesso. Novo saldo: R${self.saldo:.2f}"
          else:
              return "Saldo insuficiente!"
        else:
          return "O valor do saque inválido"
        
conta = ContaBancaria("Thauan", 2500)
print(conta.depositar(500))
print(conta.sacar(200))

# 5 Questão:

class Pessoa:
    def __init__(self,nome, idade):
        self.nome = nome
        self.idade = idade
    def falar (self):
        return f"Meu nome é {self.nome} e tenho {self.idade} anos."
    

nomePessoa = Pessoa("Thauan", 24)
print(nomePessoa.falar())

# 6 Questão:

class Produto:
    def __init__(self,nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    
    def calcular_total(self):
        total = self.preco * self.quantidade
        return f"O preço total é de: {total} "
    


produto = Produto("Régua", 3.99, 6)
print(produto.calcular_total())

# 7 Questão:

class Carro:
    def __init__(self,marca,modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def detalhes(self):
        return f"A marca é {self.marca}, modelo {self.modelo} e ano {self.ano}"
    

carro = Carro("Honda", "Civic", 2023)

print (carro.detalhes())

# 8 Questão:

class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def calcular_media(self):
        media = (self.nota1 + self.nota2) / 2
        return f"A média final é de: {media}"
    

aluno = Aluno("Thauan", 8,6)
print(aluno.calcular_media())

# 9 Questão:

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        
    def calcular_perimetro(self):
        calcular_perimetro = self.lado1 + self.lado2 + self.lado3
        return f"O perimêtro é: {calcular_perimetro}"
    


triangulo = Triangulo(8,7,6)
print(triangulo.calcular_perimetro())

# 10 Questão:

class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo
    
    def aumentar_salario(self):
        porcetagem = (0.10 * self.salario)
        aumento = porcetagem + self.salario
        return f"{self.nome}, que ocupa o cargo de {self.cargo}, teve seu salario de R${self.salario:.2f} reais, \natualizado com o reajuste de 10% anual, ficou R${aumento:.2f} reais"


funcionario = Funcionario("Thauan", 7000, "Programador")
print(funcionario.aumentar_salario())

