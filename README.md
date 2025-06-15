
# 📦 Sistema de Gerenciamento de Estoque e Vendas

Este projeto é um sistema simples de gerenciamento de produtos, clientes e vendas desenvolvido em Python, utilizando conceitos fundamentais de Programação Orientada a Objetos (POO).

## 🚀 Funcionalidades

✔️ Cadastro de produtos (nome, preço e quantidade)  
✔️ Baixa de estoque (remoção de quantidade específica de um produto)  
✔️ Remoção de produtos do sistema  
✔️ Cadastro e visualização de clientes (nome e CPF)  
✔️ Adição de produtos no carrinho de vendas  
✔️ Visualização de itens no carrinho com cálculo do subtotal e total da compra  
✔️ Finalização da venda com atualização automática do estoque  

## 🛠️ Tecnologias Utilizadas

- Python 3.x
- Paradigma de Programação Orientada a Objetos (POO)
- Tipagem com anotação de tipos (`type hints`)
- Uso de propriedades com `@property`

## 📂 Estrutura do Projeto

```
📦 projeto-estoque-vendas
 ┣ 📜 main.py
 ┗ 📜 README.md
```

## 📋 Como Executar

1. Certifique-se de ter o **Python 3.x** instalado.
2. Clone este repositório ou baixe o arquivo `main.py`.
3. No terminal, navegue até a pasta onde está o arquivo e execute:

```bash
python main.py
```

4. Use o menu interativo para utilizar as funções do sistema.

## 🎯 Fluxo Principal do Programa

1. Cadastro de produtos.
2. Controle de estoque (baixa e remoção).
3. Adição de produtos ao carrinho.
4. Visualização e finalização da venda.
5. Atualização do estoque após a venda.

## 🏗️ Conceitos de POO Aplicados

- **Encapsulamento:** uso de atributos protegidos (ex: `_lista_produtos`, `_carrinho`).
- **Associação entre classes:** a classe `Vendas` depende da classe `Produtos`.
- **Uso de propriedades:** método `adicionar_produto_compra` usando `@property`.

## 👤 Autor

Desenvolvido por Emanuel Pinheiro De Freitas Mellina
