class BombaDeCombustivel():
    def __init__(self, tipo_combustivel, preco_por_litro, quantidade_combustivel):
        self._tipo_combustivel = tipo_combustivel
        self._preco_por_litro = preco_por_litro
        self._quantidade_combustivel = quantidade_combustivel

    def reabastecer(self, quantidade):
        if quantidade < 0:
            raise ValueError("A quantidade não pode ser negativa")
        self._quantidade_combustivel += quantidade

    def abastecer_por_valor(self, dinheiro):
        if dinheiro < 0:
            raise ValueError("O valor não pode ser negativo")
        litros = dinheiro / self._preco_por_litro
        if litros > self._quantidade_combustivel:
            raise ValueError("Não há combustível suficiente na bomba")
        self._quantidade_combustivel -= litros
        return f"Pagamento: {dinheiro}, litros abastecidos: {litros}"

    def exibir_quantidade_combustivel(self):
        return f"Quantidade de combustível na bomba: {self._quantidade_combustivel} litros"

    @property
    def preco_por_litro(self):
        return self._preco_por_litro

    @preco_por_litro.setter
    def preco_por_litro(self, novo_preco):
        self._preco_por_litro = novo_preco
