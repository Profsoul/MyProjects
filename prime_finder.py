#! /usr/bin/env python
#Finding Prime Number


def prime_finder(value):
    value_list = list(range(2,value+1))
    value_list_cp = value_list.copy()
    
    for item in value_list:
        flag = True
        for item_cp in value_list_cp:
            if item != item_cp and item_cp % item == 0:
                value_list_cp.remove(item_cp)
                flag = False
        if flag:
            break
    return value_list_cp
            


if __name__ == "__main__":
    value = int(input('Enter Value: '))
    if value >0:
        result = prime_finder(value)
        print(result)
    else:
        print('The Integer Must be Positive integer')
