from typing import List, Dict

class Grafo:
    def __init__(self, direcionado:bool) -> None:
    # Cria e retorna uma matriz de adjacência vazia e uma lista de vértices.
    
    # Passos:
    # 1. Define se é direcionado.
    # 2. Inicializa matriz e lista de vertices vazias.
        self.direcionado = direcionado
        self.matriz = []
        self.vertices = []

    def inserir_vertice(self, vertice:str):
        """
        Adiciona um novo vértice ao grafo.
        """
        if vertice in self.vertices:
            return
        
        self.vertices.append(vertice)
        for linha in self.matriz:
            linha.append(0)

        nova_linha = []
        for i in range(len(self.vertices)):
            nova_linha.append(0)

        self.matriz.append(nova_linha)

    def inserir_aresta(self, origem, destino):
        """
        Adiciona uma aresta entre dois vértices.
        """
        if origem not in self.vertices:
            self.inserir_vertice(origem)
        if destino not in self.vertices:
            self.inserir_vertice(destino)
        
        i_origem = self.vertices.index(origem)
        i_destino = self.vertices.index(destino)

        self.matriz[i_origem][i_destino] = 1

        if not self.direcionado:
            self.matriz[i_destino][i_origem] = 1

    def vizinhos(self, vertice):
        """
        Retorna a lista de vizinhos para onde o vértice aponta.
        
        Passos:
        1. Acha o índice do vértice.
        2. Percorre a linha desse vértice na matriz.
        3. Se for 1, adiciona na lista.
        """
        if vertice not in self.vertices:
            return []
        
        vizinhos_lista = []
        i_vertice = self.vertices.index(vertice)
        
        # Percorre a linha do vértice (para onde ele vai)
        linha = self.matriz[i_vertice]
        for i in range(len(linha)):
            if linha[i] == 1:
                vizinhos_lista.append(self.vertices[i])
        
        return vizinhos_lista

    def exibir_grafo(self):
        print("  " + " ".join(self.vertices))
        for i in self.matriz:
            print(self.vertices[self.matriz.index(i)] +" " + " ".join([str(x) for x in i]))
    
    
    # ATIVIDADE- BUSCA EM PROFUNDIDADE


    def dfs_padrao(self, inicio: str) -> List[str]:
        """
        [cite_start]1 - Busca em Profundidade Padrão [cite: 328, 399]
        
        Passos:
        1. Inserir o vértice inicial na Pilha.
        2. Enquanto a Pilha não estiver vazia:
           - Retirar o vértice da Pilha (LIFO).
           - Se não foi visitado, marcar e pegar vizinhos.
           - Adicionar vizinhos não visitados na pilha.
        """
        visitados = []
        if inicio not in self.vertices:
            return []
        
        pilha = [inicio]

        while len(pilha) > 0:
            # pop() sem indice remove o ultimo (LIFO - Pilha)
            vertice_atual = pilha.pop()

            if vertice_atual not in visitados:
                visitados.append(vertice_atual)
                
                # Pega os vizinhos
                lista_vizinhos = self.vizinhos(vertice_atual)
                
                # Adiciona na pilha
                for vizinho in lista_vizinhos:
                    if vizinho not in visitados:
                        pilha.append(vizinho)
                        
        return visitados

    def dfs_ciclo(self, inicio: str) -> bool:
        """
        [cite_start]2 - Implemente a detecção de ciclos utilizando Busca em Profundidade [cite: 395, 400]
        
        Passos:
        1. Pilha guarda dicionario com vertice e pai.
        2. Enquanto pilha nao vazia:
           - Tira item.
           - Se vizinho ja visitado e nao for o pai -> CICLO DETECTADO.
        """
        if inicio not in self.vertices:
            return False
            
        # Estrutura igual ao slide: vertice e pai
        pilha = [{
            'vertice': inicio,
            'pai': None
        }]
        
        visitados = []

        while len(pilha) > 0:
            item = pilha.pop()
            vertice_atual = item['vertice']
            pai_atual = item['pai']

            if vertice_atual not in visitados:
                visitados.append(vertice_atual)
            
            lista_vizinhos = self.vizinhos(vertice_atual)

            for vizinho in lista_vizinhos:
                # Se nao foi visitado e nao ta na pilha (simplificado verificando visitados)
                if vizinho not in visitados:
                    pilha.append({
                        'vertice': vizinho,
                        'pai': vertice_atual
                    })
                else:
                    # Se ja foi visitado, tem que ser o pai. Se nao for o pai, é ciclo.
                    if vizinho != pai_atual:
                        return True
                        
        return False

def main():
    # Teste conforme pede a atividade
    g = Grafo(direcionado=False)
    
   
    g.inserir_aresta("A", "B")
    g.inserir_aresta("B", "C")
    g.inserir_aresta("C", "A") 
    g.inserir_aresta("A", "D")

    print(" Matriz")
    g.exibir_grafo()

    print("\n Busca em Profundidade Padrão (DFS) ")
    caminho = g.dfs_padrao("A")
    print(f"Visitados: {caminho}")

    print("\n  Detecção de Ciclos ")
    tem_ciclo = g.dfs_ciclo("A")
    if tem_ciclo:
        print("Ciclo detectado no grafo!")
    else:
        print("Nenhum ciclo encontrado.")

if __name__ == "__main__":
    main()
