# o valor da moeda convertida
def em(a,b):
    return a / b
# print(em(120, 1.32))

# # o que resta do orcamento
def getc(a,b):
    return a - b
# print(getc(127.5, 120))

# # total das contas , tirando os valores quebrados de cada conta( valor que sobram que nao sao divisiveis pelo valor padrao)
def bills(a,b):
    return a * int(b) 
# print(bills(5, 128.75))

# o numero de contas divisivel pelo valor de uma conta, dentro do orcamento
def nbill(a,b):
    return int(a // b)
print(nbill(125, 5))

# o valor que nao pode ser trocado referente ao padrao
def left_b(a,b):
    return a % b if a % b == 0 else (a - b*(a // b)) 
# print(left_b(127.5, 20))

# o valor maximo da moeda depois do spread somado a taxa de cambio
def excha(a,b,c,d):
     b += b*(c /100)
     exchange = em(a,b)
     print(exchange)
     lefttover = left_b(exchange,d)
     print(lefttover)
     
     return int(exchange - lefttover)

print(excha(127.5, 1.20, 10, 20))
