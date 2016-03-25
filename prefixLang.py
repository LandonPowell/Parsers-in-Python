 ###############COPYRIGHT##############,
########################################
####'                               '###
####    A prefix notation parser      '  ,##, ###, # #
####   made by Landon Powell, and        #  # #  # #,#
####    licensed under the ZLIB          #  # ###'  #
####            license.              ,  '##' #     #
####,                               ,###   R I G H T
########################################
 ###############COPYRIGHT##############'

varList = {} # list of variables

def varNames(variable):
    if type(variable) == float: return variable
    elif variable[0] == "'": return variable[1:-1]
    else: return varList[variable]

def calculate(tokens): # calculates operators
    if type(tokens) == list: operator = tokens.pop(0)
    else: operator = tokens

    # math operators
    if operator == '+':
        accumulator = 0
        for number in tokens:
            accumulator += calculate(number)
    elif operator == '*':
        accumulator = 1
        for number in tokens:
            accumulator *= calculate(number)
    elif operator == '/':
        return calculate(tokens[0])/calculate(tokens[1])
    elif operator == '%':
        return calculate(tokens[0])%calculate(tokens[1])
    elif operator == '-':
        accumulator = calculate(tokens.pop(0))
        for number in tokens:
            accumulator -= calculate(number)

    # comparison operators
    elif operator == '!':
        return int( calculate(tokens[0])!=calculate(tokens[1]) )
    elif operator == '=':
        return int( calculate(tokens[0])==calculate(tokens[1]) )
    elif operator == '>':
        return int( calculate(tokens[0])>calculate(tokens[1]) )
    elif operator == '<':
        return int( calculate(tokens[0])<calculate(tokens[1]) )

    # boolean operators
    elif operator == '&':
        return int( calculate(tokens[0]) and calculate(tokens[1]) )
    elif operator == '|':
        return int( calculate(tokens[0]) or calculate(tokens[1]) )

    # misc
    elif operator == 'p': # print
        return print(calculate(tokens[0]))
    elif operator == '?': # conditionals
        if calculate(tokens[0]): return calculate(tokens[1]) # if
        elif len(tokens) >= 3: return calculate(tokens[2])   # else
        else: return 0
    elif operator == ':': # sets variables
        varList[tokens[0]] = calculate(tokens[1])

    else: return varNames(tokens) # return value of token

    return accumulator # if no other returns

def parser(tokens):
    item = tokens.pop(0)
    if item == '(': # shout out to lispy
        newList = []
        while tokens[0] != ')':
            newList.append(parser(tokens))
        tokens.pop(0)
        return newList
    else:
        try: return float(item)
        except: return item

while True:
    tokenList = input("INPUT> ").replace('(',' ( ').replace(')',' ) ').split()
    print(calculate(parser(tokenList)))
