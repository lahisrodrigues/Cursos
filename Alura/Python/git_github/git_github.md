## Criando repositório
Lugar onde código dos projetos  
Repositório é único na sua conta  

GitHub: plataforma onde vamos hospedar o código  
Git: ferramenta onde fazemos o controle de versões do código  

`git init`: usamos para transformar o diretorio do projeto em um repositório Git e deve ser executado apenas uma vez pois quando executado ele configura o diretório atual para ser rastreado pelo Git, inicializando um repositório vazio  
`git add .`: adiciona todos os arquivos de uma vez no repositório
`git commit -m " "`: coloca uma mensagem ao commit
`git push`: sincroniza as mudanças do repositório local com o repositório remoto
`git remote add`: vincula o repositório remoto ao nosso repositório local e precisamos utilizar um protocolo seguro como HTTPS ou SSH

### Para fazer a chave SSH
A geração da chave SSH é feita com `ssh-keygen -t ed25519 -C "SEU EMAIL AQUI"`
Vai aparecer a primeira pergunta que vai ser sobre o diretório onde vamos guardar a chave, e entre parênteses é o reporitório padrão, recomendado é apenas apertar  `enter`, pois assim o Git encontra a chave automaticamente sempre que executamos o `git push`.
Depois vaia aparecer uma pergunta sobre cadastrar uma senha, e se voce colocar essa senha, em todo push terá que colocar tal senha. Se apertar somente `enter` a chave será gerada sem a proteção de senha
E por fim, a terceira pergunta, que é para apenas confirmar a senha anterior
Depois vai exibir uma mensagem no terminal, onde a primeira linha é do diretório, e nesse diretório tem dois aquivos que representam a chave SSH, um para chave privada e outra para chave pública.
Após isso, por fim, é so cadastrar a chave SSH no GitHub, colocando o titulo, o tipo de chave e depois o conteúdo da chave pública do diretório

## git remote

`git remote add apelido url`

'apelido': nome que atribui ao repositório remoto. Geralmente utiliza nomes descritivos, como "origin", mas pode escolher o que faz sentido

'url': insere a URL do repositório remoto, é unica e serve como endereço para acessar e interagir com ele pela internet

`git remote -v`: lista os repositórios remotos associados ao seu projeto local. Vai retornar uma lista dos repositórios remotos vinculados ao seu projeto, juntamente com sua URLs

`git remote remove apelido`: caso não precise de um r epositório remoto específico. Substitua apelido pelo nome do repositório

`git remote set-url apelido nova_url`: as vezes é necessário atualizar a URL de um repositório remoto.

`git remote rename apelido novo-apelido`: renomea um repositório remoto

## git status

`git status`: verifica o estado atual do código

## git log

`git log`: histórico de commit do projeto

## Sinalizações em arquivos do VSCode

M: Modified, modificado, arquivo já existia no repositório, mas recebeu alguma modificação que ainda não foi registrada
U: Untracked, não rastreado, ou sej,a não existia no repositório e ainda não teve seu commit feito

## git pull

`git pull`: puxa os commit do repositório remoto

## git revert
`git revert (chave do commit)`: desfaz um commit, e com isso utiliza o `git log` para ver o ID do commit que quer desfazer

## git reset
`git reset --hard (chave do commit anterior, pra onde quer voltar)`

## git commit --amend -m ""

`git commit --amend -m ""`: altera a mensagem do último commit, sem a necessidade de apagá-lo

## .gitignore
`.gitignore`: informa ao Git quais arquivos vai ignorar