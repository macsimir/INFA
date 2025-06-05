# print(all([1,1,0]))
# all -> and 

# print(any([0,1,1]))
# any -> or

# П - первый Петя
# В - второй Ваня



# def game(s,p,end):
#     '''S - кол-во камней, P - позиция , End- за сколько ходо хочется победить'''
#     if s >= 37 and p == end:
#         """Игра закончена если камней больше 37 камней и позиция конечная"""
#         return True 
#     if s >= 37 and p != end:
#         """Победили ходом, который нас не устраивает!"""
#         return False
#     if p > end:
#         return False
#     if (p+1) % 2 == (end % 2):
#         """Проверям на игрока"""
#         return game(s + 1, p + 1, end) or  game(s +4, p + 1, end) or game(s * 3, p + 1, end)
#     else:
#         return game(s + 1, p + 1, end) and game(s +4, p + 1, end) and game(s * 3, p + 1, end)
# for s in range(1,37):
#     """Перебираем s и печатаем все s с которыми мы можем выйграть за один ход"""
#     if game(s,0,2):
#         print(s)



"""Сокращенный вариант кода"""
# def game(s,p,end):
#     if s >= 37: return p in end
#     if p >= max(end): return False
#     moves = [game(s + 1, p + 1, end),  game(s +4, p + 1, end) , game(s * 3, p + 1, end)]
#     return any(moves) if (p+1) % 2 == (end[0] % 2) else all(moves)
"""19.аб"""
# for s in range(1,37):
#     """Перебираем s и печатаем все s с которыми мы можем выйграть за один ход"""
#     if game(s,0,1):
#         print(s)
"""20"""
# for s in range(1,37):
#     """Перебираем s и печатаем все s с которыми мы можем выйграть за один ход"""
#     if game(s,0,3):
#         print(s)
"""21"""
# for s in range(1,37):
#     """Перебираем s и печатаем все s с которыми мы можем выйграть за один ход"""
#     if game(s,0,[2,4]):
#         print(s)



# """Две кучи"""
# def game(x,s,p,end):
#     if (s + x) >= 107:return p in end
#     if p >= max(end): return False
#     moves = [game(x+1,s,p+1,end), game(x*2,s,p+1,end),
#              game(x,s+1,p+1,end),game(x,s*2,p+1,end)]
#     return any(moves) if (p+1) % 2 == (end[0]% 2 ) else all(moves)
# x = 13
# # for s in range(1,94):
# #     if game(x,s,0,[3]):
# #         print(s)
# for s in range(1,94):
#     if game(x,s,0,[3]):
#         print(s)



"""3 задача"""
# def game(x,s,p,end):
#     if (x+s) >= 151:return p in end
#     if p >= max(end): return False
#     moves = [game(x+1,s,p+1,end),game(x+4,s,p+1,end),
#              game(s+1,x,p+1,end),game(s+4,x,p+1,end)]
#     return any(moves) if (p+1) % 2 == (end[0] %2) else all(moves)
# x = 11 
"""19"""
# for s in range(1,138):
#     if game(x,s,0,[2]):
#         print(s)
"""20"""
# for s in range(1,138):
#     if game(x,s,0,[3]):
#         print(s)
"""21"""
# for s in range(1,138):
#     if game(x,s,0,[2,4]):
#         print(s)



def game(x,s,p,end):
    if (x+s) <= 20:return p in end
    if p >= max(end): return False
    moves = [game(x-1,s,p+1,end),game(x//2,s,p+1,end),
             game(x,s-1,p+1,end),game(x,s//2,p+1,end)]
    return any(moves) if (p+1) % 2 == (end[0] % 2) else all(moves) #Если он выигрывает то all а если проигрываем то any
x = 10
'''19'''
# for s in range(11,100):
#     if game(x,s,0,[2]):def game(x,s,p,end):
#     if (x+s) <= 20:return p in end
#     if p >= max(end): return False
#     moves = [game(x-1,s,p+1,end),game(x//2,s,p+1,end),
#              game(x,s-1,p+1,end),game(x,s//2,p+1,end)]
#     return any(moves) if (p+1) % 2 == (end[0] % 2) else all(moves) #Если он выигрывает то all а если проигрываем то any
# x = 10
#         print(s)
'''20'''
# for s in range(11,100):
#     if game(x,s,0,[3]):
#         print(s)
'''21'''
# for s in range(11,100):
#     if game(x,s,0,[2,4]) and not game(x,s,0,[2]):
#         print(s)
