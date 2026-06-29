# # Exemplo Closures

# def multiplicador(n): # Função externa
#     def multiplica(x): # Closure
#         return x * n # Usa a variavel 'n' da função externa
#     return multiplica # Retorna a Função Interna

# triplo = multiplicador(3)
# valor = triplo(5)
# print(valor) # Saída: 15

# def criar_saudacao(saudacao):
#     def saudar(nome):
#         return f"{saudacao}, {nome}!"
#     return saudar

# bom_dia = criar_saudacao("Bom dia")
# boa_noite = criar_saudacao("Boa noite")
# print(bom_dia("Vini")) # Saída: Bom dia, Vini!
# print(boa_noite("Ana")) # Saída: Boa noite, Ana!

# # Exercicio 1

# def calcular_idade(ano_nasc, ano_atual):
#      return ano_atual - ano_nasc

# nascimento = int(input("Digite a data de nascimento: "))
# atual = int(input("Digite o ano atual: "))
# idade = calcular_idade(nascimento, atual)
# print(f"A idade é {idade} anos.")


# # Exercicio 2

# def qtd_letras(palavra):
#     return len(palavra)

# palavra = input("Digite uma palavra: ")
# print(f"A palavra tem {qtd_letras(palavra)} letras")

# # Exercício 3

def saudacao_personalizada(hora):
    if hora < 12:
        return "Bom dia"
    elif hora < 18:
        return "Boa tarde"
    else:
        return "Boa noite"

hora_atual = int(input("Digite a hora atual: "))
print(saudacao_personalizada(hora_atual))