
print("x y z")
for x in range(2):
    for y in range(2):
        for z in range(2): 
            # if ((z <=((not(x)) and y) <= (z == y))) == 0:
            #     print(x,y,z)
            if ((z <= ((not(x)) and y)) <= (z == y)) == 0:
                print(x,y,z)

#Ответ zxy

