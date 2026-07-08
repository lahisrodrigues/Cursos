# Python: trabalhando com projetos

Biblioteca que podemos usar:

```
import random
 
numero = random.randint(1, 10)
print(numero)
```
`try`(tentar): tenta operar o código
`execpt`: é uma exceção que dá uma mensagem de texto
    `ValueError`(Entrada Inválida): Ocorrer quando tentamos converter um valor que não pode ser transformado no tipo esperado. Ex: `float(abc)` Soluçao: Tratar erro com o bloco `try/except`
    `TypeError`(Tipo inválido): Ocorre quando realizamos operações imcompativeis com os tipos de dados. Ex: `10 + "5"`. Solução: Converter valores antes de operações. Ex: `int(5)`
    `IndexError`(Índice fora da lista): Ocorre ao tentar acessar uma chave que não existe em um dicionário. Usar `.get("chave", valor_padrao)` para evitar erro.
    `KeyError`(KeyError): Ocorre ao tentar acessar um índice que não existe em uma lista. Ex: acessar `lista[5]` em um lista de 3 itens. Solução: Conferir `len(lista)` antes de acessar um índice
    `ImportError`(Erro de importação): Ocorre quando o módulo é encontrado mas nao pode ser carregado corretamente. Solução: Verificar se o módulo está instalado e disponível
    `ModuleNotFoundError`(Módulo não encontrado): Ocorre quando tentamos importar um módulo que não está instalado ou não existe. Solução: Garantir que o módulo está instalado com `pip install modulo`
    `AttributeError`(Atributo inexistente): Ocorre quando tentamos acessar um atributo ou método que não existe em um objeto. Ex: `"abc".append(5)`.
    `SyntaxError`(Sintaxe Inválida): Ocorre quando há erro na escrita do código, comoesquecer : ou (). Ex: Revisar a sintaxe e corrigir erros antes decordar o código
    
## Passos
Passo 1: definir o problema
Passo 2: Organizar a execução e o passo a passo do projeto
Passo 3: Estruturar o projeto
Passo 4: Escrever o código
Passo 5: Testar e refinar o código

# Cntador de palavras
Passo 1: entrada e processamento de dados
Passo 2: criar a contagem das palavras
Passo 3: exibir a contagem
Passo 4: Testar e refinar o código

## cria arquivo contador.py
```
frase = input("Digite uma frase: ")
palavras = frase.split()
print(len(palavras))
print(palavras)
```
## aprimorando o código
crie uma função para o contador

```
def contar_palavras(frase):
    palavras = frase.split()
    print(palavras)
    return len(palavras)
```

crie um arquivo `main.py` para executar os testes no mesmo diretório que o `contador.py`


```
from contador import contar_palavras

frase = input("Digite uma frase: ")
quantidade = contar_palavras(frase)
print(f"A frase tem {quantidade} palavras")
```
Saída: 'Digite uma frase: livros são livros.
['livros', 'são', 'livros.']
A frase tem 3 palavras.
'

3:10 entradas do usuário