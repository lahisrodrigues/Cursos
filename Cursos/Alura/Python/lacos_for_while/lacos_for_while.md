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
### Break

Permite que saia imediatamente de um laço, mesmo que a condição para continuar seja verdadeira
```
nomes = ["PM3", "Alura", "Latam", "Outros"]
for nome in nomes:
     if nome == "Alura":
          print("Nome encontrado! Saindo do laço.")
          break
     print(nome)
```
Neste exemplo, assim que o laço percorrer os nomes e encontrar "Alura", irá imprimir que o nome foi encontrado e sairá do laço, e não vai imprimir os proximos nomes.

### Continue
Perimite que você pula a próxima iteração do laço, ignorando o restante do código na iteração atual.
```
nomes = ["PM3", "Alura", "Latam", "Outros"]
for nome in nomes:
     if nome == "Alura":
          print("Ignorando Alura.")
          continue
     print(f"Nome: {nome}")
```
Neste exemplo, quando o laço encontra "Alura" ele imprime "Ignorando Alura" e salta a impressão de Alura, continuando com os outros nomes da lista.

### Funções úteis em laços

```len()``` utilizada para ter o nome da listra, string ou outro tipo de coleção. Ela permite saber quantas iterações vão ter no laço  
```range()``` gera uma sequência de números, que é frequentemente utilizada para saber a quantidade de iterações no laço ```for```. Com ela tambem podemos definir um espaço de números para iterar, podendo definir um passo. Por exemplo, um ```range(6)```, gera números de 0 a 5, permitindo que o laço execute cinco vezes.

