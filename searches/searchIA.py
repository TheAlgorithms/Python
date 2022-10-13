# Busca em largura

import queue

def bfs(grafo, vertice_fonte):
    queue
    visitados, fila = set(), [vertice_fonte]
    while fila:
        vertice = queue.pop(0)
        if vertice not in visitados:
            visitados.add(vertice)
            fila.extend(grafo[vertice] - visitados)
    return visitados
# Busca em Profundidade

def dfs(grafo):
    def dfs_recursiva(grafo, vertice):
        visitados.add(vertice)
        for vizinho in grafo[vertice]:
            if vizinho not in visitados:
                dfs_recursiva(grafo, vizinho)

    visitados = set()
    for vertice in grafo:
        if not vertice in visitados:
            dfs_recursiva(grafo, vertice)


def retorna_h(destino, node):
    def h(n):
        def caminhar(pos, visitados, distancia):
            caminhos = node[pos]
            distancias = []
            visitados.add(pos)
            if pos == destino:
                return distancia
            distancia += 1
            for novo_pos in caminhos:
                if novo_pos == destino:
                    return distancia
                if not novo_pos in visitados:
                    try:
                        distancias.append( caminhar(novo_pos,set(visitados), distancia) )
                    except:
                        pass
            return min(distancias)


        try:
            return caminhar(n,set(), 0)
        except:
            return None
                    
    return h

meu_h = retorna_h(final, nos)

print( meu_h(0) )

def retorna_caminho(destino, node, meu_h):
    def meu_f(n):
        def calculo_f(pos, g_anterior):
            valor = meu_h(pos)
            if not valor:
                raise Exception('Não há caminho para determinado destino')
            return g_anterior + valor
        pos = n
        g = 0
        path = [pos]
        try:
            while True:
                menor = 999999
                idx_menor = -1
                caminhos = node[pos]
                for caminho in caminhos:
                    if caminho == destino:
                        path.append(caminho)
                        return path
                    if caminho in path:
                        continue
                    heuristica = calculo_f(caminho, g+1)
                    if heuristica < menor:
                        menor = heuristica
                        idx_menor = caminho
                if idx_menor != -1:
                    pos = idx_menor
                    path.append(idx_menor)
                    g += 1
                    continue
                else:
                    break
        except:
            return []
        return path
    return meu_f

calcular_caminho = retorna_caminho(final, nos, meu_h)


            