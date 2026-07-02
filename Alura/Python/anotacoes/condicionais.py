## Atividade 1
numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print("O número  é Par")
else:
    print("O número é Ímpar")

## Atividade 2
user = int(input("Digite sua idade: "))
if user <= 12:
    print("Criança")
elif user < 18:
    print("Adolescente")
else:
    print("Adulto")

## Atividade 3

user = "lais"
password = "aluno1"

usuario = input("Digite seu nome: ")
senha = input("Digite sua senha: ")

if usuario == user and senha == password:
    print("Acesso liberado!")
else:
    print("Acesso negado")

## Atividade 4

x = float(input("Digite a coordenada x: "))
y = float(input("Digite a coordenada y: "))

if x > 0 and y > 0:
    print("O ponto está no primeiro quadrante.")
elif x < 0 and y > 0:
    print("O ponto está no segundo quadrante.")
elif x < 0 and y < 0:
    print("O ponto está no terceiro quadrante.")
elif x > 0 and y < 0:
    print("O ponto está no quarto quadrante.")
else:
    print("O ponto está sobre um eixo ou na origem.")