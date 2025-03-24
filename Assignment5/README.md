# Language Processing

**Author:** Miguel Guimarães [(Github)](https://github.com/miguel-amg).

**University of Minho** - Bachelor's degree in Software Engineering

**Year 2024/2025**

# Assignment 5: Vending Machine
- Simulate a vending machine.
- Product stock: a list of triples, product name, quantity and price.
- Save the stock list in a JSON file that is loaded when the program starts and is updated when the program ends.
- Use your imagination and creativity and consider all scenarios, for example, non-existent product or empty stock.
- **(Extra)** Add a command to add some products to the existing stock (new or existing products).

## Examples:
**Stock example:**
```
stock = [
 {"cod": "A23", "nome": "água 0.5L", "quant": 8, "preco": 0.7},
 ...
]
```

**Command examples:**
```
maq: 2024-03-08, Stock carregado, Estado atualizado.
maq: Bom dia. Estou disponível para atender o seu pedido.
>> LISTAR
maq:
cod | nome | quantidade |  preço
---------------------------------
A23 água 0.5L 8 0.7
...
>> MOEDA 1e, 20c, 5c, 5c .
maq: Saldo = 1e30c
>> SELECIONAR A23
maq: Pode retirar o produto dispensado "água 0.5L"
maq: Saldo = 60c
>> SELECIONAR A23
maq: Saldo insufuciente para satisfazer o seu pedido
maq: Saldo = 60c; Pedido = 70c
>> ...
...
maq: Saldo = 74c
>> SAIR
maq: Pode retirar o troco: 1x 50c, 1x 20c e 2x 2c.
maq: Até à próxima
```
