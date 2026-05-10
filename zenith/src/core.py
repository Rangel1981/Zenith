from src.models import Gasto

class GerenciadorFinanceiro:
    def __init__(self):
        self.gastos = []

    def adicionar_gasto(self, descricao, valor, categoria):
        novo_gasto = Gasto(descricao, valor, categoria)
        self.gastos.append(novo_gasto)
        return novo_gasto
    
    def listar_todos(self):
        return self.gastos
    
    def calcular_total(self):
        return sum(item.valor for item in self.gastos)