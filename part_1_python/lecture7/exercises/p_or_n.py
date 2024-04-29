def retorno(x):
    """
    esta função recebe um valor como argumento e retorna "P" caso ele seja positivo 
    ou "N" caso ele seja negativo.
    """
    if x % 2 == 0:
        return "P"
    else:
        return "N"

value = retorno(20)
print(value)
