# IP - АДРЕСС - 4 байта или 4 октета
# Поразрядной коньюнкции = умножение 



# from ipaddress import *
# cnt = 0
# ip_net = ip_network("172.16.80.0/255.255.248.0")
# for ip_add in ip_net:
#     if f"{ip_add:b}".count("1") % 2 != 0:
#         cnt += 1
# print(cnt)



# from ipaddress import *
# ip_net = ip_network("112.208.0.0/255.255.128.0")
# cnt = 0 
# for ip_add in ip_net:
#     if f"{ip_add:b}".count("1") % 11 == 0:
#         cnt += 1 
# print(cnt)


# from ipaddress import *
# ip_net = ip_network("11.92.135.56/255.224.0.0",0)
# print(ip_net[-2])


# from ipaddress import *
# ip_net = ip_network("98.81.154.195/255.252.0.0", 0)
# print(ip_net[-2])
#Последний = широковещатель



# from ipaddress import *
# ip_net = ip_network("252.67.33.87/255.255.0.0",0)
# cnt = 0
# for ip_add in ip_net:
#     if f"{ip_add:b}"[16:].count("1") > f"{ip_add:b}"[:16].count("1"):
#         cnt += 1 
# print(cnt)



