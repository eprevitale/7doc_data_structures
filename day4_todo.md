## FILAS

- Para atender pedidos de um restaurante
- Agilidade é necessária - velocidade no acesso às informações pode ser importante
- O volume de dados também não deve ser muito grande, então não deve ser preciso redimensionar o espaço de memória
- Portanto, as filas serão implementadas com arrays ao invés de listas encadeadas

### CLASSES

- Order (Pedido)
    - Nome do prato
    - Número da mesa do cliente

- OrdersQueue (Fila de Pedidos)
    - Adicionar pedido
    - Remover pedido
    - Listar todos os pedidos (em ordem)