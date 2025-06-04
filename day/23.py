# def task23(start,end):
#     if start > end:
#         return 0
#     if start == end:
#         return 1
#     if start < end:
#         return task23(start+2 , end) + task23(start * 2, end)
# print(task23(1,26))



def task23(start,end):
    if start > end or start == 20:
        return 0
    if start == end:
        return 1
    return task23(start+1 , end) + task23(start * 2, end) + task23(start * 3 , end)
print(task23(2,25))