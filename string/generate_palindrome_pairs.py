'''
Given a list of words, find all pairs of unique indices such that the concatenation of
the two words is a palindrome.
For example, given the list [ code,edoc,da,d],
return [ ( 0, 1), ( 1, 0), (2, 3)].
'''         
def is_palindrome(word:str)->bool:
    if(word == word[::-1]):
        return True
    return False

def generate_palindrome_index(word:list)->list:
    unique_list = []
    words_dic = {}
    for i, w in enumerate(word):
        words_dic[w] = i
    for i, w in enumerate(word):
        is_reverse = False
        for ch in range(len(w)):
            is_begin_pal = is_palindrome(w[0:ch+1])
            pal_pair_index = None
            if(is_begin_pal):
                pal_word = w[-1:ch:-1]
                pal_pair_index = words_dic.get(pal_word,None)
            else:
                if(is_reverse == False):
                    pal_word = w[::-1]
                    pal_pair_index = words_dic.get(pal_word, None)
                    is_reverse = True
            if pal_pair_index != None:
                    unique_list.append([i, pal_pair_index])
    return unique_list
'''
Idea: 
Rather than checking if any words after concat with current word will become palendrome. 
We find the possiblity of words which when concat with current words will give palandromic string
--> Current_Word + Other_Word

* Note: We also check if the current word is concated with any other words and gives palandromic string
--> Other_Word + Current_Word

Example:
word: sssl
Lets divide the word into prefix and suffix

For instance break sssl into 
Prefix: s
Suffix: ssl

Case 1: When Prefix is Palendrome
-> When Prefix is palendrome on itself, then I know that if I have the reverse of remaining suffix and insert that infront of my 
current word I will get a palendrome string
Ex: 's' is a palendrom. Reverse of suffix: lss
So Reverse_Suffix + Current_Word = Palendrome : lss + sssl =  lsssssl

Case 2: When Suffix is Palendrome
-> When Suffix is Palendrome on itself, then I know that if I have the reverse of Prefix and append to the end of my current word I will get palendrome
Suppose the current word is sll
And my Prefix: s
Suffix: ll
Then in this case suffix is palendrome, and if I append reverse of prefix in the end of my current word I will get paledrome
-> Current_Word + Reverse_Prefix = sll + s = slls

'''
def generate_palindrome_less_time(words: list) -> list:
    unique_words = {value:index for index, value in enumerate(words)}
    unique_index = []
    for index, word in enumerate(words):
        for ch in range(len(word)):
            prefix_ch = word[:ch]
            surfix_ch = word[ch:]
            reverse_prefix = prefix_ch[::-1]
            reverse_sufix = surfix_ch[::-1]
            if(is_palindrome(prefix_ch) and unique_words.get(reverse_sufix, -1) != -1 and index != unique_words[reverse_sufix]):
                unique_index.append([unique_words[reverse_sufix], index])
            if(is_palindrome(surfix_ch) and unique_words.get(reverse_prefix, -1) != -1 and index != unique_words[reverse_prefix]):
                unique_index.append([index, unique_words[reverse_prefix]])
    return unique_index





print(generate_palindrome_less_time(["abcd","dcba","lls","s","sssll"]))

