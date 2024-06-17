'''
https://leetcode.com/problems/find-all-anagrams-in-a-string/
Given a word wand a strings, find all indices ins which are the starting locations
of anagrams of w. For example, given w is ab ands is abxaba, return [ 0, 3, 4].
'''

def build_dic(strings:str)->dict:
    w_dic ={}
    for word in strings:
        w_dic[word]= w_dic.get(word, 0)+1
    return w_dic

def find_indexes_m_x_n(strings:str, words:str)->list[int]:
    w_dic ={}
    n = len(strings)
    m = len(words)
    w_dic = build_dic(words)
    list_indexes =[]
    for i in range(n-m+1):
        s = strings[i:i+m]
        str_dic =  build_dic(s)
        if(str_dic == w_dic):
            list_indexes.append(i)
    return list_indexes


def find_indexes_n(strings:str, words:str)->list[int]:
    w_dic ={}
    n = len(strings)
    m = len(words)
    w_dic = build_dic(words)
    s_dic = build_dic(strings[0:m])
    list_indexes = [0] if w_dic == s_dic else []

    for i in range(m, n):
        s_dic[strings[i-m]] -= 1
        s_dic[strings[i]] = s_dic.get(strings[i], 0) + 1 
        if(s_dic[strings[i-m]]==0):
            s_dic.pop(strings[i-m])

        if w_dic == s_dic:
            list_indexes.append(i-m+1)

    return list_indexes


if __name__ == "__main__":
    strings = "abxaba"
    words = "ab"
    list_indexes = find_indexes_n(strings, words)
    print(list_indexes)