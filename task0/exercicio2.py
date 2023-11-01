# EXERCICIO 2
'''
Implemente um autômato finito que reconheça todas as ocorrências da palavra computador
no texto T. O programa deve apontar em quais posições ocorreram o casamento exato da
palavra.
'''

texto ="O computador é uma máquina capaz de variados tipos de tratamento automático de informações ou processamento de dados. Entende-se por computador um sistema físico que realiza algum tipo de computação. Assumiu-se que os computadores pessoais e laptops são ícones da era da informação. O primeiro computador eletromecânico foi construído por Konrad Zuse (1910–1995). Atualmente, um microcomputador é também chamado computador pessoal ou ainda computador doméstico."
padrao ='computador'


def casamento_exato (texto, padrao, exato=False):
    
    #PROCESSAMENTO DO PADRAO
    if exato:
        padrao =' '+padrao+' ' # Modifica o padrao para casos em que casamento exato = True
   
    mascara_de_bits ={} # Inicialização das máscaras
    m =len(padrao) # Obtem o comprimento do padrao
    
    
    for i in range(m):
        if padrao[i] not in mascara_de_bits:
            mascara_de_bits[padrao[i]] = 1 << (m - 1 - i)
        else:
            mascara_de_bits[padrao[i]] |= 1 << (m - 1 - i)
            # atualiza mascara de bits para carecteres repetidos
 

    # EXECUCAO DO ALGORITMO    
    # Inicialização do vetor de bits e das posicoes
    n =len(texto) # Obtem o comprimento do texto
    R =0
    palavra_fixa =1<<(m-1) # Representa a palavra fixa 10^(m-1)  
    posicoes =[]

    for i in range(n):
        R = ((R >> 1) | palavra_fixa) & mascara_de_bits.get(texto[i], 0) 
        # Metodo get(x,0) busca o item na posicao x e se nao tiver retorna 0
        
        if R & 1: # Verifica se o vector encontrado e do tipo 0^(m)1
            if exato:
                posicoes.append(i-m+2)
            else:
                posicoes.append(i-m+1)

    return posicoes


# Execucao do codigo
# casamento_exato (texto, padrao)
# Imprime [2, 133, 218, 294, 384, 412, 440]

casamento_exato (texto, padrao, True)
# Imprime [2, 133, 294, 412, 440]