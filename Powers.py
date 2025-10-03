def power_three(a, b, n):
    return a**2 , b**3 , n**4



def sum_of_powers(a, b, n):
    x, y, z = power_three(a, b, n)
    return x + y + z
print(sum_of_powers(3, 4, 5))