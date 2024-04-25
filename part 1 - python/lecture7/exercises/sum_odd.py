def sum_odd(a, b):
    """
    esta função recebe dois valores como argumentos e dentro de um loop for, calcula dentro de um range, apenas a soma dos valores ímpares
    """
    sum_of_odds = 0
    for i in range(a, b+1):
        if i%2!=0:
            sum_of_odds += i

    return sum_of_odds
 
print(sum_odd(2, 7))