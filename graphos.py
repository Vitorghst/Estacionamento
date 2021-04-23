def gerar_caminhos(grafo, caminho, final):


    if caminho[-1] == final:
     yield caminho
     return
    
    for vizinho in grafo[caminho[-1]]:

        if vizinho in caminho:
             continue

        for caminho_maior in gerar_caminhos(grafo, caminho + [vizinho], final):
            yield caminho_maior


grafo = {
    "Rolandia"       :  {"Cambé":        5, "Sertanopolis"   : 15, "Warta":  2},
    "Cambé"          :  {"Rolandia":     1, "Ibipora"        :  9, "Sertanopolis":22, "Warta":  4},
    "Londrina"       :  {"Ibipora":     12, "Sertanopolis"   :  1 },
    "Ibipora"        :  {"Cambé":        9, "Londrina"       : 12, "Warta"  :6},
    "Sertanopolis"   :  {"Rolandia":    15, "Cambé"          : 22, "Londrina": 1},
    "Warta"          :  {"Rolandia":     2, "Cambé"          :  4, "Ibipora": 6}

}
for caminho in gerar_caminhos(grafo, ['Sertanopolis'], 'Londrina'):
    print(caminho)