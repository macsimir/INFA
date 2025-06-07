# print("x y z w")
# for x in range(2):
#     for y in range(2): 
#         for z in range(2):
#             for w in range(2):
#                 if ((x and (not(y))) or (y==z) or w) == 0:
#                     print(x,y,z,w)


# print("x y z w")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                     if ((x or y) and (not(y == z )) and (not(w))) == 1:
#                          print(x,z,y,w)


print("x y z w F")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((x <= y ) == (z <= (not(w)))) and (z or y)
                print(x,y,z,w,int(F))