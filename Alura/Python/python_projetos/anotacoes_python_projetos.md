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
    `AttributeError`(Atributo inexistente): Ocorre quando tentamos acessar um atributo ou método que não existe em um objeti. Ex: `"abc".append(5)`.
    `SyntaxError`(Sintaxe Inválida):