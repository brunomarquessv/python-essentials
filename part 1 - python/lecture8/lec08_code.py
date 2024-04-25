# def add(x, y):
#     return x + y
# def mult(x, y):
#     print(x*y)

# add(1,2)
# print(add(2,3))
# mult(3, 4)
# print(mult(4, 5))

# def is_triangular(n):
#     """ n is an int > 0 
#         Returns True if n is triangular, i.e. equals a continued
#         summation of natural numbers (1+2+3+...+k) 
#     """
#     total = 0
#     for i in range(n+1):
#         total += i
#         if total == n:
#             return True
#     return False

# print(is_triangular(4))
# print(is_triangular(6))
# print(is_triangular(1))

def bisection_root(x):
    epsilon = 0.01
    low = 0
    high = x
    ans = (high + low) /2.0
    while abs(ans*2-x) >= epsilon:
        if ans**2 < x:
            low = ans
        else:
            high = ans
        ans = (high+low)/2.0
    return ans

def count_nums_with_sqrt_close_to(n, epsilon):
    """
    n is an int > 2
    epsilon is a positive number < 1
    Returns how many integers have a square root within epsilon of n
    """
    count = 0
    for i in range(n**3):
        #take the sqrt of i
        sqrt = bisection_root(i)
        if abs(n-sqrt) < epsilon:
            #know that sqrt within epsilon
            count += 1
    return count

print(count_nums_with_sqrt_close_to(10, 0.1))