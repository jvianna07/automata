# Funcao de transicao para o exercicio 1_a)
transitions_1a={
    ('q0','a','Z'):('q0','XZ'),
    ('q0','a','X'):('q0','XX'),
    ('q0','c','Z'):('q2','Z'),
    ('q0','b','X'):('q1','$'),   
    ('q1','b','X'):('q1','$'),
    ('q1','c','Z'):('q2','Z'),
    ('q2','c','Z'):('q2','Z'),
    ('q2','$','Z'):('q2','$')
}

# Funcao de transicao para o exercicio 1_b)
transitions_1b={
    ('q0','a','Z'):('q0','XXXZ'),
    ('q0','a','X'):('q0','XXXX'),
    ('q0','b','X'):('q1','$'),
    ('q1','b','X'):('q1','$'),
    ('q1','$','Z'):('q1','$')
}

initial_state='q0'