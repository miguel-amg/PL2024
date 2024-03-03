""" Name: Miguel Guimarães
    University: Universidade do Minho
    Processamento de Linguagens 2024 / Language processing 2024 """ 

# Line for testing: SELECT id, nome, salario FROM empregados WHERE salario >= 820

######################## Imports ########################
import ply.lex as lex
import sys

######################## Setup ########################
# These wont be recognized as VAR
reserved = {
   'SELECT' : 'SELECT',
   'FROM'   : 'FROM',
   'WHERE'  : 'WHERE',
}

# List of recognized tokens
tokens = (
   'VAR',
   'COMMA',
   'GREATER_EQ',
   'SKIP',
   'VALUE',   
   'ERROR'
) + tuple(reserved.values())

# Regex for each token
t_COMMA      = r','       # (Signal) Regex for the ',' token 
t_GREATER_EQ = r'>='      # (Reserved word) Regex for the '>=' token
t_SKIP       = r'[\s\t]+' # (Reserved word) Regex for spaces and tabs
t_VALUE      = r'\d+'     # (Terminal variable) Regex for numbers
t_ERROR      = r'.'       # Everything else is not recognized

######################## Build ########################
# Definition of VAR token
def t_VAR(t):
    r'[a-zA-Z][$_a-zA-Z1-9]*' # (Terminal variable) Regex for SQL variable names (starting with a letter, followed by letters, numbers, underscores, or dollar signs)
    t.type = reserved.get(t.value.upper(),'VAR')  # Check if the word is in the reserved word list, if it isnt then default is VAR
    return t

# Error handling
def t_error(t):
    print("Character not recognized: '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

######################## Read stdin and run lex ########################
for line in sys.stdin:
    # Give the lexer some input
    lexer.input(line)

    # Print the test
    for tok in lexer:
        print(tok)
        print(tok.type, tok.value, tok.lineno, tok.lexpos)