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