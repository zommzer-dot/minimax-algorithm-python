values =[[[5,6],[10,15]],[[20,30],[7,2]]]
def minimax(node, ismax):

    if type(node) == int:
        return node
#max
    if ismax:
        best = -float('inf')
        for child in node:
            value = minimax(child, False)
            best = max(best, value)
        return best
#min
    else:
        best = float('inf')
        for child in node:
            value = minimax(child, True)
            best = min(best, value)
        return best   


print(minimax(values, True))
     
