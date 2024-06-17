def greater_index(k_string):
    max_index = 0
    max_alphbet = ""
    if(k_string[0]>=k_string[1]):
        max_index = 0
        max_alphbet = k_string[0]

    for i in range(2, len(k_string)):
        if(k_string[i] > max_alphbet):
            max_alphbet = k_string[i]
            max_index = i
    return max_index
            
ss ="GEEKSQUIZ"
k=3
found_lex = False
i = 0

while(found_lex == False):
    idx = greater_index(ss[:k])
    temp = ss[:idx] + ss[idx+1:] if idx+1 < len(ss) else ""
    ss = temp + ss[idx]
    for j in range(len(ss)-1):
        if(ss[j] > ss[j+1]):
            found_lex = False
            break
        else:
            found_lex = True
    i+=1

print(ss)





