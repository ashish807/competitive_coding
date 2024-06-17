'''
   *
  * *
 * * *
* * * *  
'''
def print_star(max_star: int):
    for row in range(1, max_star+1):
        count_star = 0 
        begining_star = max_star - row
        for column in range(max_star+1+row):
            if (column < begining_star or count_star >= row):
                print(" ", end="")
            else:
                print("* ", end="")
                count_star+=1

        print("")


        


