# Automato de reconhecimento por pilha vazia
def pushdown_Automata(transitions, initial_state, string): 
    if len(string)>0:
        processed_string=string+'$'
        stringLength=len(processed_string)
    else:
        return f"A cadeia foi rejeitada."
    current_state=initial_state
    stack=['Z'] # Inicializa a pilha com simbolo inicial Z_0
    top_of_stack=stack[len(stack)-1]
    

    # Operacoes da pilha (empilha e desempilha) 
    def stak_operations(stack, alfabeto_da_pilha):
        alfabeto_da_pilha=alfabeto_da_pilha[::-1]
        stack.pop()
        if stack==['']:
            pass
        else:
            if alfabeto_da_pilha=='$':
                pass
                # Desempilha
            else:
                # Empilha
                for a in alfabeto_da_pilha:
                    stack.append(a)

    # Movimentacao do cursor de acordo com a cadeia de entrada
    i=0                   
    while stringLength>0:
        cursor_position=processed_string[i]
        if transitions.get((current_state,cursor_position,top_of_stack),0): 
            alfabeto_da_pilha=transitions.get((current_state,cursor_position,top_of_stack),0)[1]
            stak_operations(stack, alfabeto_da_pilha)

            current_state=transitions.get((current_state,cursor_position,top_of_stack))[0]
            if len(stack)>0: top_of_stack=stack[len(stack)-1]
            i+=1
            stringLength-=1
            
        else:
            return f"Cadeia '{string}' rejeitada."
        if stringLength==0: #verifica se a cadeia e a pilha foram esvaziadas
            if stack==[] and cursor_position=='$' : 
                return f"Cadeia '{string}' aceita."
            else:
                return f"Cadeia '{string}' rejeitada."

# TESTE
# Importamos o ficheio que contem as transicoes e a definicao do estado inicial
import transition_functions

transitions=transition_functions.transitions_1a
initial_state=transition_functions.initial_state
cadeia='abcccc'
res=pushdown_Automata(transitions, initial_state, cadeia)
print(res)