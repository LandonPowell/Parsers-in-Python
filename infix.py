x = input("> ").split()

def calculate(tokens):
    accumulator = float(tokens.pop(0))
    while len(tokens):
        if tokens[0] == '*':
            tokens.pop(0)
            accumulator *= float(tokens.pop(0))
        elif tokens[0] == '/':
            tokens.pop(0)
            accumulator /= float(tokens.pop(0))
        elif tokens[0] == '-':
            tokens.pop(0)
            accumulator -= float(tokens.pop(0))
        elif tokens[0] == '+':
            tokens.pop(0)
            accumulator += float(tokens.pop(0))
    return accumulator

print(calculate(x))
