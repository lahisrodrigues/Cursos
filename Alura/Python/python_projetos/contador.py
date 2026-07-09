def limpar_texto(texto):
    texto = texto.lower() # colocar a palavra em toda minúscula
    caracteres = ".,!|?:\\'()[]{}\"áéíóúç"
    for char in caracteres:
        texto = texto.replace(char, "") # substituir o caracter por nada
    return texto 

def contar_palavras(frase):
    frase = limpar_texto(frase)
    if not frase.split():
        return {}
    
    palavras = frase.split()
    contagem = {}
    for palavra in palavras:
        contagem[palavra] = contagem.get(palavra, 0) + 1
    return contagem