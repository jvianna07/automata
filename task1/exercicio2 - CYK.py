#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def read_grammar():
    # Abre e lê o arquivo da gramática (grammar.txt)
    with open('grammar.txt', 'r') as grammar_file:
        rules = grammar_file.read().splitlines()
        terminal_rules = []
        variable_rules = []

        # Separa as regras em regras terminais e variáveis
        for line in rules:
            left_side, right_side = line.split(" => ")
            right_side = right_side.split(" | ")

            for letter in right_side:
                if str.islower(letter):
                    terminal_rules.append([left_side, letter])
                else:
                    variable_rules.append([left_side, letter])

        return variable_rules, terminal_rules


def cyk(variable_rules, terminal_rules, input_string):
    length = len(input_string)

    variables_pos_0 = [var[0] for var in variable_rules]
    variables_pos_1 = [var[1] for var in variable_rules]

    # Inicializa uma tabela para programação dinâmica
    table = [[set() for _ in range(length - i)] for i in range(length)]

    # Preenche a tabela com base nas regras terminais e no algoritmo CYK
    for i in range(length):
        for rule in terminal_rules:
            if input_string[i] == rule[1]:
                table[0][i].add(rule[0])

    for i in range(1, length):
        for j in range(length - i):
            for k in range(i):
                combination_values = set()

                # Verifica se ambas as substrings não estão vazias
                if table[k][j] == set() or table[i - k - 1][j + k + 1] == set():
                    combinations = set()
                for first_letter in table[k][j]:
                    for second_letter in table[i - k - 1][j + k + 1]:
                        combination_values.add(first_letter + second_letter)
                combinations = combination_values

                # Verifica se as combinações estão nas regras de variáveis
                for combination in combinations:
                    if combination in variables_pos_1:
                        table[i][j].add(variables_pos_0[variables_pos_1.index(combination)])

     # Verifica se o símbolo inicial 'S' está na célula inferior esquerda da tabela
    if 'S' in table[length - 1][0]:
        print(f'A cadeia "{input_string}" pertence a gramatica.')
    else:
        print(f'A cadeia "{input_string}" nao pertence a gramatica.')

    return table


if __name__ == '__main__':
    # Lê a gramática e solicita a entrada do usuário para teste
    var_rules, term_rules = read_grammar()
    user_input = input("escreva a cadeia a ser testada:\n")
    result_table = cyk(var_rules, term_rules, user_input)

