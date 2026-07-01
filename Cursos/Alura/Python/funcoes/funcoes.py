# Exemplo Closures

def multiplicador(n): # Função externa
    def multiplica(x): # Closure
        return x * n # Usa a variavel 'n' da função externa
    return multiplica # Retorna a Função Interna

triplo = multiplicador(3)
valor = triplo(5)
print(valor) # Saída: 15

def criar_saudacao(saudacao):
    def saudar(nome):
        return f"{saudacao}, {nome}!"
    return saudar

bom_dia = criar_saudacao("Bom dia")
boa_noite = criar_saudacao("Boa noite")
print(bom_dia("Vini")) # Saída: Bom dia, Vini!
print(boa_noite("Ana")) # Saída: Boa noite, Ana!

# Exercicio 1

def calcular_idade(ano_nasc, ano_atual):
     return ano_atual - ano_nasc

nascimento = int(input("Digite a data de nascimento: "))
atual = int(input("Digite o ano atual: "))
idade = calcular_idade(nascimento, atual)
print(f"A idade é {idade} anos.")

# Exercicio 2

def qtd_letras(palavra):
    return len(palavra)

palavra = input("Digite uma palavra: ")
print(f"A palavra tem {qtd_letras(palavra)} letras")

# Exercício 3

def saudacao_personalizada(hora):
    if hora < 12:
        return "Bom dia"
    elif hora < 18:
        return "Boa tarde"
    else:
        return "Boa noite"

hora_atual = int(input("Digite a hora atual: "))
print(saudacao_personalizada(hora_atual))

# Exercício 4

telefones = ["11987654321", "21912345678", "31987654321", "11911223344"]
def conversao_int(telefones):
    resultado = []
    for telefone in telefones:
        telefone = int(telefone)
        resultado.append(telefone)
    return resultado

def conversao_correta(lista_convertida):
    resultado = True # flag
    for telefone in lista_convertida:
        if not isinstance(telefone, int):
            resultado = False
    if resultado:
        print("Todos os números foram convertidos corretamente!")

lista_convertida = conversao_int(telefones)
conversao_correta(lista_convertida)

# Exercício 5

valores = input('Digite os valores das vendas: ').split()
total = sum(map(float, valores))
print(f'O total de vendas for: {total}')

# Exercício 6

numeros = input('Digite os números separados por espaço: ').split()
numeros_pares = (filter(lambda x: int(x) % 2 == 0, numeros))
print(f'Numeros pares:' " ".join(numeros_pares)) # o .join() fica melhor para o usuário visualizar a string

# Exercócio 7

produtos = input('Digite os produtos separados por vírgula: ').split(",")
precos = input('Digite os preços separados por vírgula: ').split(",")

def produtos_precos(prod, pre):
     for produto, preco in zip(prod, pre):
          print(f'{produto.strip()}: {preco.strip()}')

produtos_precos(produtos, precos)

# Exercicio 8

primeiro_numero = float(input('Digite o primeiro número: '))
segundo_numero = float(input('Digite o segundo número: '))
operacao = input('Escolha a operação (| + | - | * | / |): ')

def calculadora(p, s, op):
    if op == '+':
          soma = (lambda x, y: x + y)(p, s)
          print(f'O resultado é {soma}')
    elif op == '-':
          subtracao = (lambda x, y: x - y)(p, s)
          print(f'O resultado é {subtracao}')
    elif op == '*':
          vezes = (lambda x, y: x * y)(p, s)
          print(f'O resultado é {vezes}')
    elif op == '/':
          divisao = (lambda x, y: x / y if y != 0 else 'Erro: Divisão por 0.')(p, s)
          print(f'O resultado é {divisao}')
    else:
          print('Operação errada, encerrando programa...')
               
calculadora(primeiro_numero, segundo_numero, operacao)

# Exercício 9

desconto = float(input('Digite a porgentagem de desconto: '))
valor_compra = float(input('Digite o valor da compra: '))

def preco(v):
    def porcetagem(d):
        resultado = v - ((d / 100) * v)
        return resultado
    return porcetagem

valor_final = preco(valor_compra)(desconto)
print(f"Preço final com desconto: {valor_final}")

# Exercício 9

def soma(n):
    if n == 0:
        return 0
    return n + soma( n - 1)
    

numero = int(input('Digite um número: '))
resultado = soma(numero)
print(f'A soma de 1 a {numero} é: {resultado}')