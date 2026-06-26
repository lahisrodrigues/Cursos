# Anotações sobre laços, for e while
Laços de repetição são estruturas que permitem executar um código repetidamente enquanto a condição for verdadeira. Temos laços de repetição no Python que é o for e while.
A leitura de um laço de repetição pode ser lida como: repita até que a condição se torne falsa.

## Sintaxe do laço for
Utilizado para executar um bloco de código para cada elemento do iterável. Útil quando você sabe exatamente quantas iterações deseja reralizar
```
for elemento in iterável: # Dois pontos e o in são obrigatórios

# elemento = cada item indivusal do iterável que é processado dentro do laço
# iterável: é um acoleção de valores, como listas, tuplas, dicionários, entre outros.
```
##@ Exemplo  

```
nomes = ["Carlos", "Ana", "Pedro", "Maria"]

for nome in nomes:
     print(nome)  
```


Primeiro, cria uma lista com os nomes, em seguida criamos um laço for para percorrer todos os nomes da lista e exibir na tela.
O termo "nome" é somente um identificador de cada elemento da lista que vamos percorrer com o laço for. Pode colocar qualquer outro nome de váriavel que faça sentido no contexto

