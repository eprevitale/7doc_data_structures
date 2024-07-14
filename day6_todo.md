# HASHMAPS

As tabelas hash são estruturas de dados que permitem o armazenamento e acesso eficiente de elementos, através de um processo de mapeamento de chaves (keys) para valores (values) usando uma função hash.

A função hash é responsável por transformar a chave em um índice, que será utilizado para acessar o valor correspondente na tabela. Idealmente, a função hash deve gerar um índice único para cada chave, evitando colisões (quando duas ou mais chaves têm o mesmo índice).

A implementação da hash table geralmente é feita através de um array (ou vetor), onde cada elemento é uma lista encadeada. Cada lista encadeada é responsável por armazenar os pares chave-valor que foram mapeados para o mesmo índice.

Já o hashmap é uma estrutura de dados que é implementada através de uma tabela hash, e permite o armazenamento e acesso de pares chave-valor de forma eficiente. O hashmap é uma abstração da tabela hash (hash table), onde as operações são realizadas de maneira mais simplificada, abstraindo a complexidade da implementação da hash table.

## DESAFIO

### CLASSES

- Player (Jogador)
    - Nome
    - Pontos

- Game (Jogo)
    - Pontuação
    - Adicionar jogador
    - Remover jogador
    - Atualizar pontuação
    - Listar jogadores (em ordem decrescente)
    - Determinar vencedor