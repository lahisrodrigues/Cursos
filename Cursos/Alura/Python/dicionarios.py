pessoa = {'nome': 'lais', 'idade': '29', 'cidade': 'Pouso Alegre'}

pessoa['idade'] = 30
pessoa['profissão'] = 'engenheiro'
del pessoa['cidade']
print(pessoa)


meus_quadrados = {}
for x in range(1,6):
    conta = x * x
    meus_quadrados[x] = conta

print(meus_quadrados)
