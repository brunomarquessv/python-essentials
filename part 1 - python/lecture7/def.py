# def is_even(i):
#     return i%2==0

# print(is_even(3))

# print("numbers between 1 and 10: even or odd?")

# for i in range(1, 11):
#     if is_even(i):
#         print(i, "even")
#     else:
#         print(i, "odd")

def sum_odd(a, b):
    sum_of_odds = 0
    for i in range(a, b+1):
        if i%2!=0:
            sum_of_odds += i

    return sum_of_odds
 
print(sum_odd(2, 7))
    
"""
def div_by(n , d):
    return n%d==0
    
print(div_by(10, 3))
print(div_by(195, 13))
"""

