# Funções

São blocos de códigos reutilizáveis que executam uma tarefa específica

```
def nome_da_funcao(parametros):
    # Bloco de código da função
    return valor_opcional
```  
    
Sua sintaxe é definica pela palavra-chave ```def```, seguida do nome da função e os parenteses que podem conter os parâmetros.  
O bloco de código é identado e pode conter um retorno opcional com o ```return```.


```
def ola_mundo(nome):
    return f"Olá, {nome}!"

ola_mundo("Lais")
```
Os parêmtros(nome) são variáveis definidas na declaração da função, pode ser opcionais ou obrigatórias, sendo usada para tornar as funções mais flexíveis, permitindo que elas processem diferentes valores sem precisar modificar o código.
E para chamar a função, basta usar o nome da função seguido de parênteses.
Podem ser chamados tambem de Argumentos que são os valores quer são passados para a função quando ela é chamada, caso a função tenha um parâmetro obrigatório.

## Funções simples

São funções criadas e personalizadas pelo dev para realizar funções específicas

```
def somar(a, b):
    soma = a + b
    return soma
```
Essa função recebe dois parâmetros e retorna a soma desses valores.
As variavéis que estão dentro do bloco de código (soma), são locais, ou seja, não podem ser acessadas fora do seu bloco de código.

## Funções com parâmetros padrão

São funções que permitem definir valores padrão para os parâmetros caso nenhum argumento seja passado
``` 
def cumprimentar(nome="Visitante"):
    print(f"Olá, {nome}!")

cumprimentar() # Saída: Olá, Visitante!

cumprimentar("Jade") # Saída: Olá, Jade!

```
Se nenhum parâmetro for passado, o padrão será "Visitante", caso contrário, se um nome for fornecido, ele será usado na saudação.

## Funções built-in

São funções já incorporadas no Python, que podem ser utilizadas diretamente sem precisar importá-las ou defini-las.

### Referente a interação, temos:
```print()```  
```input()```

### Para manipulação, temos:
```type()``` = retorna tipo do objeto.  
```tipe(10)```, saída será <class 'int'>

```isinstance()``` = verifica se op objeto pertence a um tipo específico ou a uma tupla de tipos. Retorna ```True``` se for do tipo indicado, caso contrário ```False```.  
```isinstance(10.5, int)```, saída será ```False```  
```isinstance("Python", (int, str))```, saída será ```True```  

```len``` = retorna o tamanho de uma string, lista ou tupla  
```len("Python")```, saída será 6

### Conversão e criação de tipos, temos:

```str()``` = converte valor para string  
```str(123)```, saída será "123"

```int()``` = converte valor para inteiro  
```int("10")```, saída será 10

```float()``` = converte valor para decimal  
```float("3.14")```, saída será 3.14

```bool()``` = converte falor para ```True``` ou ```False```  
```bool(1)```, saída será ```True```

```list()``` = converte um iterável para lista  
```list("abc)```, saída será ``["a", "b", "c"]``  

```dict()``` = cria um dicionário  
``dict(nome="Ana")``, saída sería {"nome": "Ana"}

```set()``` = cria um conjunto  
```set([1, 2, 3])```, saída será {1, 2, 3}  

### Funções matemáticas, temos:
```abs()``` = retorna valor absoluto de um número  
```abs(-10)```, saída será "10"

```round()``` = arredonda um número  
```round(3.1415, 2)```, saída será 3.14

```max()``` = retorna valor maior entre os fornecidos  
```max(3, 5, 1)```, saída será 5

```min()``` = retorna valor menor entre os fornecidos  
```min(3, 5, 1)```, saída será 1

```sum()``` = retorna a soma de uma lista de números  
```sum([1, 2, 3])```, saída será 6

### Funções que trabalham com funções iteráveis:

```filter(operação, iterável)``` = filtra elementos de um iterável com base em uma condição  
```list(filter(lambda x : x > 2, [1, 2, 3, 4]))```, saída será [3, 4]

```map(função, iterável)``` = aplica a função em cada elemento de um iterável  
```list(map(lambda x : x*2, [1, 2, 3]))```, saída será [2, 4, 6]

```zip(iterável, iterável2, ...)``` = une dois ou mais iteráveis, criando pares de elemntos correspondentes  
```list(zip([1, 2, 3], [a, b, c]))```, saída será [(1, "a"), (2, "b"), (3, "c")] 

```sorted(iterável, key=função, reverse=bool)``` = retorna uma nova lista ordenada a partir de um iterável. Pode receber um argumento key para personalizar a ordenação  
```sorted(3, 1, 4, 2)```, saída será [1, 2, 3, 4]

```reversed(iterável)``` = retorna um iterador com os elementos de um iterável na ordem inversa  
```list(reversed(1, 2, 3))```, saída será [3, 2, 1]  

### Documentação oficial de funções build in
https://docs.python.org/3/library/functions.html

## Funções recursivas

São aquelas que chamam a si mesmas para resolver um problema repetitivo até atingir uma condição de parada

```
def fatorial(n):
    if n == 0: # condição de parada
        return 1
    return n * fatorial(n - 1) # chamada recursiva

print(fatorial(5)) # Saída: 120
```
São usadas para resolver problemas que podem ser subdivididos em subproblemas menores, como cálculos matemáticos e algoritmos de estrutura de dados.


## Funções anônimas (lambdas)

Lambda é uma função pequena e sem nome que podem ter múltiplos argumentos, mas apenas uma expressão

```
# Sintaxe
lambda argumentos: expressão

soma = lambda a, b: a + b
print(soma(3, 5)) # Saída: 8
```
Lambdas são úteis para operações simples ou quando precisamos de funções curtas dentro de outras funções

## Funções dentro de funções (closures)

Closure é uma funçao interna que lembra do ambiente onde foi criada, mesmo após a execução da função externa ter terminado. Isso permite que ela mantenha o estado das variáveis sem a necessidade de usá-las globalmente.
```
def multiplicador(n): # Função externa
    def multiplica(x): # Closure
        return x * n # Usa a variavel 'n' da função externa
    return multiplica # Retorna a Função Interna

triplo = multiplicador(3)
valor = triplo(5)
print(valor) # Saída: 15 
```
As closures são úteis para encapsular lógicas e criar funçoes especializadas sem usar variáveis globais

Outro exemplo do uso dos Closures seria um gerador de saudção personalizado

```
def criar_saudacao(saudacao):
    def saudar(nome):
        return f"{saudacao}, {nome}"!
    return saudar

bom_dia = criar_saudacao("Bom dia")
boa_noite = criar_saudacao("Boa noite")
print(bom_dia("Vini")) # Saída: Bom dia, Vini!
print(boa_noite("Ana")) # Saída: Boa noite, Ana!
```
