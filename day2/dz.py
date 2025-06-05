# def F(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return F(n-1) * (n+1) + 5
# print(F(7)) 



# def F(n):
#     if n == 1:
#         return 1 
#     if n > 1 and n % 2 != 0:
#         return n + 5*F(n-2)
#     if n > 1 and n % 2 == 0:
#         return 2 * n * F(n-1)
    
# print(F(9))


# F = [0]*3000
# for n in range(1,3000):
#     if n == 1:
#         F[n]=1
#     if n > 1:
#         F[n] = 2 *n * F[n-1]-1
# print(F[2000]/F[1997])  

def F(n):

    if n >= 2025:

        return n

    return n // 2 + F(n + 3)

print(F(2020) - F(2023))