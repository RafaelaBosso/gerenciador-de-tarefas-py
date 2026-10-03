# Gerenciador de Tarefas

Um gerenciador de tarefas simples desenvolvido em Python.

Este projeto surgiu a partir de um gerenciador de tarefas que desenvolvi anteriormente em C. A ideia de refazer o projeto em Python foi uma forma de praticar a linguagem e perceber como os mesmos conceitos poderiam ser aplicados em uma linguagem diferente.

**Versão anterior em C:** [Gerenciador de Tarefas em C](https://github.com/RafaelaBosso/gerenciador-de-tarefas-c)

## Funcionalidades

* Exibir todas as tarefas cadastradas
* Adicionar novas tarefas
* Definir prioridade para cada tarefa
* Marcar tarefas como concluídas
* Editar descrição ou prioridade
* Deletar tarefas
* Salvar as tarefas em um arquivo `.csv`
* Carregar automaticamente as tarefas salvas ao iniciar o programa
* Ordenar as tarefas por prioridade

### Níveis de prioridade

| Valor | Prioridade     |
| ----- | -------------- |
| 1     | Alta           |
| 2     | Média          |
| 3     | Sem prioridade |

## Tecnologias utilizadas

* Python 3
* Biblioteca `csv`
* Arquivo CSV para persistência dos dados

O projeto não utiliza bibliotecas externas, apenas recursos disponíveis na biblioteca padrão do Python.

## Como executar

Com o Python 3 instalado, execute o arquivo principal:

```bash
python GerenciadorDeTarefas.py
```

Dependendo da configuração do sistema, pode ser necessário utilizar:

```bash
python3 GerenciadorDeTarefas.py
```

O arquivo `tarefas.csv` será criado automaticamente quando as tarefas forem salvas.


## Como funciona

Ao iniciar o programa, as tarefas salvas no arquivo `tarefas.csv` são carregadas automaticamente.

Depois disso, o programa apresenta um menu com as opções disponíveis:

```text
1 - Exibir tarefas
2 - Adicionar tarefa
3 - Concluir tarefa
4 - Editar tarefa
5 - Deletar tarefa
6 - Sair
```

Sempre que uma alteração é feita, as informações são salvas no arquivo CSV.

Caso o arquivo `tarefas.csv` ainda não exista, o programa inicia com uma lista vazia e cria o arquivo quando uma tarefa for salva.

## Estrutura dos dados

Cada tarefa possui quatro informações:

```text
id
prioridade
concluida
descricao
```

Um exemplo de tarefa seria:

```text
ID: 1
Prioridade: 1
Concluída: False
Descrição: Estudar funções em Python
```

## O que pratiquei neste projeto

Durante o desenvolvimento, coloquei em prática alguns conceitos que estou estudando em Python, como:

* Funções
* Listas e dicionários
* Estruturas condicionais
* Laços de repetição
* `match/case`
* Tratamento de exceções com `try/except`
* Manipulação de arquivos
* Leitura e escrita de arquivos CSV
* `lambda` e `sorted()`
* Validação de entrada do usuário
* Organização do código em funções

## Relação com o projeto em C

A lógica geral deste projeto foi baseada no gerenciador de tarefas que desenvolvi anteriormente em C.

Ao recriá-lo em Python, mantive a ideia principal da aplicação, mas adaptei sua implementação para os recursos e características da linguagem. Isso também me permitiu comparar, na prática, algumas diferenças entre as duas linguagens e aplicar em Python conceitos que já havia utilizado no projeto em C.

**Projeto anterior:** [gerenciador-de-tarefas-c](https://github.com/RafaelaBosso/gerenciador-de-tarefas-c)

## Sobre o projeto

Este projeto foi desenvolvido de forma independente para colocar em prática o que venho aprendendo em Python.

A ideia surgiu a partir de um gerenciador de tarefas que eu havia desenvolvido anteriormente em C. Recriar o projeto em Python foi uma forma de praticar a linguagem e perceber como os mesmos conceitos poderiam ser aplicados de uma maneira diferente.

Este projeto representa uma etapa do meu aprendizado em programação e também serviu como base para continuar avançando para projetos mais complexos.
