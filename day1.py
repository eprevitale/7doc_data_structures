import sys


list = []


def add_item():
    try:
        item_quantity = 0
        new_item = []
        item_to_be_added = input("Qual item deseja inserir?\n")
        item_quantity = input("Em qual quantidade?\n")
        for i in range(int(item_quantity)):
            new_item.append(item_to_be_added)
        list.append(new_item)
        print(f"{item_quantity} {item_to_be_added} adicionado(s).")

    except Exception as e:
        print(f"Erro ao tentar adicionar item: {e}")


def remove_item():
    try:
        item_to_be_removed = input("Qual o nome do item que deseja remover?\n")
        i = 0
        for item in list:
            if item_to_be_removed in item:
                list.remove(item)
                i += 1
        if i > 0:
            print(f"{item_to_be_removed} removido com sucesso!")
        else:
            print(f"{item_to_be_removed} não encontrado. Nenhum item foi removido")

    except Exception as e:
        print(f"Erro ao tentar remover item da lista: {e}")


def list_all_items():
    try:
        if list:
            print("\nItens adicionados:\n")
            print("No.\tItem\tQuantidade")
            for index, item in enumerate(list):
                print(f"{index}\t{item[0]}\t{len(item)}")
        else:
            print("\nNenhum item adicionado.")
        print("\n")    

    except Exception as e:
        print(f"Erro ao listar itens: {e}")


def menu():
    print("\nO que deseja fazer?")
    print("1: Adicionar item")
    print("2: Remover item")
    print("3: Listar todos os itens")
    print("0: Encerrar programa")
    choice = input()
    if choice == "1":
        add_item()
    elif choice == "2":
        remove_item()
    elif choice == "3":
        list_all_items()
    elif choice == "0":
        sys.exit(1)
    else:
        print("Por favor, selecione uma ação válida.")

    menu() # TODO eliminar recursividade - se a lista for longa, vai consumir MUITO processamento


menu()