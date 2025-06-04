# def F(n):
#     if n == 0:
#         return 0
#     if n >= 1 :
#         return F(n-1) + n
# print(F(5))



# def F(n):
#     if n == 0:
#         return 0
#     if n % 2 == 0 :
#         return F(n//2)
#     if n % 2 != 0:
#         return 1+ F(n-1) 

# for n in range(1,10000):
#     if F(n) == 12:
#         print(n)
#         break


 
# def F(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return n * F(n-1)
# print(F(2222) / F(2219))


# F = [0] * 3000
# for n in range(1,3000):
#     if n == 1:
#         F[n] = 1
#     if n > 1:
#         F[n] = n *F[n-1]
# print(F[2222]/F[2219])


# F = [0]*3000
# for n in range(2999,0,-1):
#     if n > 2026:
#         F[n] = n
#     if n <= 2026:
#         F[n] = n * F[n+1]
# print(F[2024]/F[2026])



# def F(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return 2 *G(n) + 3 *n  
# def G(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return F(n-1) + 5 * n
# print(F(4)- G(5))



