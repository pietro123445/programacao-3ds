class Veiculo:
    def __init__(self, nome, custo_por_km):
        self.nome = nome
        self.custo_por_km = custo_por_km

    def calcular_custo(self, distancia):
        return distancia * self.custo_por_km

def calcular_custo_total_viagem(lista_veiculos, distancia=200):
    """
    Calcula o custo total de uma viagem de 200 km para todos os veículos na lista.
    """
    total = sum(veiculo.calcular_custo(distancia) for veiculo in lista_veiculos)
    return total

# Exemplo de uso:
if __name__ == "__main__":
    # Criando diferentes tipos de veículos
    carro = Veiculo("Carro", 0.50)  # R$ 0,50 por km
    caminhao = Veiculo("Caminhão", 2.50)  # R$ 2,50 por km
    moto = Veiculo("Moto", 0.20)  # R$ 0,20 por km

    frota = [carro, caminhao, moto]
    
    custo_total = calcular_custo_total_viagem(frota)
    print(f"O custo total para a viagem de 200km é: R$ {custo_total:.2f}")
