def game(x,p,end):
    if x <= 87:
        return p in end
    if p >= max(end):
        return False
    moves = [game(x-2,p+1, end), game(x//2, p+1,end)]
    return any(moves) if (p+1) % 2 == (end[0]%2) else all(moves)

print([x for x in range(89,1000) if game(x,0,end=[2])])
print([x for x in range(89,1000) if game(x,0,end=[2])])
