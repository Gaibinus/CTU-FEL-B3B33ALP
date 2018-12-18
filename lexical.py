#Filip Geib filip@geib.sk
#CTU FEL KYR B3B33ALP 2018/19
#homework no. 9

import sys, re, collections

#pattern for output storage
Pattern = collections.namedtuple('list', ['type', 'value'])

def tokenzie(data):
    operators=['+', '-', '*', '**', '/', '//', '%', '<<', '>>', '&', '|', '^', '~', '<', '>', '<=', '>=', '==', '!=']
    sepparators=['(', ')', '[', ']', '{', '}', ',', ':', '.', ';', '@', '=', '->', '+=', '-=', '*=', '/=', '//=', '%=', '@=', '&=', '|=', '^=', '>>=', '<<=', '**=']
    keyTerms=['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
    specification=[
        ('Rea', r'\d*(\.\d+([eE][-+]?\d+)?|[eE][-+]?\d+|\d*\.)'),
        ('Dec', r'([1-9]+\d*|0(o|O)[0-7]+|0(x|X)(\d|[a-f]|[A-F])+|0(b|B)(0|1)+|0+)'),
        # ('Oct', r'0(o|O)[0-7]+'),
        # ('Hex', r'0(x|X)([a-f]|[A-F])+'),
        # ('Bin', r'0(b|B)(0|1)+'),
        ('Var', r'([a-z]|[A-Z])+[\d\w_]*'),
        ('ST1', r"('''.*?\n*?\'''|'('|.*?\n*?[^\\]'))"),
        ('ST2', r'(""".*?\n*?"""|"("|.*?\n*?[^\\]"))'),
        ('OS', r'((\+=|\+)|(-\>|-)|(\*\*=|\*\*|\*=|\*)|(//=|//|/=|/)|(%=|%)|(\<\<=|\<\<|\<=|\<)|(\>\>=|\>\>|\>=|\>)|(&=|&)|(\|=|\|)|(\^=|\^)|~|(==|=)|!=|\(|\)|\[|\]|\{|\}|,|:|\.|;|(@=|@))'),
    ]
    tokRegex = '|'.join('(?P<%s>%s)' % pair for pair in specification)
    for mo in re.finditer(tokRegex, data):
        type=mo.lastgroup
        value=mo.group()

        if type=='Rea':
            pass

        elif type=='Dec':
            type='Int'

        elif type=='Oct':
            type='Int'

        elif type=='Hex':
            type='Int'

        elif type=='Bin':
            type='Int'

        elif type=='Var':
            if value in keyTerms: type='Key'

        elif type=='OS':
            if value in sepparators: type='Sep'
            elif value in operators: type='Ope'
            else:
                #print("OS-error",str(value))
                call=0

        elif type=='ST1' or type=='ST2':
            type='Str'
            if len(value)>=3 and value[0]==value[1]==value[2]:
                for j in range(3):
                    value=value[1:]
                    value=value[:-1]
            else:
                value=value[1:]
                value=value[:-1]

            #hotfixes
            value=value.replace("\\'","'")
            value=value.replace('\\"','"')
            value=value.replace("\\\\","\\")
            value=value.replace("\\+","+")
            value=value.replace("\\-","-")
            #replace special character back to new line
            value=value.replace('$    ','\n')

        yield Pattern(type, value)

#main-------------------------------------------------------------------------------------------------------------------

#load file and replace new lines with special character
with open(sys.argv[1], 'r') as file:
    string=file.read().replace('\n', '$')

#run the script
for type, value in tokenzie(string):
    print(type,": ",value, sep='')