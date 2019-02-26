Symbol = str
Number = (int, float)
Atom = (Symbol, Number)
List = list
Exp = (Atom, List)

def tokenize(chars: str) -> list:
    return chars.replace('(', ' ( ').replace(')', ' ) ').split()

def parse():
    pass

def eval():
    pass

program = '(begin (define r 10) (* pi (* r r)))'
print(tokenize(program))
