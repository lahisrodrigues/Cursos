# Atividade 1

clientes = ["João", "Maria", "Carlos", "Ana", "Beatriz"]

for nome in clientes:
    print(nome)


# Atividade 2

contador = 0

while contador < 10:
     print("Processando dados")
     contador += 1

# Atividade 3
# minha resposta
mensagem = "Seja bem vindo ao buscante"
contador = 0

while contador < 5:
    print(mensagem)
    contador +=1

# resposta do instrutor utilizando o for com range é mais enxuta e sabe quantas vezes vai precisar emitir a mensagem, por isso é mais indicada
for i in range(5):
    print("Bem-vindo ao Buscante!")

# Atividade 4

valores = [10, 20, 30, 40, 50]
soma = 0
for numero in valores:
    soma += numero
print(f"A soma dos valores é {soma}")

# Atividade 5

projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]
for projeto in projetos:
    if projeto == None:
        print("Projeto ausente")
    else:
        print(projeto)

# Atividade 6

livros = ["1984", "Dom Casmurro", "O Pequeno Príncipe", "O Hobbit", "Orgulho e Preconceito"]
for livro in livros:
    if livro == "O Hobbit":
        print(f"Livro encontrado: {livro}")
        break

# Atividade 7

estoque = 5
# minha resposta. O if ali é desnecessário pois o mais elegante é colocar o print para fora do laço, mas das duas formas está correto
while estoque > 0:
    estoque -= 1
    print(f"Venda realizada! Estoque restante: {estoque}")
    # if estoque == 0: # o print viria depois
print("EStoque esgotado")

# Atividade 8

for contagem in range(10, 0, -1):
    if contagem % 2 == 0:
        print(f"Faltam apenas {contagem} segundos - Não perca essa oportunidade!")
    else:
        print(f"A contagem continua: {contagem} segundos restantes.")
print("Aproveite a promoção agora!")

# Atividade 9
# minha resposta, é mais legível, verifica somente se o estoque é positivo e imprime
livros = [

    {"nome": "1984", "estoque": 5},

    {"nome": "Dom Casmurro", "estoque": 0},

    {"nome": "O Pequeno Príncipe", "estoque": 3},

    {"nome": "O Hobbit", "estoque": 0},

    {"nome": "Orgulho e Preconceito", "estoque": 2}

]

for livro in livros:
    if livro["estoque"] > 0:
        print(f'Livro disponível: {livro["nome"]}')
# Resposta do instrutor, ela verifica se o estoque é igual a 0, se for, ela continua e depois imprime somente o estoque disponível
for livro in livros:
    if livro["estoque"] == 0:
        continue
    print(f"Livro disponível: {livro['nome']}")

# Atividade 10

while True:
    nome = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")

    if len(nome) < 5:
        print('O nome de usuário deve ter pelo menos 5 caracteres.')
    if len(senha) < 8:
        print('A senha deve ter pelo menos 8 caracteres.')
    else:
        print("Cadastro realizado com sucesso!")
        break