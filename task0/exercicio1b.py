#EXERCICIO 1-B
'''
Implemente AFD que aceite todas  cadeias em $ \{a,b\}^* $ 
de modo que o último símbolo seja b e o número de símbolos a seja par.
'''

# Definindo as transições
transicoes={
    "q0":{'a':"q1",'b':"q2"},
    "q1":{'a':"q0",'b':"q1"},
    "q2":{'a':"q1",'b':"q2"}
}


# Definindo os estados (inicial e finais)
e_inicial='q0'
e_final=['q2']


# Definindo a função
def testAFD(transicoes, e_inicial, e_final, cadeia):
    estado = e_inicial
    
    for simbolo in cadeia:
        # Verifica se no corrente estado tem transição para o símbolo de entrada.
        if simbolo in transicoes[estado]: 
            
            # Se TRUE, para cada símbolo da cadeia ele associa o estado para passar ao próximo estado
            estado = transicoes[estado][simbolo] 
        else:
            return f"Cadeia '{cadeia}' rejeitada." # Se FALSE, pára o autômato e rejeita a cadeia
    
    # Verifica se o estado atual pertence ao conjunto dos estado finais (retorna TRUE ou FALSE)
    if estado in e_final: 
        return f"Cadeia '{cadeia}' aceite."
    else:
        return f"Cadeia '{cadeia}' rejeitada."


# Executando o código    
print(testAFD(transicoes, e_inicial, e_final, 'babab')) # Deve imprimir: Cadeia 'babab' aceite