f = open("dz_17/4.txt")
a = [int(s) for s in f]
max13 = max([q for q in a if q % 100 == 13 ])
sum_par = []
cnt = 0
for i in range(len(a)-2):
    if ( ((len(str(a[i]))) == 5) + ((len(str(a[i+1]))) == 5) + ((len(str(a[i+2]))) == 5)) == 2 and (a[i]+a[i+1]+a[i+2] <= max13):
         cnt += 1
         sum_par.append(a[i]+a[i+1]+a[i+2])
print(cnt,max(sum_par))