from typing import List


class Grafo:
    def __init__(self, direcionado:bool) -> None: #criar grafo
    # Cria e retorna uma matriz de adjacência vazia e uma lista de vértices.

    # Passos:
    # 1. Criar uma lista vazia chamada matriz (para armazenar as conexões).
    # 2. Criar uma lista vazia chamada vertices (para armazenar os nomes dos vértices).
    # 3. Retornar (matriz, vertices).
        self.direcionado = direcionado
        self.matriz = []
        self.vertices = []

    def vizinhos(self, vertice):
                # [       A  B  C
                #     A: [0, 0, 0]
                #     C: [0, 0, 0]
                #     B: [0, 0, 0]
                # ]
        """
        Retorna a lista de vizinhos (vértices alcançáveis a partir de 'vertice').

        Passos:
        1. Verificar se 'vertice' existe em 'vertices'.
        2. Obter o índice 'i' correspondente.
        3. Criar uma lista de vizinhos vazia
        4. Para cada item da linha matriz[i], verificar se == 1
            - Adicionar o vértice correspondente na lista de vizinhos
        5. Retornar essa lista.
        """
        if vertice not in self.vertices:
            return []
        vizinhos = []
        i = self.vertices.index(vertice)
        for linha in self.matriz:
            if linha[i] == 1:
                index_vizinho = self.matriz.index(linha)
                vizinhos.append(self.vertices[index_vizinho])


    def bfs(self) -> List[str]:
        visitados = []
        if len(self.vertices) == 0: return []
        fila = [self.vertices[0]]
        while len(fila) > 0:
            v =fila.pop(0)
            visitados.append(v)
            vizinhos = self.vizinhos(v).sort()
            for vizinho in vizinhos:
                if vizinho in fila or vizinho in visitados:
                    continue
                fila.append(vizinho)
        return visitados
    
    def menor_caminho(self, origem, destino) -> List[str]:
        visitados = []
        if len(self.vertices) == 0: return []
        fila = [{
            'vertice': origem,
            'caminho': [],
        }]
        while fila:
            v =fila.pop(0)
            vertice = v['vertice']
            caminho = v['caminho']
            if vertice == destino:
                return caminho
            visitados.append(v)
            vizinhos = self.vizinhos(vertice).sort()
            for vizinho in vizinhos:
                # se esta na fila
                if vizinho in [i['vertice'] for i in fila]:
                    continue
                if vizinho in visitados:
                    continue
                fila.append({
                    'vertice': vizinho,
                    'caminho': caminho + [vizinho]
                })
        return []

