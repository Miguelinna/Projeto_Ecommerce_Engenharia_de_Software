# loja_roupas.py
class Roupa:
    def __init__(self, id, nome, tamanho, preco, estoque):
        self.id = id
        self.nome = nome
        self.tamanho = tamanho
        self.preco = preco
        self.estoque = estoque
    def __str__(self):
        return f"{self.id} - {self.nome} (Tamanho: {self.tamanho}) | R${self. preco:.2f} | Estoque: {self.estoque}"
class LojaRoupas:
    def __init__(self):
        self.estoque = []
        self.carrinho = []
    def adicionar_roupa(self, roupa):
        self.estoque.append(roupa)
    def listar_estoque(self):
        print("\n Roupas disponíveis:")
        for roupa in self.estoque:
            print(roupa)
  def adicionar_ao_carrinho(self, id_roupa, quantidade):
        roupa = next((r for r in self.estoque if r.id == id_roupa), None)
        if roupa:
            if roupa.estoque >= quantidade:
                self.carrinho.append((roupa, quantidade))
                roupa.estoque -= quantidade
                print(f"\n {quantidade}x {roupa.nome} (Tamanho {roupa.tamanho}) adicionado(s) ao carrinho.")
            else:
                print("\n Estoque insuficiente.")
        else:
            print("\n Roupa não encontrada.")
    def ver_carrinho(self):
        print("\n Carrinho:")
        if not self.carrinho:
            print("Carrinho está vazio.")
            return
        total = 0
        for roupa, qtd in self.carrinho:
            subtotal = roupa.preco * qtd
            total += subtotal
            print(f"{qtd}x {roupa.nome} (Tamanho {roupa.tamanho}) - R${subtotal:.2f}")
        print(f"\n Total: R${total:.2f}")
    def finalizar_compra(self):
        if not self.carrinho:
            print("\n Carrinho está vazio.")
            return
        self.ver_carrinho()
        confirmar = input("Deseja finalizar a compra? (s/n): ").strip().lower()
        if confirmar == 's':
            self.carrinho.clear()
            print("\n Compra finalizada com sucesso!")
        else:
            print("\n Compra cancelada.")
def menu():
    loja = LojaRoupas()
    # Adicionando roupas ao estoque
    loja.adicionar_roupa(Roupa(1, "Camiseta Básica", "M", 49.90, 10))
    loja.adicionar_roupa(Roupa(2, "Calça Jeans", "G", 129.90, 5))
    loja.adicionar_roupa(Roupa(3, "Vestido Floral", "P", 99.90, 8))
    loja.adicionar_roupa(Roupa(4, "Jaqueta de Couro", "M", 249.90, 2))
    while True:
        print("\n=== MENU LOJA DE ROUPAS ===")
        print("1 - Listar roupas")
        print("2 - Adicionar ao carrinho")
        print("3 - Ver carrinho")
        print("4 - Finalizar compra")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            loja.listar_estoque()
        elif opcao == '2':
            try:
                id_roupa = int(input("ID da roupa: "))
                qtd = int(input("Quantidade: "))
                loja.adicionar_ao_carrinho(id_roupa, qtd)
            except ValueError:
                print(" Entrada inválida.")
        elif opcao == '3':
            loja.ver_carrinho()
        elif opcao == '4':
            loja.finalizar_compra()
        elif opcao == '0':
            print("\n Obrigado por visitar a nossa loja!")
            break
        else:
            print(" Opção inválida. Tente novamente.")
if __name__ == "__main__":
    menu()

