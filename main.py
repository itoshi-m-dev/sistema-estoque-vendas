class Produtos:
    def __init__(self):
        self._lista_produtos = []
    
    def cadastrar_produtos(self):
        nome = input('Digite o nome do produto que deseja cadastrar: ')
        preco = float(input('Digite o preço do produto: '))
        quantidade = int(input('Digite a quantidade disponivel no estoque: '))

        produto = {
            'nome': nome,
            'preco': preco,
            'quantidade': quantidade
        }

        self._lista_produtos.append(produto)
        print(f'Produto {nome} adicionado com sucesso')


    def baixar_estoque(self):
        nome = input('Digite o nome do produto que deseja baixar no estoque: ')
        quantidade = int(input('Agora digite a quantidade: '))

        for produto in self._lista_produtos:
            if produto['nome'] == nome:
                if produto['quantidade'] >= quantidade:
                    produto['quantidade'] -= quantidade
                    print(f'{quantidade} unidade(s) de {nome} removidas do estoque')
                else:
                    print('Estoque insuficiente')
                    break
            else:
                print('Produto nao encontrado')
            
    def remover_produto(self):
        nome = input('Digite o nome do produto: ')

        for produto in self._lista_produtos:
            if produto['nome'] == nome:
                self._lista_produtos.remove(produto)
                print(f'{nome} produto removido com sucesso')
                break
            else:
                print('Produto não encontrado')


class Clientes:
    def __init__(self, nome,cpf):
        self.nome = nome
        self.cpf = cpf

    def mostrar_dados(self):
        print(f'Nome: {self.nome}')
        print(f'CPF: {self.cpf}')


class Vendas:
    def __init__(self,produtos: Produtos):
        self._produtos = produtos
        self._carrinho = []
    
    @property
    def adicionar_produto_compra(self):
        nome = input('Digite o nome do produto: ')
        qtd = int(input('Digite sua quantidade: '))
        
        for produto in self._produtos._lista_produtos:
            if produto['nome'] == nome:
                if produto['quantidade'] >= qtd:
                    item = {
                        'nome': nome,
                        'preco': produto['preco'],
                        'quantidade': qtd,
                        'subtotal': produto['preco'] * qtd
                    }
                    self._carrinho.append(item)
                    print(f'{qtd} unidade(s) de {nome} adicionadas ao carrinho.')
                else:
                    print('Estoque insuficiente.')
                break
        else:
            print('Produto não encontrado.')

    def mostrar_carrinho(self):
        if not self._carrinho:
            print('Carrinho vazio')
            return
        
        print('\n ---- ITENS NO CARRINHO ----')
        total = 0
        for item in self._carrinho:
            print(f"{item['nome']} - {item['quantidade']} x {item['preco']:.2f} = {item['subtotal']:.2f}")
            total += item['subtotal']
            print(f"TOTAL: R$ {total:.2f}\n")

    def finalizar_venda(self):
        if not self._carrinho:
            print("Carrinho vazio. Nenhuma venda foi realizada.")
            return
        
        for item in self._carrinho:
            for produto in self._produtos._lista_produtos:
                if produto['nome'] == item['nome']:
                    produto['quantidade'] -= item['quantidade']

        print("Venda finalizada com sucesso!")
        self.mostrar_carrinho()
        self._carrinho = []


def menu():
    produtos = Produtos()
    vendas = Vendas(produtos)

    while True:
        print("\n===== MENU =====")
        print("1 - Cadastrar produto")
        print("2 - Baixar estoque")
        print("3 - Remover produto")
        print("4 - Adicionar produto à venda")
        print("5 - Ver carrinho")
        print("6 - Finalizar venda")
        print("0 - Sair")

        opcao = input('Escolha uma opçao: ')
        
        if opcao == '1':
            produtos.cadastrar_produtos()

        elif opcao == '2':
            produtos.baixar_estoque()

        elif opcao == '3':
            produtos.remover_produto()

        elif opcao == '4':
            vendas.adicionar_produto_compra

        elif opcao == '5':
            vendas.mostrar_carrinho()

        elif opcao == '6':
            vendas.finalizar_venda()

        elif opcao == '0':
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
