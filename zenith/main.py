from src.core import GerenciadorFinanceiro
from src.persistence import RepositorioJSON
from src.models import Gasto

def iniciar():
    gerenciador = GerenciadorFinanceiro()
    repo = RepositorioJSON()

    # Carregar dados existentes ao iniciar
    dados_salvos = repo.carregar()
    for item in dados_salvos:
        # Reconstruindo os objetos Gasto a partir dos dicionários do JSON
        g = Gasto(item['descricao'], item['valor'], item['categoria'], item['data'])
        gerenciador.gastos.append(g)

    while True:
        print("\n--- ZENITH: Controle de Gastos ---")
        print("1. Registrar Novo Gasto")
        print("2. Exibir Relatório")
        print("3. Ver Total Acumulado")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            try:
                desc = input("O que você comprou? ")
                vlr = float(input("Quanto custou? R$ "))
                cat = input("Qual a categoria? ")
                
                gasto = gerenciador.adicionar_gasto(desc, vlr, cat)
                repo.salvar(gerenciador.listar_todos())
                print(f"\n Sucesso: {gasto}")
            except ValueError:
                print("\n Erro: No valor, use apenas números e ponto (ex: 10.50)")

        elif opcao == "2":
            print("\n--- SEUS GASTOS ---")
            gastos = gerenciador.listar_todos()
            if not gastos:
                print("Nenhum gasto registrado ainda.")
            for g in gastos:
                print(g)

        elif opcao == "3":
            total = gerenciador.calcular_total()
            print(f"\n TOTAL ACUMULADO: R$ {total:.2f}")

        elif opcao == "4":
            print("\nEncerrando Zenith. Economize sempre!")
            break
        else:
            print("\n Opção inválida!")

if __name__ == "__main__":
    iniciar()