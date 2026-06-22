# exercício 1 e 2
pessoa = {'nome': 'lais', 'idade': '29', 'cidade': 'Pouso Alegre'}
pessoa['idade'] = 30
pessoa['profissão'] = 'engenheiro'
del pessoa['cidade']
print(pessoa)

# exercício 3
meus_quadrados = {}
for x in range(1,6):
    conta = x * x
    meus_quadrados[x] = conta
print(meus_quadrados)

# exercício 4
pessoa = {'nome': 'lais', 'idade': '29', 'cidade': 'Pouso Alegre'}
if 'nome' in pessoa:
    print('Existe essa chave')
else:
    print('Não existe essa chave')

# exercício 5 
frase = "o rato roeu a roupa do rei e o rato fugiu"
contagem = {}
for palavra in frase.split():
    if palavra in contagem:
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1
print(contagem)
