def is_even(i):
    """
    esta função recebe um valor como argumento que será utilizado como um range dentro de um loop for, diante disso
    retorna cada numero dentro do range informando se é positivo ou negativo
    """
    return i%2==0
print("numbers between 1 and 10: even or odd?")

for i in range(1, 11):
    if is_even(i):
        print(i, "even")
    else:
        print(i, "odd")
