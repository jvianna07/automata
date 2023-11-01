#EXERCICIO 1-A
'''Implemente AFD que aceite todas  as cadeias em $ \{0,1\}^* $ 
que representam cada 1 seguido imediatamente de dois 0.'''

# Definindo as transições
transicoes={
    "q0":{'0':"q0",'1':"q1"},
    "q1":{'0':"q2"},
    "q2":{'0':"q0"}  
}


# Definindo os estados (inicial e finais)
e_inicial='q0'
e_final=['q0']

# Definindo a função
def testAFD(transicoes, e_inicial, e_final, cadeia):
    estado = e_inicial
    
    for simbolo in cadeia:
        if simbolo in transicoes[estado]: # Verifica se no corrente estado tem transicao para o simbolo de entada.
            estado = transicoes[estado][simbolo] # Se TRUE, para cada símbolo da cadeia ele associa o estado para passar ao próximo estado
        else:
            return f"Cadeia '{cadeia}' rejeitada." # Se FALSE, pára o autômato e rejeita a cadeia
        
    if estado in e_final: # Verifica se o estado atual pertence ao conjunto dos estado finais (retorna TRUE ou FALSE)
        return f"Cadeia '{cadeia}' aceite."
    else:
        return f"Cadeia '{cadeia}' rejeitada."
    
# Executando o código    
print(testAFD(transicoes, e_inicial, e_final, '0100100'))