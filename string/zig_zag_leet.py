def convert(s, numRows):
    L = []
    for i in range(numRows):
        L.append([])
    index = 0
    for ch in s:
        L[index].append(ch)
        if index == 0:
            step = 1
        if index == numRows - 1:
            step = -1
        index += step
        
    return ''.join([''.join(item) for item in L])
        
        
print(convert("thisisazigzag",4))