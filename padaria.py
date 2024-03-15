class Pao:
    def __init__(self):
        self.farinha = float(input("Preço da farinha: "))
        self.sal = float(input("Preço do sal: "))
        self.fermento = float(input("Preço do fermento: "))
        self.custo = self.farinha + self.sal + self.fermento

class Padaria:
    def __init__(self):
        self.pao = Pao()

    def custo_op(self):
        return self.pao.custo

    def ganho(self):
        return self.pao.custo * 0.5 + self.pao.custo

padaria = Padaria()
print("Custo operacional da produção: ", padaria.custo_op())
print("Para ter um ganho de 50% sobre a unidade, o preço de venda deve ser: ", padaria.ganho())
