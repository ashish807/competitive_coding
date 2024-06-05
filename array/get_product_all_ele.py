''''
Given an array of integers, return a new array such that each element at index i of
the new array is the product of all the numbers in the original array except the one
at i.
For example, if our input was [ 1, 2, 3, 4, 5], the expected output would be [ 120,
60, 40, 30, 24]. Ifourinputwas [3, 2, 1],theexpectedoutputwouldbe [2,
3, 6]
'''
def get_product_all_ele(array: list):
    new_prod_list = []
    all_prod = 1
    for i in range(len(array)):
        all_prod*=array[i]

    for i in range(len(array)):
        prod =1
        if(array[i]!=0):
            prod = int(all_prod / array[i])
        else:
            prod = 0
        new_prod_list.append(prod)
    print(new_prod_list)

def get_prduct_On(array: list):
    prefix_product =[]
    suffix_product = []
    new_prod = []
    # product of i is (product of all left element * product of all right element)
    for num in array:
        if prefix_product:
            prefix_product.append(prefix_product[-1]*num)
        else:
            prefix_product.append(num)
    for num in reversed(array):
        if suffix_product:
            suffix_product.append(suffix_product[-1]*num)
        else:
            suffix_product.append(num)

    suffix_product.reverse()

    for i in range(len(array)):
        if(i==0):
            new_prod.append(suffix_product[i+1])
        elif(i==len(array)-1):
            new_prod.append(prefix_product[i-1])
        else:
            new_prod.append(prefix_product[i-1] * suffix_product[i+1])
    print(new_prod)




if __name__ == "__main__":
    array = [1,2,3,4,5]
    get_prduct_On(array)
