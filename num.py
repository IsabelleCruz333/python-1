# definimdo um função
def dobrar_numero():
    numero = float(input("Digite um numero: "))
    resultado = numero * 2
    return resultado
print('O dobro do numero é:   ',dobrar_numero())

# exercicio 2 - crie uma função que soma dois numeros inteiros
def somar_numeros():
    numero1 = float(input("Digite o primeiro numero: "))
    numero2 = float(input("Digite o segundo numero: "))
    resultado = numero1 + numero2 
    return resultado
print(' A soma dos numeros é:   ',somar_numeros())

# exercicio 3 - crie uma função que forneça o modulo do numero
def valor_absoluto():
    numero = float(input("Digite um numero:  "))
    resultado = abs(numero)
    return resultado
print(' O modulo do numero é:  ',valor_absoluto())

# exercicio 4 - calcule o modulo do quadrado de n
def quadrado_de_n():
    numero = float(input("Digite um numero:  "))
    resultado = numero ** 2
    return resultado
print(' O modulo do numero é:  ',quadrado_de_n())

# exercicio 5 - crie um código para calcular o fatorial de um numero 
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n-1)
    n = int(input('Digite o numero que voce quer calcular:  '))
    print("O fatorial de",n,"é",fatorial(n))

# exercicio 6 - crie uma função que retorna o maior entre dois
def busca_maior():
    numero1 = float(input("Digite o primeiro numero:  "))
    numero2 = float(input("Digite o segundo numero:  "))
    if numero1 > numero2:
        return numero1
    else:
        return numero2
    print(' O maior numero é:  ',busca_maior())

# exercicio 7 - crie uma função que retorne o antecessor do numero 
def buscar_antecessor():
    numero = float(input("Digite um numero:  "))
    antecessor = numero - 1
    return antecessor
print(' O antecessor é:  ',buscar_antecessor())

# exercicio 8 - crie uma função que retorna o menor entre dois numeros
def buscar_menor():
    numero1 = float(input("Digite o primeiro numero:  "))
    numero2 = float(input("Digite o segundo numero:  "))
    if numero1 < numero2:
        return numero1
    else:
        return numero2
print(' O numero menor é:   ',buscar_menor())

# exercicio 9 - crie uma função que verifica se um numero é par
def verificar_par():
    numero = int(input("Digite um numero:  "))
    if numero % 2 == 0:
        return print("O numero é par: ")
    else:
        return print("O numero é impar: ")
print(verificar_par())

# exercicio 10 - crie uma função para calcular a raiz quadrada de um numero
import math 

def calcular_raiz_quadrada():
    numero = float(input("Digite um numero: "))
    raiz_quadrada = math.sqrt(numero)
    return raiz_quadrada
print('A raiz quadrada é: ',calcular_raiz_quadrada())

# exercicio 11 - crie um codigo para somar dois numeros complexos
def somar_numeros_complexos(num1, num2):
    real = num1[0] + num2[0]
    imaginaria = num1[1] + num2[1]
    resultado = (real,imaginaria)
    return resultado

# solicita as partes real e imaginaria do primeiro numero complexo
real1 = float(input("Digite a parte real do primeiro numero complexo: "))
imaginaria1 = float(input("Digite a parte imaginaria do primeiro numero complexo: "))

# solicita as partes real e imaginaria do segundo numero complexo
real2 = float(input("Digite a parte real do segundo numero complexo: "))
imaginaria2 = float(input("Digite a parte imaginaria do segundo numero complexo: "))

# cria as representações dos numeros complexos como tuplas (parte real, parte imaginaria)
num1 = (real1,imaginaria1)
num2 = (real2,imaginaria2)

# realiza a soma dos numeros complexos
soma = somar_numeros_complexos(num1, num2)

# exibe o resultado
print('A soma dos numeros complexos é:', soma)

# exercicio 12 - crie um codigo completo e detalhado que retorne as duas raizes de uma equação de segundo grau usando a formula de baskhara
import math 

def calcular_raizes(a, b, c):
    discriminante = b**2 - 4*a*c
    
    if discriminante > 0:
        raiz1 = (-b + math.sqrt(discriminante)) / (2*a)
        raiz2 = (-b - math.sqrt(discriminante)) / (2*a)
        return raiz1, raiz2
    elif discriminante == 0:
        raiz = -b / (2*a)
        return raiz, raiz
    else:
        parte_real = -b / (2*a)
        parte_imaginaria =  math.sqrt(discriminante) / (2*a)
        raiz1 = complex(parte_real, parte_imaginaria)
        raiz2 = complex(parte_real, -parte_imaginaria)
        return raiz1, raiz2


    
