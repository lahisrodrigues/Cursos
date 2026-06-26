# Anotações sobre laços, for e while
Laços de repetição são estruturas que permitem executar um código repetidamente enquanto a condição for verdadeira. Temos laços de repetição no Python que é o for e while.
A leitura de um laço de repetição pode ser lida como: repita até que a condição se torne falsa.

## Sintaxe do laço for
Utilizado para executar um bloco de código para cada elemento do iterável. Útil quando você sabe exatamente quantas iterações deseja reralizar.
```
for elemento in iterável: # Dois pontos e o in são obrigatórios

# elemento = cada item indivusal do iterável que é processado dentro do laço
# iterável: é um acoleção de valores, como listas, tuplas, dicionários, entre outros.
```
### Exemplo de laço FOR

```
nomes = ["Carlos", "Ana", "Pedro", "Maria"]

for nome in nomes:
     print(nome)  
```
Primeiro, cria uma lista com os nomes, em seguida criamos um laço for para percorrer todos os nomes da lista e exibir na tela.
O termo "nome" é somente um identificador de cada elemento da lista que vamos percorrer com o laço for. Pode colocar qualquer outro nome de váriavel que faça sentido no contexto.

## Sintaxe do laço While
Executa o bloco de código enquanto a condição especificada for verdadeira. É útil quando não se sabe exatamente a quantidade de iterações serão necessárias, já que a condição depende do resultado da condição de cada iteração.
```
while condicao:
```
A condição é qualquer expressão que resulta em um valor booleano (True or False)
### Operadores de comparação
Igualdade (==), diferente (!=), maior que (>), maior ou igual (>=), menor que (<), menor ou igual (<=)

### Exemplo de laço WHILE
```
contador = 0

while contador < 5:
     print(f"Contador atual: {contador}")
contador +=1
```
Primeiro, cria uma variável com o contador igual a 0. O contador serve para garantir eventualmente que a condição se torne falsa.
O laço while verifica a condição contador < 5. Enquanto a condição for verdadeira o código dentro do laço continua sendo executado.
Dentro do laço imprimimos o contador atual, e depois incrementamos o contador com += 1, esse processo repete até que se torne falsa, ou seja, chegue até no < 5

### Loop Infinito

É quandoi um laço de repetição executa sem parar, porque a condição dele nunca se torna falsa.
```
contador = 0

while contador < 5:
     print("Contador:", contador)
```
