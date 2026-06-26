# Atividade 1

maca = input('Digite a quantidade de maças vendidas: ')
banana = input('Digite a quantidade de bananas vendidas: ')

if maca > banana:
    print('As maças foram mais vendidas.')
elif banana > maca:
    print('As bananas foram mais vendidas.')
else:
    print('Ambas venderam a mesma quntidade')


# Atividade 2

atividadeA = int(input('Digite a quantidade de dias para atividade A: '))
atividadeB = int(input('Digite a quantidade de dias para atividade B: '))
atividadeC = int(input('Digite a quantidade de dias para atividade C: '))

if (atividadeA >= 0 and atividadeB >= 0 and atividadeC >= 0):
    tempo_total = atividadeA + atividadeB + atividadeC
    print(f'O total de dias para atividade é: {tempo_total}')
else:
    print('Erro: os dias não podem ser negativos.')


# Atividade 3

temperatura_atual = float(input('Digite a temperatura atual: '))

if temperatura_atual > 25:
    print('Alerta!! Temperatura acima do limite permitido.')
else:
    print('Temperatura está de acordo.')


# Atividade 4

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

IMC = peso/(altura ** 2)
print(f'Seu IMC é: {IMC:.2f}')

if IMC > 25:
    print('Você está acima do peso.')
elif IMC > 18.5:
    print('Voce está com peso normal.')
else:
    print('Você está abaixo do peso.')


# Atividade 5
limite = 3000
total_despesas = float(input('Digite o total de despesas deste mês (R$): '))

if total_despesas >= limite:
    print('Atenção!! Você superou o limite do orçamento.')
else:
    print('Ainda não superou o limite do orçamento.')


# Atividade 6
hora_atual = int(input('Digite a hora atual (formato 24 horas): '))
if (8 <= hora_atual <= 18 ):
    print('Acesso liberado.')
else:
    print('Acesso bloqueado.')


# Atividade 7 

primeira_nota = float(input('Digite a primeira nota: '))
segunda_nota = float(input('Digite a segunda nota: '))
terceira_nota = float(input('Digite a terceira nota: '))

media = (primeira_nota + segunda_nota + terceira_nota) / 3
if media >= 7:
    print('Você foi aprovado.')
elif 5 <= media < 7:
    print('Você está de recuperação.')
else:
    print('Você está reprovado.')


# Atividade 8 

distancia_percorrida = float(input('Digite a distancia percorrida: '))

if distancia_percorrida < 100:
    print('Valor do pedágio: R$ 10,00')
elif distancia_percorrida < 200:
    print('Valor do pedágio: R$ 20,00')
else:
    print('Valor do pedágio: R$ 30,00')

# Atividade 9 

numero = int(input('Digite um número inteiro: '))

if numero % 2:
    print(f'O número {numero} é impar.')
else:
    print(f'O numero {numero} é par.')

# Atividade 10

renda = float(input('Digite o valor da sua renda mensal: '))
parcela = float(input('Digite o valor da parcela deseja: '))

if renda > 2000 and parcela <= 0.3 * renda:
    print('Emprétimo aprovado.')
elif renda < 2000:
    print('Empréstimo negado! Valor de renda abaixo.')
else:
    print('Empréstimo negado. Parcela acima de 30% da renda')