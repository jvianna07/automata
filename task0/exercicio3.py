# EXERCICIO 3

'''
Implemente um transdutor finito (máquina de Moore ou Mealy) que, dada uma sequência de
moedas de 25 e 50 centavos e de 1 real, forneça uma lata de refrigerante quando a sequência
totalizar 1 real ou mais. Cada moeda inserida deverá corresponder a uma de duas saídas: 0, se
uma lata não pode ser (ainda) liberada, ou 1, se uma lata deve ser liberada.
'''

# Definindo as transições (estado, entrada) -> próximo estado
transicoes={
    ('q0',25):'q1',
    ('q0',50):'q2',
    ('q0',100):'q3',
    
    ('q1',25):'q2',
    ('q1',50):'q4',
    ('q1',100):'q5',
    
    ('q2',25):'q4',
    ('q2',50):'q3',
    ('q2',100):'q6', 
    
    ('q3',25):'q1',
    ('q3',50):'q2',
    ('q3',100):'q3',
    
    ('q4',25):'q3',
    ('q4',50):'q5',
    ('q4',100):'q7',
    
    ('q5',25):'q2',
    ('q5',50):'q4',
    ('q5',100):'q5',
    
    ('q6',25):'q4',
    ('q6',50):'q3',
    ('q6',100):'q6',
    
    ('q7',25):'q3',
    ('q7',50):'q5',
    ('q7',100):'q7'
    
}

# Definindo as saídas (estado, entrada) -> saída
saidas ={
    ('q0',25):0,
    ('q0',50):0,
    ('q0',100):1,
    
    ('q1',25):0,
    ('q1',50):0,
    ('q1',100):1,
    
    ('q2',25):0,
    ('q2',50):1,
    ('q2',100):1,
    
    ('q3',25):0,
    ('q3',50):0,
    ('q3',100):1,
    
    ('q4',25):1,
    ('q4',50):1,
    ('q4',100):1,
    
    ('q5',25):0,
    ('q5',50):0,
    ('q5',100):1,
    
    ('q6',25):0,
    ('q6',50):1,
    ('q6',100):1,
    
    ('q7',25):1,
    ('q7',50):1,
    ('q7',100):1
}

# Definindo o estado inicial
e_inicial ='q0'


# Definindo a função Máquina de Refri
def maquina_refrigerante(transicoes, saidas, e_inicial, moedas):
    estado =e_inicial
    sequencia_de_saida =[]
    
    for moeda in moedas:
        # Mapeia o estado e a moeda de entrada para saber qual o proximo estado
        novo_estado = transicoes[(estado, moeda)]
        
        # Mapeia o estado e a moeda de entrada pra saber qual o simbolo de saida
        simbolo_de_saida = saidas[(estado, moeda)]
        
        estado = novo_estado # Atualiza o estado para novo estado
        sequencia_de_saida.append(simbolo_de_saida) # Atualiza o simbolo de saida na sequencia de saida
    
    return sequencia_de_saida


# Executando o código
moedas=[50,25,50,100,25,50,100] 

print(maquina_refrigerante(transicoes, saidas, e_inicial, moedas)) # Deve imprimir [0, 0, 1, 1, 0, 1, 1]